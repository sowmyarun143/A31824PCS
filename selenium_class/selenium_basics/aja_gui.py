'''
Created on 27-Oct-2024

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
driver.get("https://testautomationpractice.blogspot.com/p/gui-elements-hidden.html")
driver.implicitly_wait(20)

"""3 Create actonchains class object"""
my_actions=ActionChains(driver)


"""4 GUI elements and Ajax"""
"""4a Input box 1 text area"""
input_box1 = driver.find_element(By.XPATH,'//*[@id="input1"]')
input_box1.send_keys("sowmya")
checkbox_1 = driver.find_element(By.ID, "checkbox1")
checkbox_1.click()
toggle_input_box2 = driver.find_element(By.ID, "toggleInput") 
toggle_input_box2.click()
input_box2 = driver.find_element(By.XPATH,'//*[@id="input2"]')
input_box2.send_keys("sarthak")
toggle_checkbox2 = driver.find_element(By.ID, "toggleCheckbox") 
toggle_checkbox2.click()
checkbox_2 = driver.find_element(By.ID, "checkbox2")
checkbox_2.click()
"""Scrolling"""
my_actions.scroll_by_amount(0,500).perform()
load_ajax_content_btn = driver.find_element(By.ID,"loadContent")
load_ajax_content_btn.click()
ajax_content_header=driver.find_element(By.XPATH, '//*[@id="ajaxContent"]/h2')
print(ajax_content_header.text)
ajax_content_para=driver.find_element(By.XPATH, '//*[@id="ajaxContent"]/p')
print(ajax_content_para.text)