from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

# Selecting the Dropdown

drop_down = driver.find_element(By.ID, 'Form_submitForm_Industry')
value = Select(drop_down)


# Select the item from Dropdown

value.select_by_visible_text('Education')


