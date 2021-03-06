from threading import Thread
from cookie import cookies
from selenium.common.exceptions import NoSuchElementException        
import time

class API:
    def __init__(self, driver):
        self.TwitchPath = "https://twitch.tv/"
        self.Live = '//*[@id="root"]/div/div[2]/div/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/a/div[2]/div/div/div'
        self.WatchBc = '//*[@id="root"]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[5]/div/div[3]/button/div/div'
        self.isRust = '//*[@id="root"]/div/div[2]/div/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/a/span'
        self.Cookie = cookies
        self.driver = driver
        self.LoggingIn = False
        self.StreamerList = {
            "ShackyHD": 0,
            "starsmitten": 0,
            "itsRyanHiga": 0,
            "Frost_": 0,
            "kkatamina": 0,
            "xChocoBars": 0,
            "QuarterJade": 0,
            "iiTzTimmy": 0,
            "Natsumii": 0
        }

        self.Threads()

    def Threads(self):
        Thread(target=self.isLogged).start()


    def check_if_exists(self, xpath: str) -> bool:
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def login(self) -> bool:
        for x in self.Cookie:
            self.driver.add_cookie(x)
        self.driver.refresh()
    
        return True
    
    def isLoggedin(self) -> bool:
        for x in self.driver.get_cookies():
            if x["value"].lower() == "Twitch name here ALL LOWER CASE!":
                return True
        return False

    def gotoStreamer(self, streamer: str) -> bool:
        self.driver.get(self.TwitchPath + streamer)
        time.sleep(1)
        print(self.check_if_exists(self.Live))
        if self.check_if_exists(self.Live) and self.driver.find_element_by_xpath(self.isRust).text.lower() == "rust":
            return True
        return False


    def CreateTimer(self, streamer: str) -> bool:
        for x in self.StreamerList:
            if x == streamer:
                if self.check_if_exists(self.WatchBc):
                    self.driver.find_element_by_xpath(self.WatchBc).click()
                for x in range(round(abs((self.StreamerList[streamer]*60) - 120)/10)+1):
                    if not self.gotoStreamer(streamer):
                        self.LoggingIn = False
                        return False
                    self.LoggingIn = True
                    time.sleep(10 * 60)
                    self.StreamerList[streamer] += round(1/6, 1)
                    if self.StreamerList[streamer] >= 2.2:
                        self.LoggingIn = False
                        return True
                self.LoggingIn = False
                return True


    def BagItem(self):
        Bagged = False
        self.driver.get("https://www.twitch.tv/drops/inventory")
        time.sleep(4)
        while True:
            if self.check_if_exists("//div[text()='Claim Now']"):
                self.driver.find_element_by_xpath("//div[text()='Claim Now']").click()
                Bagged = True
            else:
                break
        return Bagged
    
    def isLogged(self) -> None:
        while True:
            if self.LoggingIn:
                if not self.isLoggedin():
                    print("not logged")
                    self.login()
            time.sleep(5)
