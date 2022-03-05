from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
alert_button = driver.find_element(By.NAME, 'proceed').click()
alert = driver.switch_to.alert
time.sleep(5)
alert.accept()
print("Alert Accepted")
driver.switch_to.default_content()
# alert.dismiss()
time.sleep(3)
driver.quit()
