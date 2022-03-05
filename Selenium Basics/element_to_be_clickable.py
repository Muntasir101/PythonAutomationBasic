from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
wait = WebDriverWait(driver,10)
login_link = wait.until(ec.element_to_be_clickable((By.NAME, 'proceed')))
print(login_link.text)
login_link.click()
