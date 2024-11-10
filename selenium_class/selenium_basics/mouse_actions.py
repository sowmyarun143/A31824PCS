'''
Created on 21-Oct-2024

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
# driver.get("https://demo.guru99.com/test/simple_context_menu.html")#context click
driver.implicitly_wait(10)

"""3 Create actonchains class object"""
my_actions=ActionChains(driver)

"""4 Double click to copy field1 to field2"""
# copy_txt_btn=driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
# my_actions.double_click(copy_txt_btn).perform()

"""5 Drag and Drop"""
# source = driver.find_element(By.ID,"draggable")
# target = driver.find_element(By.ID,"droppable")
# my_actions.drag_and_drop(source, target).perform()

# """6 Slider"""
# while True:
#     lower_range = int(input("Enter the lower range of slider:"))
#     upper_range = int(input("Enter the upper range of slider:"))
#     source1 = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
#     my_actions.drag_and_drop_by_offset(source1, lower_range, 0).perform()
#     source2 = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")
#     my_actions.drag_and_drop_by_offset(source2,upper_range,0).perform()
"""Scrolling"""
my_actions.scroll_by_amount(0,700).perform()

"""8 Mouse Hover """
point_me_btn = driver.find_element(By.CLASS_NAME,"dropbtn")
my_actions.move_to_element(point_me_btn).perform()

"""9 context click(Right click)"""
# "https://demo.guru99.com/test/simple_context_menu.html"
# right_click = driver.find_element(By.XPATH,"//*[@id='authentication']/span")
# my_actions.context_click(right_click).perform()

