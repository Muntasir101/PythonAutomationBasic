from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://classic.crmpro.com/index.html")
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div/input')

action_chain = ActionChains(driver)
action_chain.send_keys_to_element(username, 'admin').perform()
action_chain.send_keys_to_element(password, 'admin12345').perform()
action_chain.click(login_button).perform()

driver.close()
