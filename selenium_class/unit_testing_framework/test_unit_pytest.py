'''
Created on 03-Nov-2024
pytest framework
@author: Hp
'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.parametrize("username,password,expected_url",
                         [
                             ("Admin","admin123","dashboard/index"),
                             ("Admin","admin","auth/login")
                             ]
    )
def test_Login(username,password,expected_url):
    options = ChromeOptions()
    options.add_experimental_option("detach",True)
    options.add_argument("start-maximized")
    driver = Chrome(options = options)
    """2. Navigate to Site"""
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    """Login """
    # user_name_given = input("Enter user name to login:")
    # password_given = input("Enter password to login:")
    # if user_name_given == "Admin" and password_given == "admin123":
    login_input=driver.find_element(By.NAME, "username")
    login_input.send_keys(username)
        
    pswd = driver.find_element(By.NAME,"password")
    pswd.send_keys(password)
    # else:
    #     print("invalid credentials,Please check!")
        
    submit = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    submit.click()
        
        # expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    actual_url = driver.current_url
        # self.assertEqual(actual_url,expected_url,"Login failed")
        # assert actual_url==expected_url,"login Failed"
    assert expected_url in actual_url,"Login Failed"