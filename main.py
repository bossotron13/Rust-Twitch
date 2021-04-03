from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException        
import requests, time
from threading import Thread
from cookie import cookies

PATH = r"driver/msedgedriver.exe"

class API:
    def __init__(self):
        self.TwitchPath = "https://twitch.tv/"
        self.Live = '//*[@id="root"]/div/div[2]/div/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div/a/div[2]/div/div/div'
        self.WatchBc = '//*[@id="root"]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[5]/div/div[3]/button/div/div'
        self.Cookie = cookies
        self.StreamerList = {
            "Suspect": 0,
            "NoraExplorer": 0,
            "etoleto": 0,
            "Picco": 0
            "PyrooTv": 0,
            "6zdenko": 0
        }

        self.Threads()
    
    def Threads(self):
        Thread(target=self.isLogged).start()


    def check_if_exists(self, xpath: str) -> bool:
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def login(self) -> bool:
        driver.get("https://twitch.tv/")
        for x in self.Cookie:
            driver.add_cookie(x)
        driver.refresh()
    
        return True
    
    def isLoggedin(self) -> bool:
        for x in driver.get_cookies():
            if x["value"].lower() == "Streamer name here":
                return True
        return False

    def gotoStreamer(self, streamer: str) -> bool:
        driver.get(self.TwitchPath + streamer)
        if self.check_if_exists(self.Live):
            return True
        return False


    def CreateTimer(self, streamer: str) -> bool:
        for x in self.StreamerList:
            if self.check_if_exists(self.WatchBc):
                driver.find_element_by_xpath(self.WatchBc).click()
            if x == streamer:
                for x in range(round(abs((self.StreamerList[streamer]*60) - 120)/10)+1):
                    if not self.gotoStreamer(streamer):
                        return False
                    time.sleep(10 * 60)
                    self.StreamerList[streamer] += round(1/6, 1)
                    if self.StreamerList[streamer] >= 2.2:
                        return True
                return True


    
    def isLogged(self) -> None:
        while True:
            if not self.isLoggedin():
                print("not logged")
                self.login()
            time.sleep(5)
    

driver = webdriver.Edge(PATH)
API = API()
while True:
    for x in API.StreamerList:
        if API.gotoStreamer(x):
            if API.CreateTimer(x):
                print("Bagged {} item".format(x))




