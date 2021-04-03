from selenium import webdriver
from threading import Thread
import time
from API import API

PATH = r"driver/msedgedriver.exe"
driver = webdriver.Edge(PATH)
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




