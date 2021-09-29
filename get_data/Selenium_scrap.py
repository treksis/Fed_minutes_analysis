from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

def scrap_links():

    link_lst = []
    driver = webdriver.Chrome(PATH)

    # go to federal reserve's search page and click the minutes box

    driver.get("https://www.federalreserve.gov/monetarypolicy/materials/")
    time.sleep(2)
    click_minutes_box = driver.find_element_by_css_selector('.col-lg-6:nth-of-type(7) input').click()
    time.sleep(2)
    click_submit = driver.find_element_by_css_selector("div.row > div > div > form > button").click()
    time.sleep(2)

    

    for i in range(11):
        time.sleep(1)
        # get the all url links

        minutes_rows = driver.find_elements_by_css_selector("div.row.fomc-meeting")

        time.sleep(1)


        for minute_row in minutes_rows:
            a_tags = minute_row.find_elements_by_tag_name("a")
            time.sleep(0.2)
            for a_tag in a_tags:
                link = a_tag.get_attribute("href")
                if "htm" in link:
                    link_lst.append(link) 
                #print(a_tag.get_attribute("href"))

        time.sleep(2)
        next_page = driver.find_element_by_css_selector("ul > li:nth-child(13) > a").click()

        # Remove Duplicates in case of browser discrepancies
        h = list(dict.fromkeys(link_lst))
        
    return h