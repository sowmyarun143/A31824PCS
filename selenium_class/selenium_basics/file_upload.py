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
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

"""3 Create actonchains class object"""
my_actions=ActionChains(driver)

"""Upload single file"""
# single_file_input=driver.find_element(By.ID, "singleFileInput")
# single_file_input.send_keys("C:/Users/Hp/Iquest/tokensgithub.txt")
# single_file_submit = driver.find_element(By.XPATH, "//*[@id='singleFileForm']/button")
# single_file_submit.click()
# print(driver.find_element(By.ID, "singleFileStatus").text)
"""upload multiple file"""
multiple_file_input=driver.find_element(By.ID, "multipleFilesInput")
multiple_file_input.send_keys("C:/Users/Hp/Iquest/tokensgithub.txt")
multiple_file_input.send_keys("C:/Users/Hp/Iquest/Sowmyashree_CV.docx")
multiple_file_submit = driver.find_element(By.XPATH, "//*[@id='multipleFilesForm']/button")
multiple_file_submit.click()
print(driver.find_element(By.ID,"multipleFilesStatus").text)

"""Scrolling"""
my_actions.scroll_by_amount(0,300).perform()
"""screen shot save"""
# driver.save_screenshot("C:/Users/Hp/Iquest/ss.png")