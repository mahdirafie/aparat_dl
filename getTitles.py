import codecs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def get_titles(url):
    
    # Create driver
    driver = webdriver.Firefox()
    
    try:
        driver.get(url)

        page_titles = []

        # Wait for the page to load
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div/div[2]/ul")))

        # Get all links
        ul = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/ul")
        lis = ul.find_elements(By.TAG_NAME, "li")

        action = ActionChains(driver)
        aida = 0

        for li in lis:
            # a = li.find_element(By.CLASS_NAME, "title") // use this if the below code did not work
            a = li.find_element(By.CSS_SELECTOR, ".title")
            page_titles.append(a.text)

        if len(page_titles) > 0:
            with codecs.open("titles.txt", "w", "utf-8") as f:
                for title in page_titles:
                    f.write(title + "\n")
    finally:
        driver.quit()