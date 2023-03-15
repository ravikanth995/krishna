from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
s=Service("C:/VS_New/krishna/selenium/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
time.sleep(7)
driver.find_element(By.ID,"origin").send_keys("KOL")
fromlist=driver.find_element('//[@id="origin"]/span/input')






