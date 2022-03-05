from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

base_url = "https://www.amazon.com/"


class Headless:
    def chrome_headless(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get(base_url)
        driver.implicitly_wait(5)
        print("Title of the Page in chrome : ", driver.title)

    def firefox_headless(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        driver.get(base_url)
        driver.implicitly_wait(5)
        print("Title of the Page in Firefox: ", driver.title)


obj = Headless()
obj.chrome_headless()
obj.firefox_headless()
