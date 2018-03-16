def speak(text):
    import win32com.client as wincl
    speak1 = wincl.Dispatch("SAPI.SpVoice")
    if int(text) > 5:
        speak1.speak("Bester Mann hat ")
        speak1.speak(text)
        speak1.speak("eingetragen. ")
    else:
        speak1.speak("Zu wenige... SO EINEN HALS!!!! ")



def suche():
    import pyautogui
    import datetime
    import time
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium import webdriver
    from pymongo import MongoClient
    chrome_options = Options()

    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)  # docker port anstatt lokal
    client = MongoClient("192.168.100.5", 27017, maxPoolSize=None)
    db2 = client['gemeinden']
    collection = db2['gemeinden']
    while True:
        cursor = collection.find({'telefon': {"$exists": False}, "zahl":"1"}, no_cursor_timeout=True, limit=1)
        a = collection.count({'telefon': {"$exists": False}, "zahl":"1"})
        print(a)
        for i in cursor:
            suchbegriff = i['Anschrift der Gemeinde']
            suchbegriff2 = i['Ort']
            suchbegriff3 = suchbegriff + " " + suchbegriff2 + " telefon"

            google_url = "https://www.google.de/search?q="
            google_url = google_url + suchbegriff3 + " impressum"
            driver.get(google_url)
            driver.switch_to.window(driver.window_handles[-1])
            print(suchbegriff, suchbegriff2)
            nummer = input("Bitte nummer eingeben\n\n")

            nummer = nummer.strip()
            if nummer:
                collection.update_many({'Anschrift der Gemeinde': i['Anschrift der Gemeinde'], 'Ort': i['Ort']}, {"$set": {'telefon': nummer}})
                ausgefuellt = a - collection.count({'telefon': {"$exists": False}})
                #	03 99 98 - 15 30speak(ausgefuellt)
                print(ausgefuellt, "Eingetragen.\n")
                print(collection.count({'telefon': {"$exists": False}}), "verbleibend.")

suche()