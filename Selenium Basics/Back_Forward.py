import webdriver_manager.chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Today's Deals").click()
time.sleep(2)

driver.back()  # Go back to Homepage
time.sleep(2)
# driver.refresh()

driver.forward()  # Again go to Today's Deals Page
time.sleep(2)

driver.back()  # Again go to homepage
time.sleep(2)

driver.refresh()


