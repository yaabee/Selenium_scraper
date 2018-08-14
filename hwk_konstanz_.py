import requests
from bs4 import BeautifulSoup as bs

def insert_new_dataset_into_mdb(mdb_uri, datenbank, collection, datensatz):
    from pymongo import MongoClient
    client = MongoClient(mdb_uri, 27017, maxPoolSize=500)
    db = client[datenbank]
    collection = db[collection]
    collection.insert_one(datensatz)


url = 'https://www.hwk-konstanz.de/betriebe/suche-64,0,bdbsearch.html?search-searchterm=&search-filter-zipcode=*&search-filter-radius=250&search-filter-jobnr=&search-job=&search-filter-experience='
page = requests.get(url)
clean_text = page.text
prefix = 'https://www.hwk-konstanz.de'

soup = bs(clean_text, 'html.parser')

for link in soup.select('a[href^=/betriebe/]')[:10]:
    # print(link)
    href = link.get('href')
    new_page = requests.get(prefix + href)
    new_page_text = new_page.text
    soup2 = bs(new_page_text, 'html.parser')

    import requests
    from bs4 import BeautifulSoup

    # in 10er schritten pro seite
    z = 2410
    while z < 2460:

        url = 'https://www.hwk-konstanz.de/betriebe/suche-64,0,bdbsearch.html?limit=10&search-searchterm=&search-job=&search-filter-experience=&search-filter-radius=250&search-filter-jobnr=&search-filter-zipcode=*&offset=' + str(
            z)
        baseurl = "https://www.hwk-konstanz.de"

        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        for a in soup.select('a[href^="/betriebe/"]', limit=10):
            # print(a["href"])
            single_page = requests.get(baseurl + a["href"])
            soup_single_page = BeautifulSoup(single_page.content, "html.parser")
            name_branche = []
            for l, n_b in enumerate(soup_single_page.find_all("div", class_="col-md-12", limit=2)):
                name_branche.append((n_b.p, l))
            # print(name_branche)

            branche = "K/A"
            try:
                branche = name_branche[1][0].text
            except:
                pass

            # name, str, plz, ort, landkreis
            meta = []
            for m, i in enumerate(soup_single_page.find_all("div", class_="col-md-3")):
                meta.append((i.p, m))
            # print(str(meta[2][0]))

            # x = [name0, strasse1, plz + ort + landkreis]
            x = str(meta[2][0]).split("<br/>")

            name = x[0].replace("<p>", "")
            strasse = x[1]

            landkreis = "K/A"

            # x0 immer name, x1 immer str, x2 evtl landkreis drin oder durch <br> nur plz und ort
            try:
                if "Landkreis" in x[2]:
                    plz_ort_landkreis = x[2].split("Landkreis")
                    landkreis = plz_ort_landkreis[1].strip()
                    plz = plz_ort_landkreis[0][2:8].strip()
                    ort = plz_ort_landkreis[0][8:].strip()
                else:
                    plz = x[2][2:8].strip()
                    ort = x[2][8:].strip()
            except:
                pass


            # y0 tele, y1 branche
            email = "K/A"
            internet = "K/A"

            tele_handy_fax = str(meta[3][0]).split("<br/>")
            email_internet = meta[3][0]

            for e in meta[3][0].find_all("a", href=True):

                if "--at--" in e.text:
                    email = e.text.replace("--at--", "@")
                else:
                    internet = e.text


            tele = "K/A"
            handy = "K/A"
            fax = "K/A"

            for i in tele_handy_fax:
                if "Telefon" in i:
                    tele = i.replace("<p>", "").replace("Telefon ", "")
                elif "Handy" in i:
                    handy = i.replace("<p>", "").replace("Handy ", "")
                elif "Fax" in i:
                    fax = i.replace("<p>", "").replace("Fax ", "")
            # print(meta[2][0])
            # print(meta[3][0])
            # print(email)
            # print(internet)
            # print(tele)
            # print(handy)
            # print(fax)
            # print(name)
            # print(strasse)
            # print(landkreis)
            # print(plz)
            # print(ort)

            datensatz = {
                "firma_name": name,
                "firma_telefon": tele,
                "firma_handy": handy,
                "firma_fax": fax,
                "firma_strasse": strasse,
                "firma_plz": plz,
                "firma_ort": ort,
                "firma_landkres": landkreis,
                "firma_email": email,
                "firma_internet": internet,
                "firma_branche": branche,
            }

            print(datensatz)
            print('neuerDatensatz++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            insert_new_dataset_into_mdb(mdb_uri="192.168.100.5", datenbank='yanghi', collection='hwk_konstanz_neu',
                                        datensatz=datensatz)

        z += 10
        print('#####################################################################', z)