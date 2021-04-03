from selenium import webdriver
from threading import Thread
from API import API

PATH = r"driver/msedgedriver.exe"

driver = webdriver.Edge(PATH)
API = API(driver)
while True:
    for x in API.StreamerList:
        if API.gotoStreamer(x) and API.StreamerList[x] < 2:
            if API.CreateTimer(x):
                print("Bagged {} item".format(x))




