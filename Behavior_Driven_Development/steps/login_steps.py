from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given(u'I launched Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when(u'I Open ORANGE HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'I enter Username')
def step_impl(context):
    context.driver.find_element_by_id("txtUsername").send_keys("admin")


@when(u'I enter Password')
def step_impl(context):
    context.driver.find_element_by_id('txtPassword').send_keys('admin123')


@when(u'I Click Login')
def step_impl(context):
    context.driver.find_element_by_id('btnLogin').click()


@then(u'User Suceesfully Logged in.')
def step_impl(context):
    text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text()
    assert text == "Dashboard"
    context.driver.close()
