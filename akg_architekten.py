from bs4 import BeautifulSoup
import requests


def insert_new_dataset_into_mdb(mdb_uri, datenbank, collection, datensatz):
    from pymongo import MongoClient
    client = MongoClient(mdb_uri, 27017, maxPoolSize=500)
    db = client[datenbank]
    collection = db[collection]
    collection.insert_one(datensatz)

page = requests.get("http://akg-architekten.de/gallery")
soup = BeautifulSoup(page.content, "html.parser")

x = []
for a in soup.select("a[href^=/architekten/profile]"):
    profile_nr = int(a.get("href").replace("/architekten/profile/", ""))
    if profile_nr not in x:
        x.append(profile_nr)

for i in x:
    single_page = requests.get("http://akg-architekten.de/architekten/profile/" + str(i))
    soup_2 = BeautifulSoup(single_page.content, "html.parser")

    name = soup_2.find("h2", class_="profile-title").text
    # print(name.text)

    address = []
    for index, j in enumerate(soup_2.find_all("li", class_="detail-item")):
        address.append((j, index))
        # in address[0][0] befinden sich str, plz, ort, fon, fax
        # in address[1][0] ist mail
        # in address[2][0] internet
    single_address = str(address[0][0]).split("\n")
    # print(address)
    # print(len(address))

    strasse = "K/A"
    plz = "K/A"
    ort = "K/A"
    tele = "K/A"
    fax = "K/A"

    if len(single_address) >= 6:
        strasse = single_address[2].strip().replace("<br/>", "")

        plz_ort = single_address[3].strip().replace("<br/>", "")

        plz = plz_ort[0:5]
        ort = plz_ort[6:]
        tele = single_address[4].strip().replace("<br/>", "").replace("Fon ", "")
        try:
            if "Fax" in single_address[5]:
                fax = single_address[5].strip().replace("<br/>", "").replace("Fax ", "")
            else:  fax = "K/A"
        except IndexError:
            fax = "K/A"

        print(strasse)
        print(plz)
        print(ort)
        print(tele)
        print(fax)


    if "@" in address[1][0].text:
        mail = "www." + address[1][0].text
    else: mail = "K/A"

    print(mail)

    if "www" in address[2][0].text:
        internet = address[2][0].text
    else: internet = "K/A"

    print(internet)

    datensatz = {
        "firma_name": name,
        "firma_telefon": tele,
        "firma_fax": fax,
        "firma_strasse": strasse,
        "firma_plz": plz,
        "firma_ort": ort,
        "firma_email": mail,
        "firma_internet": internet,
    }

    insert_new_dataset_into_mdb(mdb_uri="192.168.100.5", datenbank='yanghi', collection='akg_architekten',
                                datensatz=datensatz)
    print(datensatz)
    print('################################################################################################')
