from http.server import executable
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, time
import time
from selenium.common.exceptions import ElementClickInterceptedException

chrome_driver_path = "chrome_driver_path"

#driver = webdriver.Chrome(executable_path=chrome_driver_path)
SIMILAR_ACCOUNT = "other_insta_account_name"
username_n = "YOUR_ACCOUNT_USERNAME"
password_p = "YOUR_ACCOUNT_PASSWORD"

class Instafollower:
    def __init__(self,path):
        self.driver = webdriver.Chrome(executable_path=path)
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        username = self.driver.find_element_by_name("username")
        username.send_keys(username_n)
        password = self.driver.find_element_by_name("password")
        password.send_keys(password_p)
        login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        login.click()
        time.sleep(5)
        save_info = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        save_info.click()
        time.sleep(2)
        not_now = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
        not_now.click()
    def find_followers(self):
        time.sleep(5)
        self.driver.get("https://www.instagram.com/FOLLOWINF_ACCOUNT_NAME/")
        follow = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        follow.click()
        time.sleep(2)
        
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
            
    def follow(self):
        follow = self.driver.find_elements_by_css_selector("li button")
        
        for button in follow:
            if button.text!="Follow":
                pass
            else:
                button.click()
                time.sleep(100)

        
bot = Instafollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()



