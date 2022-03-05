from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random
import string


class InitializeDriver:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://demo.opencart.com/index.php?route=account/register")
    driver.implicitly_wait(10)


class RegisterAutomation(InitializeDriver):
    def __init__(self):
        extensions = ['com', 'net', 'org', 'gov']
        domains = ['gmail', 'yahoo', 'hotmail', 'outlook']
        generate_extension = extensions[random.randint(0, len(extensions) - 1)]
        generate_domain = domains[random.randint(0, len(domains) - 1)]
        m_length = random.randint(1, 20)
        mail = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(m_length))
        self.finale = mail + "@" + generate_domain + "." + generate_extension

    def register_with_valid_data(self):
        first_name = self.driver.find_element_by_id("input-firstname")
        first_name.send_keys("Mr. John")
        last_name = self.driver.find_element_by_id("input-lastname")
        last_name.send_keys("Doe")
        mail = self.driver.find_element_by_id("input-email")
        mail.send_keys(self.finale)
        phone = self.driver.find_element_by_id("input-telephone")
        phone.send_keys("123456789")
        password = self.driver.find_element_by_id("input-password")
        password.send_keys("abcdefgh")
        confirm_password = self.driver.find_element_by_id("input-confirm").send_keys("abcdefgh")
        check_box = self.driver.find_element_by_name("agree").click()
        submit = self.driver.find_element_by_xpath(
            "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[2]").click()
        title = self.driver.title
        # error = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]").text
        if title == "Your Account Has Been Created!":
            print("Account Creation Success and Now You are in Your Dashboard")
        else:
            print("Account Creation Failed Because of " + error)
        self.driver.back()
        self.driver.close()

    def register_with_invalid_data(self):

        first_name = self.driver.find_element_by_id("input-firstname")
        first_name.send_keys("")  # Keeping this field empty
        last_name = self.driver.find_element_by_id("input-lastname")
        last_name.send_keys("Pranto")
        mail = self.driver.find_element_by_id("input-email")
        mail.send_keys(self.finale)
        phone = self.driver.find_element_by_id("input-telephone")
        phone.send_keys("123456789")
        password = self.driver.find_element_by_id("input-password")
        password.send_keys("abcdefgh")
        confirm_password = self.driver.find_element_by_id("input-confirm").send_keys("abcdefgh")
        check_box = self.driver.find_element_by_name("agree").click()
        submit = self.driver.find_element_by_xpath(
            "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[2]").click()
        title = self.driver.title

        if title == "Your Account Has Been Created!":
            print("Account Creation Success and Now You are in Your Dashboard")
        else:
            print("Account Creation Failed")
        self.driver.close()


obj = RegisterAutomation()
# obj.register_with_invalid_data()
obj.register_with_valid_data()

