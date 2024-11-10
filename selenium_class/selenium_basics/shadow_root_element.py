'''
Created on 01-Nov-2024

@author: Hp
'''
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from _ast import arg

"""1. Launch Chrome browser"""
options = ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("start-maximized")
driver = Chrome(options = options)
"""2. Navigate to Site"""
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

"""1 Enter text inside Shadow root"""#one method
# script='document.querySelector("#shadow_host").shadowRoot.querySelector("input[type=text]:nth-child(5)").value=arguments[0]'
# arg = "Hello"
# driver.execute_script(script,arg)

"""2 upload file inside shadow root"""#second method
"""2a Identifying Parent element"""
shadow_host = driver.find_element(By.ID,"shadow_host")

"""2b Getting access to shadow root element"""
shadow_root = driver.execute_script("return arguments[0].shadowRoot",shadow_host)

"""2c locating and interacting with the elements inside shadowroot"""
# file_input = shadow_root.find_element(By.CSS_SELECTOR,"input[type=file]:nth-child(9)")
# file_input.send_keys("C:/Users/Hp/Iquest/tokensgithub.txt")

# check_box = shadow_root.find_element(By.CSS_SELECTOR,"input[type=checkbox]:nth-child(7)")
# check_box.click()
#
# text_input = shadow_root.find_element(By.CSS_SELECTOR,"input[type=text]:nth-child(5)")
# text_input.send_keys("Sowmya")

# blog = shadow_root.find_element(By.CSS_SELECTOR,"a")
# driver.execute_script("arguments[0].click()",blog)

youtube_link = driver.find_element(By.XPATH, "//*[@id='HTML16']/div[1]/a")
youtube_link.click()
