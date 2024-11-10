'''
Created on 16-Oct-2024

@author: Hp
'''
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
"""1. Launch Chrome browser"""
options = ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("start-maximized")
driver = Chrome(options = options)
"""2. Navigate to Practice Site"""
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(30)

"""3 Create action chains class object"""
my_actions=ActionChains(driver)

"""3 Gender """
# gender_chechbox = driver.find_element(By.XPATH,"//*[@id='female']")
# gender_chechbox.click()

"""4 Days"""
days_checkbox_list = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
for i in days_checkbox_list:
        days_checkbox = driver.find_element(By.ID,i)
        days_checkbox.click()
   
# days1_checkbox = driver.find_element(By.ID,"monday")
# days1_checkbox.click()
# days2_checkbox = driver.find_element(By.ID,"tuesday")
# days2_checkbox.click()
# days3_checkbox = driver.find_element(By.ID,"wednesday")
# days3_checkbox.click()
# days4_checkbox = driver.find_element(By.ID,"thursday")
# days4_checkbox.click()
# days5_checkbox = driver.find_element(By.ID,"friday")
# days5_checkbox.click()
# days6_checkbox = driver.find_element(By.ID,"saturday")
# days6_checkbox.click()
# days7_checkbox = driver.find_element(By.ID,"sunday")
# days7_checkbox.click()

"""5 country"""
# country_select = driver.find_element(By.XPATH,"//*[@id='country']/option[10]")
# country_select.click()

"""6 Colors"""
# colors_select = driver.find_element(By.XPATH,"//*[@id='colors']/option[4]")
# colors_select.click()

"""7 Sorted list"""
# sorted_list_select = driver.find_element(By.XPATH,"//*[@id='animals']/option[5]")
# sorted_list_select.click()

"""8 Dynamic button"""
"""8a start button"""
start_button=driver.find_element(By.NAME,"start")
start_button.click()
time.sleep(3)
stop_button=driver.find_element(By.NAME,"stop")
stop_button.click()

"""8b New tab"""
# new_tab_button = driver.find_element(By.XPATH,"//*[@id='HTML4']/div[1]/button")
# new_tab_button.click()

"""9 Alerts and popups"""
# """9a simple alert"""
# simple_alert=driver.find_element(By.ID,"alertBtn")
# simple_alert.click()
# driver.switch_to.alert.accept()

"""9b Confirmation alert"""
# confirmation_alert = driver.find_element(By.ID,"confirmBtn")
# confirmation_alert.click()
# driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()

# """Prompt alert"""
# prompt_alert=driver.find_element(By.ID,"promptBtn")
# prompt_alert.click()
# driver.switch_to.alert.send_keys("sowmya")
# driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()

"""10 Popup window"""
# popup_button=driver.find_element(By.ID,"PopUp")
# popup_button.click()
# print(driver.window_handles)
# list_of_windows = driver.window_handles
# driver.switch_to.window(list_of_windows[2])
# print(driver.title)
# driver.maximize_window()


"""Date picker1"""
# date_picker_1=driver.find_element(By.ID,"datepicker").send_keys("10/15/2024")
date_picker1_text = driver.find_element(By.ID, "datepicker")
date_picker1_text.click()
date_picker_1 = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr[5]/td[2]/a")
date_picker_1.click()
print(date_picker_1.text)

"""Date picker3"""
date_picker_3_a = driver.find_element(By.ID, "start-date")
date_picker_3_a.send_keys("27-10-2024")
date_picker_3_b = driver.find_element(By.ID, "end-date")
date_picker_3_b.send_keys("28-10-2024")
submit = driver.find_element(By.CLASS_NAME,"submit-btn")
submit.click()
print(driver.find_element(By.XPATH,"//*[@id='result']").text)

"""Date picker2"""
date_picker_2=driver.find_element(By.ID,"txtDate")
date_picker_2.click()
select_month = driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/div/select[1]/option[11]")
select_month.click()
select_day = driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr[4]/td[7]/a")
select_day.click()
print(select_day.text)
# table_name = driver.find_element(By.CLASS_NAME,"ui-datepicker-calendar")
# rows = table_name.find_elements(By.TAG_NAME, "tr")
# # for j in range(0,7):
# #     for i in range(1,6):
# #         col = rows[i].find_elements(By.TAG_NAME, "td")[j]
# #         print(col.text)
# day = rows[4].find_elements(By.TAG_NAME, "td")[6]
# print(day.text)


# select_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
# select_year.click()

# """scrolling drop down"""
# scrolling_input=driver.find_element(By.ID,"comboBox")
# scrolling_input.click()
# scrolling_drop_down = driver.find_element(By.XPATH, "//*[@id='dropdown']/div[13]")
# scrolling_drop_down.click()
#
# """Scrolling"""
# my_actions.scroll_by_amount(0,100).perform()
