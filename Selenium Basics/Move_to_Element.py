import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.spicejet.com/")
time.sleep(3)
action_chain = ActionChains(driver)
login_element = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
action_chain.move_to_element(login_element).perform()

spice_club_member_element = driver.find_element(By.LINK_TEXT, 'SpiceClub Members')
action_chain.move_to_element(spice_club_member_element).perform()

member_login = driver.find_element(By.LINK_TEXT, 'Member Login').click()
time.sleep(3)

