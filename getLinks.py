import time
import codecs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def get_links(url):

    # Create driver
    driver = webdriver.Firefox()
    try:
        driver.get(url)

        page_links = []

        # Wait for the page to load
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div/div[2]/ul")))

        # Get all links
        ul = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/ul")
        lis = ul.find_elements(By.TAG_NAME, "li")

        action = ActionChains(driver)
        aida = 0
        for li in lis:
            aida = aida + 1
            a = li.find_element(By.TAG_NAME, "a")
            action.move_to_element(a)
            action.context_click().perform()
            action.send_keys(Keys.ESCAPE)
            size = a.size
            driver.execute_script("window.scrollTo(0, " + str(aida * (size['height'] + 20)) + ");")
            time.sleep(0.1)
            print("Can Right Click On {} from {}".format(aida, 77))

        for li in lis:
            a = li.find_element(By.TAG_NAME, "a")
            page_links.append(a.get_dom_attribute("href"))

        if len(page_links) > 0:
            with codecs.open("links.txt", "w+", "utf-8") as f:
                for link in page_links:
                    f.write(link + "\n")
    finally:
        driver.quit()
