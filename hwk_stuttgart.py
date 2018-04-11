from bs4 import BeautifulSoup
import requests
import time


def insert_new_dataset_into_mdb(mdb_uri, datenbank, collection, datensatz):
    from pymongo import MongoClient
    client = MongoClient(mdb_uri, 27017, maxPoolSize=500)
    db = client[datenbank]
    collection = db[collection]
    collection.insert_one(datensatz)




z = 0
y = 0
maxSeiten = 1398
while y < maxSeiten:

    mainLink = 'https://www.hwk-stuttgart.de/betriebe/suche-67,0,bdbsearch.html?limit=10&search-searchterm=&search-job=&search-filter-jobnr=&search-filter-zipcode=bayern&search-filter-radius=20&offset=' + str(z)
    page = requests.get(mainLink)
    prefix = 'https://www.hwk-stuttgart.de'

    clean_text = page.text
    soup = BeautifulSoup(clean_text, 'html.parser')

    for link in soup.select('a[href^=/betriebe/]')[:10]:
        href = link.get('href')
        newPage = requests.get(prefix + href)
        single_page_text = newPage.text
        soup2 = BeautifulSoup(single_page_text, 'html.parser')

        name = 'K/A'
        strasse = 'K/A'
        plz ='K/A'
        homepage = 'K/A'
        mail = 'K/A'
        Landkreis = 'K/A'
        Tele = 'K/A'
        Fax = 'K/A'
        ort = 'K/A'
        Handy = 'K/A'
        Fax = 'K/A'
        branche = 'K/A'

        for firma in soup2('h1'):
            name = firma.text
            name = name.replace('\n', '')
            name = name.replace('\t', '')
            print(name.strip())
        for meta in soup2('section', limit=1):

            print('meta',meta)

            # metaNaked = meta.text.split(' ')
            # print(metaNaked)


            # strasse ist immer vorhanden in metaNaked => teil vor D-
            metaNaked = meta.text

            # print('metaNaked', metaNaked)
            strasse = metaNaked.split('D-')[0]



            # plz auch immer vorhanden =>  teil nach D-
            # abStrasse = metaNaked.split('D-')[1]
            # print(abStrasse)
            # abStrasse = abStrasse.split(' ')
            # plz = abStrasse[0]

            # print(strasse)
            # print(plz)


            # branche, email als einzelne loops
            for branchen in meta('p'):
                branche = branchen.text
                # print(branchen.text)

            mail = 'K/A'
            homepage = 'K/A'
            for a in meta('a'):
                # print(a.text)
                if 'www.' in a.text:
                    homepage = a.text
                    # print(homepage)
                if '--at--' in a.text:
                    mail = a.text
                    mail = mail.replace('--at--','@')
                    # print(mail)


            # elements were mixing z.b. 32412handy 23424fax => split/join -> one string and split by tele/handy/fax
            # take right side of split and run for loop x.isdigit() and append, until is false -> break
            for address in soup2('address'):
                #optimierungspoti => guckt beide address elemente durch, eins reicht
                #kann strasse,ort,plz, landkreis und tele,handy,fax einzelnt

                # print('address',address)
                address = address.text.split(' ')
                # print(address)
                address = ''.join(address)
                # print(address)

                #strasse, ORT, plz, landkreis
                if 'D-' in address:
                    address = address.split('D-')
                    # print('address',address[1])
                    #wechsel restarray
                    address = address[1]
                    # print('address[1]', address)
                    plz = address[0:5]
                    # print(plz)


                    # restarray ohne plz
                    addressCut = address[5:]
                    # print(addressCut)
                    if 'Landkreis' in addressCut:
                        addressCut = addressCut.split('Landkreis')
                        ort = addressCut[0]
                        Landkreis = addressCut[1]
                        # print(Landkreis)
                        print('landkreis true', ort)
                    else:
                        ort = addressCut
                        print('landkreis false', ort)

                Tele = []
                if 'Telefon' in address:
                    address = address.split('Telefon')
                    address = address[1].replace('-', '')
                    # print('tele', address)
                    for i in address:
                        if i.isdigit():

                            tele = Tele.append(i)
                        else:
                            break
                    Tele = ''.join(Tele)
                    # print(Tele)

                else:
                    Tele = 'K/A'
                    # print(Tele)
                Handy = []
                if 'Handy' in address:
                    address = address.split('Handy')
                    address = address[1]
                    for j in address:
                        if j.isdigit():
                            handy = Handy.append(j)
                        else:
                            break
                    Handy = ''.join(Handy)
                    # print(Handy)
                else:
                    Handy = 'K/A'
                    # print(Handy)
                Fax = []
                if 'Fax' in address:
                    address = address.split('Fax')
                    address = address[1]
                    for k in address:
                        if k.isdigit():
                            fax = Fax.append(k)
                        else:
                            break
                    Fax = ''.join(Fax)
                    # print(Fax)
                else:
                    Fax = 'K/A'

                    # print(Fax)

            datensatz = {
                'firma_name': name,
                'firma_strasse': strasse,
                "firma_plz": plz,
                "firma_ort": ort,
                "firma_telefon": Tele,
                "firma_handy": Handy,
                "firma_fax": Fax,
                "firma_mail": mail,
                "firma_homepage": homepage,
                "firma_branche": branche
            }
            print(datensatz)
            print('neuerDatensatz++++++++++++++++++++++++++++++++++++++++++++++++++++++++++', y)
            insert_new_dataset_into_mdb(mdb_uri="192.168.100.5", datenbank='yanghi', collection='hwk_stuttgart', datensatz=datensatz)
    z  = z + 10
    print(z)
    y += 1
    print('##################################################################', y)
