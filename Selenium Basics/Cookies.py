from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.espncricinfo.com/")
driver.maximize_window()
cookies = driver.get_cookies()  # Return a Dictionary
print(len(driver.get_cookies()))

my_cookie = {"name": "Cookie_by_Muntasir", "domain": "www.espncricinfo.com", "value": "123466"}
driver.add_cookie(my_cookie)

for cookie in cookies:
    print(cookie)

print(len(driver.get_cookies()))
for cookie in cookies:
    print(cookie)

driver.quit()
