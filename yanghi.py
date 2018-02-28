import requests
from lxml import html
import time
import re

def scrapeit(link):
    r = requests.get(link)
    random_link = r.url
    page = requests.get(random_link)

    a = html.fromstring(page.content)
    #Erste Zeile der Firmen
    firmenname =  str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname = str(a.xpath('// *[@id="c68651"]/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname2 = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname3 = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[3]/div/div[1]/div[2]/div[1]/p//text()'))

    #Zweite Zeile der Firmen
    firmenname4 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname5 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname6 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[1]/p//text()'))

    #Dritte Zeile der Firmen
    firmenname7 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[1]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname8 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[2]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname9 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[3]/div/div[1]/div[2]/div[1]/p//text()'))

    #Vierte Zeile der Firmen
    firmenname10 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname11 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[2]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname12 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[3]/div/div[1]/div[2]/div[1]/p//text()'))

    #Fünfte Zeile der Firmen
    firmenname13 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[1]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname14 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname15 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[3]/div/div[1]/div[2]/div[1]/p//text()'))

    #Sechste Zeile der Firmen
    firmenname16 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[1]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname17 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[2]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname18 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[3]/div/div[1]/div[2]/div[1]/p//text()'))

    #Siebte Zeile der Firmen
    firmenname19 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[1]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname20 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[2]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname21 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[3]/div/div[1]/div[2]/div[1]/p//text()'))

    #Achte Zeile der Firmen
    firmenname22 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[1]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname23 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[2]/div/div[1]/div[2]/div[1]/p//text()'))
    firmenname24 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[3]/div/div[1]/div[2]/div[1]/p//text()'))


    #Erste Zeile Straßen
    strasse = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse2 = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse3 = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[3]/div/div[1]/div[2]/div[2]/p/text()[1]'))

    #Zweite Zeile Straßen
    strasse4 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse5 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse6 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[2]/p/text()[1]'))

    #Dritte Zeile Straßen
    strasse7 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[1]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse8 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[2]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse9 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[3]/div/div[1]/div[2]/div[2]/p/text()[1]'))

    #Vierte Zeile Straßen
    strasse10 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse11 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[2]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse12 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[3]/div/div[1]/div[2]/div[2]/p/text()[1]'))

    #Fünfte Zeile Straßen
    strasse13 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[1]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse14 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse15 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[3]/div/div[1]/div[2]/div[2]/p/text()[1]'))

    #Sechste Zeile Straßen
    strasse16 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[1]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse17 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[2]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse18 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[3]/div/div[1]/div[2]/div[2]/p/text()[1]'))

    #Siebte Zeile Straßen
    strasse19 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[1]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse20 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[2]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse21 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[3]/div/div[1]/div[2]/div[2]/p/text()[1]'))

    #Achte Zeile Straßen
    strasse22 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[1]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse23 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[2]/div/div[1]/div[2]/div[2]/p/text()[1]'))
    strasse24 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[3]/div/div[1]/div[2]/div[2]/p/text()[1]'))

    #Erste Zeile PLZ und Ort
    plz_ort  = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort2 = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort3 = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[3]/div/div[1]/div[2]/div[2]/p/text()[2]'))

    #Zweite Zeile PLZ und Ort
    plz_ort4 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort5 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort6 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[2]/p/text()[2]'))

    #Dritte Zeile PLZ und Ort
    plz_ort7 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[1]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort8 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[2]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort9 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[3]/div/div[1]/div[2]/div[2]/p/text()[2]'))

    #Vierte Zeile PLZ und Ort
    plz_ort10 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort11 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[2]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort12 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[3]/div/div[1]/div[2]/div[2]/p/text()[2]'))

    #Fünfte Zeile PLZ und Ort
    plz_ort13 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[1]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort14 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort15 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[3]/div/div[1]/div[2]/div[2]/p/text()[2]'))

    #Sechste Zeile PLZ und Ort
    plz_ort16 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[1]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort17 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[2]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort18 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[3]/div/div[1]/div[2]/div[2]/p/text()[2]'))

    #Siebte Zeile PLZ und Ort
    plz_ort19 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[1]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort20 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[2]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort21 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[3]/div/div[1]/div[2]/div[2]/p/text()[2]'))

    #Achte Zeile PLZ und Ort
    plz_ort22 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[1]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort23 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[2]/div/div[1]/div[2]/div[2]/p/text()[2]'))
    plz_ort24 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[3]/div/div[1]/div[2]/div[2]/p/text()[2]'))


    #Erste Zeile Telefon
    telefon = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon2 = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon3 = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[3]/div/div[1]/div[2]/div[3]/p/text()'))

    #Zweite Zeile Telefon
    telefon4 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon5 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon6 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[3]/p/text()'))

    #Dritte Zeile Telefon
    telefon7 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[1]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon8 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[2]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon9 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[3]/div/div[1]/div[2]/div[3]/p/text()'))

    #Vierte Zeile Telefon
    telefon10 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon11 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[2]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon12 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[3]/div/div[1]/div[2]/div[3]/p/text()'))

    #Fünfte Zeile Telefon
    telefon13 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[1]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon14 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon15 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[3]/div/div[1]/div[2]/div[3]/p/text()'))

    #Sechste Zeile Telefon
    telefon16 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[1]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon17 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[2]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon18 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[3]/div/div[1]/div[2]/div[3]/p/text()'))

    #Siebte Zeile Telefon
    telefon19 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[1]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon20 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[2]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon21 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[3]/div/div[1]/div[2]/div[3]/p/text()'))

    #Achte Zeile Telefon
    telefon22 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[1]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon23 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[2]/div/div[1]/div[2]/div[3]/p/text()'))
    telefon24 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[3]/div/div[1]/div[2]/div[3]/p/text()'))

    #Erste Zeile Faxnummer
    fax = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[4]/p/text()'))
    fax2 = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[4]/p/text()'))
    fax3 = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[3]/div/div[1]/div[2]/div[4]/p/text()'))

    #Zweite Zeile Faxnummer
    fax4 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[4]/p/text()'))
    fax5 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[4]/p/text()'))
    fax6 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[4]/p/text()'))

    #Dritte Zeile Faxnummer
    fax7 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[1]/div/div[1]/div[2]/div[4]/p/text()'))
    fax8 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[2]/div/div[1]/div[2]/div[4]/p/text()'))
    fax9 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[3]/div/div[1]/div[2]/div[4]/p/text()'))

    #Vierte Zeile Faxnummer
    fax10 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[4]/p/text()'))
    fax11 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[2]/div/div[1]/div[2]/div[4]/p/text()'))
    fax12 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[3]/div/div[1]/div[2]/div[4]/p/text()'))

    #Fünfte Zeile Faxnummer
    fax13 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[1]/div/div[1]/div[2]/div[4]/p/text()'))
    fax14 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[4]/p/text()'))
    fax15 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[3]/div/div[1]/div[2]/div[4]/p/text()'))

    #Sechste Zeile Faxnummer
    fax16 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[1]/div/div[1]/div[2]/div[4]/p/text()'))
    fax17 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[2]/div/div[1]/div[2]/div[4]/p/text()'))
    fax18 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[3]/div/div[1]/div[2]/div[4]/p/text()'))

    #Siebte Zeile Faxnummer
    fax19 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[1]/div/div[1]/div[2]/div[4]/p/text()'))
    fax20 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[2]/div/div[1]/div[2]/div[4]/p/text()'))
    fax21 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[3]/div/div[1]/div[2]/div[4]/p/text()'))

    #Achte Zeile Faxnummer
    fax22 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[1]/div/div[1]/div[2]/div[4]/p/text()'))
    fax23 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[2]/div/div[1]/div[2]/div[4]/p/text()'))
    fax24 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[3]/div/div[1]/div[2]/div[4]/p/text()'))

    #Erste Zeile Mail
    mail = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail2 = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail3 = str(a.xpath('//*[@id="c68651"]/div[3]/div[1]/div[3]/div/div[1]/div[2]/div[5]/p/a/text()'))

    #Zweite Zeile Mail
    mail4 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail5 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail6 = str(a.xpath('//*[@id="c68651"]/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[5]/p/a/text()'))

    #Dritte Zeile Mail
    mail7 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[1]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail8 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[2]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail9 = str(a.xpath('//*[@id="c68651"]/div[3]/div[3]/div[3]/div/div[1]/div[2]/div[5]/p/a/text()'))

    #Vierte Zeile Mail
    mail10 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail11 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[2]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail12 = str(a.xpath('//*[@id="c68651"]/div[3]/div[4]/div[3]/div/div[1]/div[2]/div[5]/p/a/text()'))

    #Fünfte Zeile Mail
    mail13 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[1]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail14 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail15 = str(a.xpath('//*[@id="c68651"]/div[3]/div[5]/div[3]/div/div[1]/div[2]/div[5]/p/a/text()'))

    #Sechste Zeile Mail
    mail16 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[1]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail17 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[2]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail18 = str(a.xpath('//*[@id="c68651"]/div[3]/div[6]/div[3]/div/div[1]/div[2]/div[5]/p/a/text()'))

    #Siebte Zeile Mail
    mail19 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[1]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail20 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[2]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail21 = str(a.xpath('//*[@id="c68651"]/div[3]/div[7]/div[3]/div/div[1]/div[2]/div[5]/p/a/text()'))

    #Achte Zeile Mail
    mail22 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[1]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail23 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[2]/div/div[1]/div[2]/div[5]/p/a/text()'))
    mail24 = str(a.xpath('//*[@id="c68651"]/div[3]/div[8]/div[3]/div/div[1]/div[2]/div[5]/p/a/text()'))

    firmenname = firmenname.replace('\\n', '')
    firmenname = firmenname.replace("['", '')
    firmenname = firmenname.replace("']", '')
    firmenname = firmenname.replace("', '", '')
    firmenname = firmenname.replace("  ", ' ')
    firmenname = firmenname.replace('            ', ' ')
    telefon = telefon.replace("\\n                        ']", '')
    telefon = telefon.replace("['\\n                            ", '')
    mail = mail.replace("['", '')
    mail = mail.replace("']", '')
    mail = mail.replace("(at)", '@')
    plz_ort = plz_ort.replace("['\\n                        ", '')
    plz_ort = plz_ort.replace("\\n                    ']", '')
    strasse = strasse.replace("['\\n                        ", '')
    strasse = strasse.replace("']", '')
    fax = fax.replace("['\\n                            ", '')
    fax = fax.replace("\\n                        ']", '')

    firmenname2 = firmenname2.replace('\\n', '')
    firmenname2 = firmenname2.replace("['", '')
    firmenname2 = firmenname2.replace("']", '')
    firmenname2 = firmenname2.replace("', '", '')
    firmenname2 = firmenname2.replace("  ", ' ')
    firmenname2 = firmenname2.replace('            ', ' ')
    telefon2 = telefon2.replace("\\n                        ']", '')
    telefon2 = telefon2.replace("['\\n                            ", '')
    mail2 = mail2.replace("['", '')
    mail2 = mail2.replace("']", '')
    mail2 = mail2.replace("(at)", '@')
    plz_ort2 = plz_ort2.replace("['\\n                        ", '')
    plz_ort2 = plz_ort2.replace("\\n                    ']", '')
    strasse2 = strasse2.replace("['\\n                        ", '')
    strasse2 = strasse2.replace("']", '')
    fax2 = fax2.replace("['\\n                            ", '')
    fax2 = fax2.replace("\\n                        ']", '')

    firmenname3 = firmenname3.replace('\\n', '')
    firmenname3 = firmenname3.replace("['", '')
    firmenname3 = firmenname3.replace("']", '')
    firmenname3 = firmenname3.replace("', '", '')
    firmenname3 = firmenname3.replace("  ", ' ')
    firmenname3 = firmenname3.replace('            ', ' ')
    telefon3 = telefon3.replace("\\n                        ']", '')
    telefon3 = telefon3.replace("['\\n                            ", '')
    mail3 = mail3.replace("['", '')
    mail3 = mail3.replace("']", '')
    mail3 = mail3.replace("(at)", '@')
    plz_ort3 = plz_ort3.replace("['\\n                        ", '')
    plz_ort3 = plz_ort3.replace("\\n                    ']", '')
    strasse3 = strasse3.replace("['\\n                        ", '')
    strasse3 = strasse3.replace("']", '')
    fax3 = fax3.replace("['\\n                            ", '')
    fax3 = fax3.replace("\\n                        ']", '')

    firmenname4 = firmenname4.replace('\\n', '')
    firmenname4 = firmenname4.replace("['", '')
    firmenname4 = firmenname4.replace("']", '')
    firmenname4 = firmenname4.replace("', '", '')
    firmenname4 = firmenname4.replace("  ", ' ')
    firmenname4 = firmenname4.replace('            ', ' ')
    telefon4 = telefon4.replace("\\n                        ']", '')
    telefon4 = telefon4.replace("['\\n                            ", '')
    mail4 = mail4.replace("['", '')
    mail4 = mail4.replace("']", '')
    mail4 = mail4.replace("(at)", '@')
    plz_ort4 = plz_ort4.replace("['\\n                        ", '')
    plz_ort4 = plz_ort4.replace("\\n                    ']", '')
    strasse4 = strasse4.replace("['\\n                        ", '')
    strasse4 = strasse4.replace("']", '')
    fax4 = fax4.replace("['\\n                            ", '')
    fax4 = fax4.replace("\\n                        ']", '')

    firmenname5 = firmenname5.replace('\\n', '')
    firmenname5 = firmenname5.replace("['", '')
    firmenname5 = firmenname5.replace("']", '')
    firmenname5 = firmenname5.replace("', '", '')
    firmenname5 = firmenname5.replace("  ", ' ')
    firmenname5 = firmenname5.replace('            ', ' ')
    telefon5 = telefon5.replace("\\n                        ']", '')
    telefon5 = telefon5.replace("['\\n                            ", '')
    mail5 = mail5.replace("['", '')
    mail5 = mail5.replace("']", '')
    mail5 = mail5.replace("(at)", '@')
    plz_ort5 = plz_ort5.replace("['\\n                        ", '')
    plz_ort5 = plz_ort5.replace("\\n                    ']", '')
    strasse5 = strasse5.replace("['\\n                        ", '')
    strasse5 = strasse5.replace("']", '')
    fax5 = fax5.replace("['\\n                            ", '')
    fax5 = fax5.replace("\\n                        ']", '')

    firmenname6 = firmenname6.replace('\\n', '')
    firmenname6 = firmenname6.replace("['", '')
    firmenname6 = firmenname6.replace("']", '')
    firmenname6 = firmenname6.replace("', '", '')
    firmenname6 = firmenname6.replace("  ", ' ')
    firmenname6 = firmenname6.replace('            ', ' ')
    telefon6 = telefon6.replace("\\n                        ']", '')
    telefon6 = telefon6.replace("['\\n                            ", '')
    mail6 = mail6.replace("['", '')
    mail6 = mail6.replace("']", '')
    mail6 = mail6.replace("(at)", '@')
    plz_ort6 = plz_ort6.replace("['\\n                        ", '')
    plz_ort6 = plz_ort6.replace("\\n                    ']", '')
    strasse6 = strasse6.replace("['\\n                        ", '')
    strasse6 = strasse6.replace("']", '')
    fax6 = fax6.replace("['\\n                            ", '')
    fax6 = fax6.replace("\\n                        ']", '')

    firmenname7 = firmenname7.replace('\\n', '')
    firmenname7 = firmenname7.replace("['", '')
    firmenname7 = firmenname7.replace("']", '')
    firmenname7 = firmenname7.replace("', '", '')
    firmenname7 = firmenname7.replace("  ", ' ')
    firmenname7 = firmenname7.replace('            ', ' ')
    telefon7 = telefon7.replace("\\n                        ']", '')
    telefon7 = telefon7.replace("['\\n                            ", '')
    mail7 = mail7.replace("['", '')
    mail7 = mail7.replace("']", '')
    mail7 = mail7.replace("(at)", '@')
    plz_ort7 = plz_ort7.replace("['\\n                        ", '')
    plz_ort7 = plz_ort7.replace("\\n                    ']", '')
    strasse7 = strasse7.replace("['\\n                        ", '')
    strasse7 = strasse7.replace("']", '')
    fax7 = fax7.replace("['\\n                            ", '')
    fax7 = fax7.replace("\\n                        ']", '')

    firmenname8 = firmenname8.replace('\\n', '')
    firmenname8 = firmenname8.replace("['", '')
    firmenname8 = firmenname8.replace("']", '')
    firmenname8 = firmenname8.replace("', '", '')
    firmenname8 = firmenname8.replace("  ", ' ')
    firmenname8 = firmenname8.replace('            ', ' ')
    telefon8 = telefon8.replace("\\n                        ']", '')
    telefon8 = telefon8.replace("['\\n                            ", '')
    mail8 = mail8.replace("['", '')
    mail8 = mail8.replace("']", '')
    mail8 = mail8.replace("(at)", '@')
    plz_ort8 = plz_ort8.replace("['\\n                        ", '')
    plz_ort8 = plz_ort8.replace("\\n                    ']", '')
    strasse8 = strasse8.replace("['\\n                        ", '')
    strasse8 = strasse8.replace("']", '')
    fax8 = fax8.replace("['\\n                            ", '')
    fax8 = fax8.replace("\\n                        ']", '')

    firmenname9 = firmenname9.replace('\\n', '')
    firmenname9 = firmenname9.replace("['", '')
    firmenname9 = firmenname9.replace("']", '')
    firmenname9 = firmenname9.replace("', '", '')
    firmenname9 = firmenname9.replace("  ", ' ')
    firmenname9 = firmenname9.replace('            ', ' ')
    telefon9 = telefon9.replace("\\n                        ']", '')
    telefon9 = telefon9.replace("['\\n                            ", '')
    mail9 = mail9.replace("['", '')
    mail9 = mail9.replace("']", '')
    mail9 = mail9.replace("(at)", '@')
    plz_ort9 = plz_ort9.replace("['\\n                        ", '')
    plz_ort9 = plz_ort9.replace("\\n                    ']", '')
    strasse9 = strasse9.replace("['\\n                        ", '')
    strasse9 = strasse9.replace("']", '')
    fax9 = fax9.replace("['\\n                            ", '')
    fax9 = fax9.replace("\\n                        ']", '')

    firmenname10 = firmenname10.replace('\\n', '')
    firmenname10 = firmenname10.replace("['", '')
    firmenname10 = firmenname10.replace("']", '')
    firmenname10 = firmenname10.replace("', '", '')
    firmenname10 = firmenname10.replace("  ", ' ')
    firmenname10 = firmenname10.replace('            ', ' ')
    telefon10 = telefon10.replace("\\n                        ']", '')
    telefon10 = telefon10.replace("['\\n                            ", '')
    mail10 = mail10.replace("['", '')
    mail10 = mail10.replace("']", '')
    mail10 = mail10.replace("(at)", '@')
    plz_ort10 = plz_ort10.replace("['\\n                        ", '')
    plz_ort10 = plz_ort10.replace("\\n                    ']", '')
    strasse10 = strasse10.replace("['\\n                        ", '')
    strasse10 = strasse10.replace("']", '')
    fax10 = fax10.replace("['\\n                            ", '')
    fax10 = fax10.replace("\\n                        ']", '')

    firmenname11 = firmenname11.replace('\\n', '')
    firmenname11 = firmenname11.replace("['", '')
    firmenname11 = firmenname11.replace("']", '')
    firmenname11 = firmenname11.replace("', '", '')
    firmenname11 = firmenname11.replace("  ", ' ')
    firmenname11 = firmenname11.replace('            ', ' ')
    telefon11 = telefon11.replace("\\n                        ']", '')
    telefon11 = telefon11.replace("['\\n                            ", '')
    mail11 = mail11.replace("['", '')
    mail11 = mail11.replace("']", '')
    mail11 = mail11.replace("(at)", '@')
    plz_ort11 = plz_ort11.replace("['\\n                        ", '')
    plz_ort11 = plz_ort11.replace("\\n                    ']", '')
    strasse11 = strasse11.replace("['\\n                        ", '')
    strasse11 = strasse11.replace("']", '')
    fax11 = fax11.replace("['\\n                            ", '')
    fax11 = fax11.replace("\\n                        ']", '')

    firmenname12 = firmenname12.replace('\\n', '')
    firmenname12 = firmenname12.replace("['", '')
    firmenname12 = firmenname12.replace("']", '')
    firmenname12 = firmenname12.replace("', '", '')
    firmenname12 = firmenname12.replace("  ", ' ')
    firmenname12 = firmenname12.replace('            ', ' ')
    telefon12 = telefon12.replace("\\n                        ']", '')
    telefon12 = telefon12.replace("['\\n                            ", '')
    mail12 = mail12.replace("['", '')
    mail12 = mail12.replace("']", '')
    mail12 = mail12.replace("(at)", '@')
    plz_ort12 = plz_ort12.replace("['\\n                        ", '')
    plz_ort12 = plz_ort12.replace("\\n                    ']", '')
    strasse12 = strasse12.replace("['\\n                        ", '')
    strasse12 = strasse12.replace("']", '')
    fax12 = fax12.replace("['\\n                            ", '')
    fax12 = fax12.replace("\\n                        ']", '')

    firmenname13 = firmenname13.replace('\\n', '')
    firmenname13 = firmenname13.replace("['", '')
    firmenname13 = firmenname13.replace("']", '')
    firmenname13 = firmenname13.replace("', '", '')
    firmenname13 = firmenname13.replace("  ", ' ')
    firmenname13 = firmenname13.replace('            ', ' ')
    telefon13 = telefon13.replace("\\n                        ']", '')
    telefon13 = telefon13.replace("['\\n                            ", '')
    mail13 = mail13.replace("['", '')
    mail13 = mail13.replace("']", '')
    mail13 = mail13.replace("(at)", '@')
    plz_ort13 = plz_ort13.replace("['\\n                        ", '')
    plz_ort13 = plz_ort13.replace("\\n                    ']", '')
    strasse13 = strasse13.replace("['\\n                        ", '')
    strasse13 = strasse13.replace("']", '')
    fax13 = fax13.replace("['\\n                            ", '')
    fax13 = fax13.replace("\\n                        ']", '')

    firmenname14 = firmenname14.replace('\\n', '')
    firmenname14 = firmenname14.replace("['", '')
    firmenname14 = firmenname14.replace("']", '')
    firmenname14 = firmenname14.replace("', '", '')
    firmenname14 = firmenname14.replace("  ", ' ')
    firmenname14 = firmenname14.replace('            ', ' ')
    telefon14 = telefon14.replace("\\n                        ']", '')
    telefon14 = telefon14.replace("['\\n                            ", '')
    mail14 = mail14.replace("['", '')
    mail14 = mail14.replace("']", '')
    mail14 = mail14.replace("(at)", '@')
    plz_ort14 = plz_ort14.replace("['\\n                        ", '')
    plz_ort14 = plz_ort14.replace("\\n                    ']", '')
    strasse14 = strasse14.replace("['\\n                        ", '')
    strasse14 = strasse14.replace("']", '')
    fax14 = fax14.replace("['\\n                            ", '')
    fax14 = fax14.replace("\\n                        ']", '')

    firmenname15 = firmenname15.replace('\\n', '')
    firmenname15 = firmenname15.replace("['", '')
    firmenname15 = firmenname15.replace("']", '')
    firmenname15 = firmenname15.replace("', '", '')
    firmenname15 = firmenname15.replace("  ", ' ')
    firmenname15 = firmenname15.replace('            ', ' ')
    telefon15 = telefon15.replace("\\n                        ']", '')
    telefon15 = telefon15.replace("['\\n                            ", '')
    mail15 = mail15.replace("['", '')
    mail15 = mail15.replace("']", '')
    mail15 = mail15.replace("(at)", '@')
    plz_ort15 = plz_ort15.replace("['\\n                        ", '')
    plz_ort15 = plz_ort15.replace("\\n                    ']", '')
    strasse15 = strasse15.replace("['\\n                        ", '')
    strasse15 = strasse15.replace("']", '')
    fax15 = fax15.replace("['\\n                            ", '')
    fax15 = fax15.replace("\\n                        ']", '')

    firmenname16 = firmenname16.replace('\\n', '')
    firmenname16 = firmenname16.replace("['", '')
    firmenname16 = firmenname16.replace("']", '')
    firmenname16 = firmenname16.replace("', '", '')
    firmenname16 = firmenname16.replace("  ", ' ')
    firmenname16 = firmenname16.replace('            ', ' ')
    telefon16 = telefon16.replace("\\n                        ']", '')
    telefon16 = telefon16.replace("['\\n                            ", '')
    mail16 = mail16.replace("['", '')
    mail16 = mail16.replace("']", '')
    mail16 = mail16.replace("(at)", '@')
    plz_ort16 = plz_ort16.replace("['\\n                        ", '')
    plz_ort16 = plz_ort16.replace("\\n                    ']", '')
    strasse16 = strasse16.replace("['\\n                        ", '')
    strasse16 = strasse16.replace("']", '')
    fax16 = fax16.replace("['\\n                            ", '')
    fax16 = fax16.replace("\\n                        ']", '')

    firmenname17 = firmenname17.replace('\\n', '')
    firmenname17 = firmenname17.replace("['", '')
    firmenname17 = firmenname17.replace("']", '')
    firmenname17 = firmenname17.replace("', '", '')
    firmenname17 = firmenname17.replace("  ", ' ')
    firmenname17 = firmenname17.replace('            ', ' ')
    telefon17 = telefon17.replace("\\n                        ']", '')
    telefon17 = telefon17.replace("['\\n                            ", '')
    mail17 = mail17.replace("['", '')
    mail17 = mail17.replace("']", '')
    mail17 = mail17.replace("(at)", '@')
    plz_ort17 = plz_ort17.replace("['\\n                        ", '')
    plz_ort17 = plz_ort17.replace("\\n                    ']", '')
    strasse17 = strasse17.replace("['\\n                        ", '')
    strasse17 = strasse17.replace("']", '')
    fax17 = fax17.replace("['\\n                            ", '')
    fax17 = fax17.replace("\\n                        ']", '')

    firmenname18 = firmenname18.replace('\\n', '')
    firmenname18 = firmenname18.replace("['", '')
    firmenname18 = firmenname18.replace("']", '')
    firmenname18 = firmenname18.replace("', '", '')
    firmenname18 = firmenname18.replace("  ", ' ')
    firmenname18 = firmenname18.replace('            ', ' ')
    telefon18 = telefon18.replace("\\n                        ']", '')
    telefon18 = telefon18.replace("['\\n                            ", '')
    mail18 = mail18.replace("['", '')
    mail18 = mail18.replace("']", '')
    mail18 = mail18.replace("(at)", '@')
    plz_ort18 = plz_ort18.replace("['\\n                        ", '')
    plz_ort18 = plz_ort18.replace("\\n                    ']", '')
    strasse18 = strasse18.replace("['\\n                        ", '')
    strasse18 = strasse18.replace("']", '')
    fax18 = fax18.replace("['\\n                            ", '')
    fax18 = fax18.replace("\\n                        ']", '')

    firmenname19 = firmenname19.replace('\\n', '')
    firmenname19 = firmenname19.replace("['", '')
    firmenname19 = firmenname19.replace("']", '')
    firmenname19 = firmenname19.replace("', '", '')
    firmenname19 = firmenname19.replace("  ", ' ')
    firmenname19 = firmenname19.replace('            ', ' ')
    telefon19 = telefon19.replace("\\n                        ']", '')
    telefon19 = telefon19.replace("['\\n                            ", '')
    mail19 = mail19.replace("['", '')
    mail19 = mail19.replace("']", '')
    mail19 = mail19.replace("(at)", '@')
    plz_ort19 = plz_ort19.replace("['\\n                        ", '')
    plz_ort19 = plz_ort19.replace("\\n                    ']", '')
    strasse19 = strasse19.replace("['\\n                        ", '')
    strasse19 = strasse19.replace("']", '')
    fax19 = fax19.replace("['\\n                            ", '')
    fax19 = fax19.replace("\\n                        ']", '')

    firmenname20 = firmenname20.replace('\\n', '')
    firmenname20 = firmenname20.replace("['", '')
    firmenname20 = firmenname20.replace("']", '')
    firmenname20 = firmenname20.replace("', '", '')
    firmenname20 = firmenname20.replace("  ", ' ')
    firmenname20 = firmenname20.replace('            ', ' ')
    telefon20 = telefon20.replace("\\n                        ']", '')
    telefon20 = telefon20.replace("['\\n                            ", '')
    mail20 = mail20.replace("['", '')
    mail20 = mail20.replace("']", '')
    mail20 = mail20.replace("(at)", '@')
    plz_ort20 = plz_ort20.replace("['\\n                        ", '')
    plz_ort20 = plz_ort20.replace("\\n                    ']", '')
    strasse20 = strasse20.replace("['\\n                        ", '')
    strasse20 = strasse20.replace("']", '')
    fax20 = fax20.replace("['\\n                            ", '')
    fax20 = fax20.replace("\\n                        ']", '')

    firmenname21 = firmenname21.replace('\\n', '')
    firmenname21 = firmenname21.replace("['", '')
    firmenname21 = firmenname21.replace("']", '')
    firmenname21 = firmenname21.replace("', '", '')
    firmenname21 = firmenname21.replace("  ", ' ')
    firmenname21 = firmenname21.replace('            ', ' ')
    telefon21 = telefon21.replace("\\n                        ']", '')
    telefon21 = telefon21.replace("['\\n                            ", '')
    mail21 = mail21.replace("['", '')
    mail21 = mail21.replace("']", '')
    mail21 = mail21.replace("(at)", '@')
    plz_ort21 = plz_ort21.replace("['\\n                        ", '')
    plz_ort21 = plz_ort21.replace("\\n                    ']", '')
    strasse21 = strasse21.replace("['\\n                        ", '')
    strasse21 = strasse21.replace("']", '')
    fax21 = fax21.replace("['\\n                            ", '')
    fax21 = fax21.replace("\\n                        ']", '')

    firmenname22 = firmenname22.replace('\\n', '')
    firmenname22 = firmenname22.replace("['", '')
    firmenname22 = firmenname22.replace("']", '')
    firmenname22 = firmenname22.replace("', '", '')
    firmenname22 = firmenname22.replace("  ", ' ')
    firmenname22 = firmenname22.replace('            ', ' ')
    telefon22 = telefon22.replace("\\n                        ']", '')
    telefon22 = telefon22.replace("['\\n                            ", '')
    mail22 = mail22.replace("['", '')
    mail22 = mail22.replace("']", '')
    mail22 = mail22.replace("(at)", '@')
    plz_ort22 = plz_ort22.replace("['\\n                        ", '')
    plz_ort22 = plz_ort22.replace("\\n                    ']", '')
    strasse22 = strasse22.replace("['\\n                        ", '')
    strasse22 = strasse22.replace("']", '')
    fax22 = fax22.replace("['\\n                            ", '')
    fax22 = fax22.replace("\\n                        ']", '')

    firmenname23 = firmenname23.replace('\\n', '')
    firmenname23 = firmenname23.replace("['", '')
    firmenname23 = firmenname23.replace("']", '')
    firmenname23 = firmenname23.replace("', '", '')
    firmenname23 = firmenname23.replace("  ", ' ')
    firmenname23 = firmenname23.replace('            ', ' ')
    telefon23 = telefon23.replace("\\n                        ']", '')
    telefon23 = telefon23.replace("['\\n                            ", '')
    mail23 = mail23.replace("['", '')
    mail23 = mail23.replace("']", '')
    mail23 = mail23.replace("(at)", '@')
    plz_ort23 = plz_ort23.replace("['\\n                        ", '')
    plz_ort23 = plz_ort23.replace("\\n                    ']", '')
    strasse23 = strasse23.replace("['\\n                        ", '')
    strasse23 = strasse23.replace("']", '')
    fax23 = fax23.replace("['\\n                            ", '')
    fax23 = fax23.replace("\\n                        ']", '')

    firmenname24 = firmenname24.replace('\\n', '')
    firmenname24 = firmenname24.replace("['", '')
    firmenname24 = firmenname24.replace("']", '')
    firmenname24 = firmenname24.replace("', '", '')
    firmenname24 = firmenname24.replace("  ", ' ')
    firmenname24 = firmenname24.replace('            ', ' ')
    telefon24 = telefon24.replace("\\n                        ']", '')
    telefon24 = telefon24.replace("['\\n                            ", '')
    mail24 = mail24.replace("['", '')
    mail24 = mail24.replace("']", '')
    mail24 = mail24.replace("(at)", '@')
    plz_ort24 = plz_ort24.replace("['\\n                        ", '')
    plz_ort24 = plz_ort24.replace("\\n                    ']", '')
    strasse24 = strasse24.replace("['\\n                        ", '')
    strasse24 = strasse24.replace("']", '')
    fax24 = fax24.replace("['\\n                            ", '')
    fax24 = fax24.replace("\\n                        ']", '')



    firma = {"firmenname": firmenname,
              "strasse" : strasse,
              "plz_und_ort" : plz_ort,
              "telefon": telefon,
              "fax":fax,
              "mail" :mail}

    firma2 = {"firmenname": firmenname2,
              "strasse" : strasse2,
              "plz_und_ort" : plz_ort2,
              "telefon": telefon2,
              "fax":fax2,
              "mail" :mail2}

    firma3 = {"firmenname": firmenname3,
              "strasse" : strasse3,
              "plz_und_ort" : plz_ort3,
              "telefon": telefon3,
              "fax":fax3,
              "mail" :mail3}

    firma4 = {"firmenname": firmenname4,
              "strasse" : strasse4,
              "plz_und_ort" : plz_ort4,
              "telefon": telefon4,
              "fax":fax4,
              "mail" :mail4}

    firma5 = {"firmenname": firmenname5,
              "strasse" : strasse5,
              "plz_und_ort" : plz_ort5,
              "telefon": telefon5,
              "fax":fax5,
              "mail" :mail5}

    firma6 = {"firmenname": firmenname6,
              "strasse" : strasse6,
              "plz_und_ort" : plz_ort6,
              "telefon": telefon6,
              "fax":fax6,
              "mail" :mail6}

    firma7 = {"firmenname": firmenname7,
              "strasse" : strasse7,
              "plz_und_ort" : plz_ort7,
              "telefon": telefon7,
              "fax":fax7,
              "mail" :mail7}

    firma8 = {"firmenname": firmenname8,
              "strasse" : strasse8,
              "plz_und_ort" : plz_ort8,
              "telefon": telefon8,
              "fax":fax8,
              "mail" :mail8}

    firma9 = {"firmenname": firmenname9,
              "strasse" : strasse9,
              "plz_und_ort" : plz_ort9,
              "telefon": telefon9,
              "fax":fax9,
              "mail" :mail9}

    firma10 = {"firmenname": firmenname10,
              "strasse" : strasse10,
              "plz_und_ort" : plz_ort10,
              "telefon": telefon10,
              "fax":fax10,
              "mail" :mail10}

    firma11 = {"firmenname": firmenname11,
              "strasse" : strasse11,
              "plz_und_ort" : plz_ort11,
              "telefon": telefon11,
              "fax":fax11,
              "mail" :mail11}

    firma12 = {"firmenname": firmenname12,
              "strasse" : strasse12,
              "plz_und_ort" : plz_ort12,
              "telefon": telefon12,
              "fax":fax12,
              "mail" :mail12}

    firma13 = {"firmenname": firmenname13,
              "strasse" : strasse13,
              "plz_und_ort" : plz_ort13,
              "telefon": telefon13,
              "fax":fax13,
              "mail" :mail13}

    firma14 = {"firmenname": firmenname14,
              "strasse" : strasse14,
              "plz_und_ort" : plz_ort14,
              "telefon": telefon14,
              "fax":fax14,
              "mail" :mail14}

    firma15 = {"firmenname": firmenname15,
              "strasse" : strasse15,
              "plz_und_ort" : plz_ort15,
              "telefon": telefon15,
              "fax":fax15,
              "mail" :mail15}

    firma16 = {"firmenname": firmenname16,
              "strasse" : strasse16,
              "plz_und_ort" : plz_ort16,
              "telefon": telefon16,
              "fax":fax16,
              "mail" :mail16}

    firma17 = {"firmenname": firmenname17,
              "strasse" : strasse17,
              "plz_und_ort" : plz_ort17,
              "telefon": telefon17,
              "fax":fax17,
              "mail" :mail17}

    firma18 = {"firmenname": firmenname18,
              "strasse" : strasse18,
              "plz_und_ort" : plz_ort18,
              "telefon": telefon18,
              "fax":fax18,
              "mail" :mail18}

    firma19 = {"firmenname": firmenname19,
              "strasse" : strasse19,
              "plz_und_ort" : plz_ort19,
              "telefon": telefon19,
              "fax":fax19,
              "mail" :mail19}

    firma20 = {"firmenname": firmenname20,
              "strasse" : strasse20,
              "plz_und_ort" : plz_ort20,
              "telefon": telefon20,
              "fax":fax20,
              "mail" :mail20}

    firma21 = {"firmenname": firmenname21,
              "strasse" : strasse21,
              "plz_und_ort" : plz_ort21,
              "telefon": telefon21,
              "fax":fax21,
              "mail" :mail21}

    firma22 = {"firmenname": firmenname22,
              "strasse" : strasse22,
              "plz_und_ort" : plz_ort22,
              "telefon": telefon22,
              "fax":fax22,
              "mail" :mail22}

    firma23 = {"firmenname": firmenname23,
              "strasse" : strasse23,
              "plz_und_ort" : plz_ort23,
              "telefon": telefon23,
              "fax":fax23,
              "mail" :mail23}

    firma24 = {"firmenname": firmenname24,
              "strasse" : strasse24,
              "plz_und_ort" : plz_ort24,
              "telefon": telefon24,
              "fax":fax24,
              "mail" :mail24}

    #print(firma)
    #print(firma2)
    #print(firma3)
    #print(firma4)
    #print(firma5)
    #print(firma6)
    #print(firma7)
    #print(firma8)
    #print(firma9)
    #print(firma10)
    #print(firma11)
    #print(firma12)
    #print(firma13)
    #print(firma14)
    #print(firma15)
    #print(firma16)
    #print(firma17)
    #print(firma18)
    #print(firma19)
    #print(firma20)
    #print(firma21)
    #print(firma22)
    #print(firma23)
    #print(firma24)

    from pymongo import MongoClient
    mz_token = 'http://192.168.100.5:8080/search.php'
    client = MongoClient("192.168.100.5", 27017, maxPoolSize=50)
    db = client.mz  # mz durch die entsprechende Datenbank ersetzen
    collection = db['scraped_complete_januar']  # db durch entsprechende DB ersetzen
    collection.insert_one(firma)
    collection.insert_one(firma2)
    collection.insert_one(firma3)
    collection.insert_one(firma4)
    collection.insert_one(firma5)
    collection.insert_one(firma6)
    collection.insert_one(firma7)
    collection.insert_one(firma8)
    collection.insert_one(firma9)
    collection.insert_one(firma10)
    collection.insert_one(firma11)
    collection.insert_one(firma12)
    collection.insert_one(firma13)
    collection.insert_one(firma14)
    collection.insert_one(firma15)
    collection.insert_one(firma16)
    collection.insert_one(firma17)
    collection.insert_one(firma18)
    collection.insert_one(firma19)
    collection.insert_one(firma20)
    collection.insert_one(firma21)
    collection.insert_one(firma22)
    collection.insert_one(firma23)
    collection.insert_one(firma24)
    print(firma)

grundlink = "http://localhost/zveh/fachbetriebssuche"
suffix = 1
endung = ".html"

while suffix < 7838:
    gesamtlink = grundlink + str(suffix) + endung
    # Hier code
    scrapeit(gesamtlink)
    print(gesamtlink)
    suffix = suffix + 1
print("Done")