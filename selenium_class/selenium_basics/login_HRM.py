'''
Created on 03-Nov-2024

@author: Hp
'''
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

"""1. Launch Chrome browser"""
options = ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("start-maximized")
driver = Chrome(options = options)
"""2. Navigate to Site"""
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)

"""Login """
# user_name = input("Enter user name to login:")
# password = input("Enter password to login:")
# if user_name == "Admin" and password == "admin123":
#     login_input=driver.find_element(By.NAME, "username")
#     login_input.send_keys(user_name)
#
#     pswd = driver.find_element(By.NAME,"password")
#     pswd.send_keys(password)
# else:
#     print("invalid credentials,Please check!")
#
# submit = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
# submit.click()

expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
actual_url = driver.current_url
assert actual_url == expected_url
# if actual_url == expected_url:
#     print("Test passed")
# else:
#     print("Test Failed")