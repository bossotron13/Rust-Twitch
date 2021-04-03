from selenium import webdriver
from threading import Thread
from API import API

PATH = r"driver/msedgedriver.exe"
API = API(driver)

driver = webdriver.Edge(PATH)

while True:
    for x in API.StreamerList:
        if API.StreamerList[x] < 2:
            if API.gotoStreamer(x):
                if API.CreateTimer(x):
                    print("Bagged {} item".format(x))




