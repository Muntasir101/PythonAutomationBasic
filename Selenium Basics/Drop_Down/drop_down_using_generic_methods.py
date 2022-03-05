from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from drop_down_methods import *

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
industry_drop_down = driver.find_element(By.ID, 'Form_submitForm_Industry')
country_drop_down = driver.find_element(By.ID, 'Form_submitForm_Country')

# drop_down(industry_drop_down, 'Education')
# drop_down(country_drop_down, 'Bangladesh')

# show_all_drop_down_items(country_drop_down)

# stop_after_specific_value(country_drop_down, 'Bangladesh')

industry_drop = driver.find_elements(By.ID, 'Form_submitForm_Industry')
without_using_select(industry_drop)
