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
driver.get("https://www.amazon.in/price/s?k=price")
driver.implicitly_wait(10)

"""3 Create actonchains class object"""
my_actions=ActionChains(driver)

# lower_bound_slider = driver.find_element(By.ID, "p_36/range-slider_slider-item_lower-bound-slider")
# # my_actions.drag_and_drop_by_offset(lower_bound_slider,40, 0).perform()
# lower_bound_slider.send_keys(100)
# go_btn=driver.find_element(By.XPATH,"//*[@id='a-autoid-24']/span/input")
# go_btn.click()
# my_actions.click_and_hold(lower_bound_slider).move_by_offset(30, 0).release(lower_bound_slider).perform()

lower_bound = driver.find_element(By.ID, "p_36/range-slider_slider-item_lower-bound-slider")
document.getElementById("p_36/range-slider_slider-item_lower-bound-slider").value=500

document.getElementById("p_36/range-slider_slider-item_lower-bound-slider").dispatchEvent(new Event("change"))
