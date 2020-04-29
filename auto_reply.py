from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time 
import random

# user input
eID = "090829"
measurement = '1'

driver = webdriver.Chrome(executable_path="./chromedriver") 
driver.get('https://zh.surveymonkey.com/r/EmployeeHealthCheck')

# agreement 
xpath1 = '//input[@id="430334642_2860832437"][@type="radio"][@value=2860832437]'
answer_1 = driver.find_elements_by_xpath(xpath1)[0]
driver.execute_script("arguments[0].click();", answer_1)

# employee ID
xpath2 = '//input[@id="430334639"][@type="text"][@name=430334639]'
answer_2 = driver.find_elements_by_xpath(xpath2)[0]
answer_2.clear()
answer_2.send_keys("090829")

# temperature measurement method
if measurement == '1':
    xpath3 = '//input[@id="430334644_2860832441"][@type="radio"][@value=2860832441]'
elif measurement == '2':
    xpath3 = '//input[@id="430334644_2860832442"][@type="radio"][@value=2860832442]'
elif measurement == '3':
    xpath3 = '//input[@id="430334644_2860832443"][@type="radio"][@value=2860832443]'
answer_3 = driver.find_elements_by_xpath(xpath3)[0]
driver.execute_script("arguments[0].click();", answer_3)

# temperature
xpath4 = '//input[@id="430334640"][@type="text"][@name=430334640]'
answer_4 = driver.find_elements_by_xpath(xpath4)[0]
answer_4.clear()
answer_4.send_keys(str(round(random.uniform(35.00, 36.50), 2)))

# take medicines
xpath5 = '//input[@id="447437405_2965044714"][@type="radio"][@value=2965044714]'
answer_5 = driver.find_elements_by_xpath(xpath5)[0]
driver.execute_script("arguments[0].click();", answer_5)

# symptoms
xpath6 = '//input[@id="430334646_2860832447"][@type="checkbox"][@value=2860832447]'
answer_6 = driver.find_elements_by_xpath(xpath6)[0]
driver.execute_script("arguments[0].click();", answer_6)

# Ya
xpath7 = '//input[@id="430334641_2860832427"][@type="radio"][@value=2860832427]'
answer_7 = driver.find_elements_by_xpath(xpath7)[0]
driver.execute_script("arguments[0].click();", answer_7)

# submit
WebDriverWait(driver, 10).until( \
    EC.element_to_be_clickable((By.XPATH, \
        "//button[@class='btn small next-button survey-page-button user-generated notranslate']"))).click()
