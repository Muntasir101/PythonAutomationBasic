from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://courses.letskodeit.com/practice')
# driver.implicitly_wait(10)


# driver.get_screenshot_as_file('screenshot.png')

# Full Screenshot - Need to running in Headless Mode


class FullScreenshot:
    def full_screenshot(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get("https://courses.letskodeit.com/practice")
        driver.implicitly_wait(10)
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
        driver.set_window_size(S('Width'), S('Height'))
        driver.find_element(By.TAG_NAME, 'body').screenshot('full_screenshot.png')


obj = FullScreenshot()
obj.full_screenshot()
