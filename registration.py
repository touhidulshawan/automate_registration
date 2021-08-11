import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# GLOBALS
url = "https://wise.com/register/"
country = "United States"
country_name_for_phone = "USA"
phone_number = "202-555-0165"
password = "T10020001"

try:
    # if you are in windows uncomment below line
    # driver = webdriver.Chrome("./driver/win/chromedriver.exe")
    # if your are in window comment out below line
    driver = webdriver.Chrome("./driver/linux/chromedriver")
    driver.get(url)
    time.sleep(1)

    # email field
    driver.find_element_by_id("email").send_keys("shrabonahmed66@gmail.com")
    time.sleep(1)

    # select next button and click it
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div/section/div/div/div/div/div/div/form/button').click()
    time.sleep(2)

    # select account type
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div/section/div/div/div/div/div/div/div/div/div/a[1]').click()
    time.sleep(2)

    # select country
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div/section/div/div/div/div/div/div/form/div/div/div/button').click()
    time.sleep(1)

    select_country_input = driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div/section/div/div/div/div/div/div/form/div/div/div/ul/li[1]/a/div/input')

    select_country_input.send_keys(country)
    time.sleep(1)
    select_country_input.send_keys(Keys.ENTER)
    time.sleep(1)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div/section/div/div/div/div/div/div/form/button').click()
    time.sleep(2)

    # Give Phone Number
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div/section/div/div/div/div/div/div/div/form/div/div[1]/div/button').click()
    time.sleep(1)

    phone_code_country_input = driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div/section/div/div/div/div/div/div/div/form/div/div[1]/div/ul/li[1]/a/div/input')

    phone_code_country_input.send_keys(country_name_for_phone)
    time.sleep(1)
    phone_code_country_input.send_keys(Keys.ENTER)
    time.sleep(1)

    driver.find_element_by_name("phoneNumber").send_keys(phone_number)
    time.sleep(1)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div/section/div/div/div/div/div/div/div/form/button').click()
    time.sleep(2)

    # insert otp code [ skipped ]

    # password
    driver.find_element_by_id("new-password").send_keys(password)
    time.sleep(1)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div/section/div/div/div/div/div/div/form/button').click()
    time.sleep(2)

except:
    print("Something wrong!!")
