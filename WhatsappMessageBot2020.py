from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
PATH = "C:\Program Files (x86)\chromedriver.exe"#path of your web driver here i have given the default path of chromedriver

driver = webdriver.Chrome(PATH)
contact = ""#name of your contact

driver.get("https://web.whatsapp.com")
time.sleep(20)
search_bar = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")#search bar
search_bar.click()
search_bar.send_keys(contact)
time.sleep(2)
search_bar.send_keys(Keys.RETURN)
input_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")#input box
input_box.click()
f = open("text.txt",'r')
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")

time.sleep(2)
driver.quit()