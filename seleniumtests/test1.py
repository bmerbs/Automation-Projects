from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_run_example():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    
    search = driver.find_element(by=By.NAME, value="q")

    search.send_keys("Selenium")
    search.send_keys(Keys.RETURN)

    driver.quit()
