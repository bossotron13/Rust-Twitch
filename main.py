from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from threading import Thread
import time
from API import API

PATH = r"driver/msedgedriver.exe"

webdriver.FirefoxProfile()
options = EdgeOptions()
options.use_chromium = True
options.add_argument("headless")
options.add_argument("mute-audio")
driver = webdriver.Chrome(executable_path=PATH, options=options)
API = API(driver)

while True:
    for x in API.StreamerList:
        if API.StreamerList[x] < 2:
            if API.gotoStreamer(x):
                if API.CreateTimer(x):
                    if API.BagItem():
                        print("Bagged {} item".format(x))
                    else:
                        print("Missed item")
        time.sleep(2)




