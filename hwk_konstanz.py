from bs4 import BeautifulSoup
import requests
# from selenium import webdiver

# driver = driver.Chrome('chromedriver.exe')
# driver.get('')

def insert_new_dataset_into_mdb(mdb_uri, datenbank, collection, datensatz):
    from pymongo import MongoClient
    client = MongoClient(mdb_uri, 27017, maxPoolSize=500)
    db = client[datenbank]
    collection = db[collection]
    collection.insert_one(datensatz)



z = 1420
y = 142
maxSeiten = 4000
while y < maxSeiten:

    mainlink = 'https://www.hwk-konstanz.de/betriebe/suche-64,0,bdbsearch.html?limit=10&search-searchterm=&search-job=&search-filter-jobnr=&search-filter-zipcode=bayern&search-filter-experience=&search-filter-radius=250&offset=' + str(z)
    page = requests.get(mainlink)
    prefix = 'https://www.hwk-konstanz.de'

    clean_text = page.text
    soup = BeautifulSoup(clean_text,'html.parser')

    # print(soup.prettify())

    for link in soup.select('a[href^=/betriebe/]')[:10]:
        # print(link)
        href = link.get('href')
        # print(href)
        newPage = requests.get(prefix + href)
        # print(newPage)
        single_page_text = newPage.text
        # print(single_page_text)
        # print('################################################################')
        soup2 = BeautifulSoup(single_page_text, 'html.parser')

        for firma in soup2('h1'):
            name = 'K/A'

            name = firma.text
            # name = name.replace('\n', '')
            # name = name.replace('\t', '')
            name = name.strip()
            # print(name)

        for section in soup2('section', limit=1):

            strasse = 'K/A'
            plz = 'K/A'
            ort = 'K/A'
            tele = 'K/A'
            handy = 'K/A'
            fax = 'K/A'
            mail = 'K/A'
            homepage = 'K/A'


            print(section.text)
            section = section.text

            if 'D-' in section:
                # token ist ganzer addressen string
                string_strasse = section.split('D-')
                strasse = string_strasse[0]
                # print(strasse)

                string_plz = string_strasse[1]
                plz_token = string_plz.split(' ')
                plz = plz_token[0]
                # print(plz)

                ort_array = plz_token[1:]
                ort_string = ' '.join(ort_array)
                if 'Landkreis' in ort_string:
                    ort_token = ort_string.split('Landkreis')
                    ort = ort_token[0]
                    # print(ort)

                    tele_string = ort_token[1].split(' ')
                    tele_string = ''.join(tele_string)
                    # print(tele_string)

                    Tele = []
                    if 'Telefon' in tele_string:
                        tele_token = tele_string.split('Telefon')
                        tele_string = tele_token[1].replace('-', '')

                        for i in tele_string:
                            if i.isdigit():
                                tele = Tele.append(i)
                            else:
                                break
                        tele = ''.join(Tele)
                        # print(tele)

                    Handy = []
                    if 'Handy' in tele_string:
                        handy_token = tele_string.split('Handy')
                        handy_string = handy_token[1].replace('-', '')
                        for j in handy_string:
                            if j.isdigit():
                                handy = Handy.append(j)
                            else:
                                break
                        handy = ''.join(Handy)
                        # print(handy)

                    Fax = []
                    if 'Fax' in tele_string:
                        fax_token = tele_string.split('Fax')
                        fax_string = fax_token[1].replace('-', '')
                        for k in fax_string:
                            if k.isdigit():
                                fax = Fax.append(k)
                            else:
                                break
                        fax = ''.join(Fax)
                        # print(fax)


        for section in soup2.find_all('section'):
            for a in section.find_all('a'):

                # print(a)
                # print(section.text)
                if 'www.' in a.text:
                    homepage = a.text
                    # print(homepage, 'homepage')
                if '--at--' in a.text:
                    mail = a.text
                    mail = mail.replace('--at--', '@')
                    # print(mail, 'mail')

            datensatz = {
                'firma_name': name,
                'firma_strasse': strasse,
                "firma_plz": plz,
                "firma_ort": ort,
                "firma_telefon": tele,
                "firma_handy": handy,
                "firma_fax": fax,
                "firma_mail": mail,
                "firma_homepage": homepage,
            }
        print(datensatz)
        print('neuerDatensatz++++++++++++++++++++++++++++++++++++++++++++++++++++++++++', y)
        insert_new_dataset_into_mdb(mdb_uri="192.168.100.5", datenbank='yanghi', collection='hwk_konstanz',
                                    datensatz=datensatz)
    z = z + 10
    print(z)
    y += 1
    print('neueSeite##############################################################################################')








