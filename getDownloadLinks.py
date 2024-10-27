import time
import codecs
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Illustration playlist 
url = "https://www.aparat.com/playlist/1640324"
base_url = "https://www.aparat.com"
# Create driver
driver = webdriver.Firefox()
driver.get(url)

download_links = []

with codecs.open("links.txt", "r", "utf-8") as f:
    lines = f.readlines()
    for line in lines:
        driver.get(base_url + line)
        
        WebDriverWait(driver, 100).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "single-playlist__title")))
        meta = driver.find_element(By.XPATH, "//meta[@property='og:video']")

        content = meta.get_dom_attribute("content")
        print(content)
        download_links.append(content)

with codecs.open("download_links.txt", "w", "utf-8") as f:
    for link in download_links:
        f.write(link + "\n")