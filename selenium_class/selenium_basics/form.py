'''
Created on 28-Oct-2024

@author: Hp
'''
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

"""1. Launch Chrome browser"""
options = ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("start-maximized")
driver = Chrome(options = options)
"""2. Navigate to Site"""
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

"""3 Create action chains class object"""
my_actions=ActionChains(driver)

"""form"""
# form_section1=driver.find_element(By.ID, "input1")
# form_section1.send_keys("python")
# submit_btn1 = driver.find_element(By.ID, "btn1")
# submit_btn1.click()
# form_section2=driver.find_element(By.ID, "input2")
# form_section2.send_keys("selenium")
# submit_btn2 = driver.find_element(By.ID, "btn2")
# submit_btn2.click()
# form_section3=driver.find_element(By.ID, "input3")
# form_section3.send_keys("iquest")
# submit_btn3 = driver.find_element(By.ID, "btn3")
# submit_btn3.click()

"""shadow DOM"""
mobiles = driver.find_element(By.ID, "shadow_host")
print(mobiles.text)