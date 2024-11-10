'''
Created on 15-Oct-2024
login 
@author: Hp
'''
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
# import time
"""1. Launch Chrome browser"""
options = ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("start-maximized")
driver = Chrome(options = options)
"""2. Navigate to Practice Site"""
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(30)
print(driver.title)
"""3. Enter Name """
"""3a. Locate the Element """
name_txtbx=driver.find_element(By.ID,"name")

"""3b. Interact with the Element """
name_txtbx.send_keys("Sowmya")

"""4. Enter Email """
"""4a. Locate the Element """
email_txtbx=driver.find_element(By.ID,"email")

"""4a. Interact with the Element """
email_txtbx.send_keys("sowmyashree0195@gmail.com")

"""5. Enter Phone """
"""5a. Locate the Element """
phno_txtbx=driver.find_element(By.ID,"phone")

"""5a. Interact with the Element """
phno_txtbx.send_keys("8971769681")

"""6. Enter Address"""
"""6a. Locate the Element """
addr_txtbx=driver.find_element(By.ID,"textarea")

"""6b. Interact with the Element """
addr_txtbx.send_keys("vijaynagar 4th phase,2nd stage,near sankalpa apartment,Mysore-570011")

"""7. Wikipedia search input"""
"""7a. Locate the Element """
search_txtbx=driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input")

"""7b. Interact with the Element """
search_txtbx.send_keys("selenium")

"""7c. wikipidea search button"""
"""7d. Locate the element"""
wiki_search_button=driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
wiki_search_button.click()
# time.sleep(5)

"""8 selenium"""
selenium_search = driver.find_element(By.XPATH,"(//*[@id='wikipedia-search-result-link']/a)[3]")
selenium_search.click()

print(driver.window_handles)#gives list of windows 
print(driver.current_window_handle)

list_of_windows=driver.window_handles
driver.switch_to.window(list_of_windows[1])
print(driver.title)#using title of tab it showing the current page we are to validate
inside_selenium_history = driver.find_element(By.XPATH,"//*[@id='toc-History']/a/div/span[2]")
inside_selenium_history.click()
print(inside_selenium_history.text)#prints which window we are at current page