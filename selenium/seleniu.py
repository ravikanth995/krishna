from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s=Service("C:/VS_New/krishna/selenium/chromedriver.exe")
driver=webdriver.Chrome(service=s)
# driver.get("https://www.irctc.co.in/nget/train-search")
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)
# print(driver.title)
#IRCTC
# Select(driver.find_element(By.ID,"origin")).select_by_visible_text("KOLKATA-KOAA")
# Select(driver.find_element(By.ID,"destination")).select_by_visible_text("VISAKHAPATNAM - VSKP")

#Facebook
driver.find_element(By.XPATH,"//*[text()='Create new account']").click()
time.sleep(1)
driver.find_element(By.NAME,"firstname").send_keys("Ravikanth")
time.sleep(1)
driver.find_element(By.NAME,"lastname").send_keys("Chavan")
time.sleep(1)
driver.find_element(By.NAME,"reg_email__").send_keys("Ravikanthchavan@gmail.com")
time.sleep(1)
driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("ravikanthchavan@gmail.com")
time.sleep(1)
driver.find_element(By.NAME,"reg_passwd__").send_keys("ravi@123")
time.sleep(1)
day=driver.find_element(By.ID,"day")
dateDD=Select(day)
dateDD.select_by_visible_text("2")
time.sleep(1)
month=driver.find_element(By.ID,"month")
monthDD=Select(month)
monthDD.select_by_visible_text("Jan")
time.sleep(1)
year=driver.find_element(By.ID,"year")
yearDD=Select(year)
yearDD.select_by_visible_text("1995")
time.sleep(1)
driver.find_element(By.XPATH,("//input[@value='2']")).click()
time.sleep(1)
driver.find_element(By.NAME,"websubmit").click()
time.sleep(13)



# driver.find_element(By.CLASS_NAME,"in-line").click()
# time.sleep(2)
# driver.find_element(By.ID,"mat-input-0").send_keys("JKNPK5498A")
# #Select Value
# x=Select(driver.find_element(By.CLASS_NAME,"mat-select-value-text ng-tns-c11-36 ng-star-inserted"))
# x.select_by_value("2019-20")
# time.sleep(10)
# driver.find_element(By.CLASS_NAME,"x6s0dn4 x1npaq5j x1c83p5e x1enjb0b x199158v x9f619 x78zum5 x1q0g3np xvs91rp x1n2onr6 xh8yej3 xnz67gz x5n08af xx7zo7k x1fzb3qy xb0nk2e xubunj8")
# time.sleep(4)
# driver.find_element(By.NAME,"username").send_keys("995698715")
# time.sleep(4)
# driver.find_element(By.NAME,"password").send_keys("ravi@123")
# time.sleep(4)
# driver.find_element(By.CLASS_NAME,"Log in").click()
# time.sleep(10)