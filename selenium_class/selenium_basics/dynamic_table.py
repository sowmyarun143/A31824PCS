'''
Created on 28-Oct-2024

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
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

"""Dynamic table"""
"""1. Print dynamic data from paragraph"""
dynamic_datas = driver.find_element(By.ID, "displayValues")
print(dynamic_datas.text)

"""2. read dynamic table data and print all data"""
# dynamic_table = driver.find_element(By.ID, "taskTable")
# cols = dynamic_table.find_elements(By.TAG_NAME, "th")
# rows = dynamic_table.find_elements(By.TAG_NAME, "tr")
# for i in range(len(cols)):
#     for j in range(1,len(rows)):
#         data = rows[j].find_elements(By.TAG_NAME, "td")[i]
#         print(data.text)
        
"""3 take name from user and print corresponding data's"""
name = input("Enter the name which is in dynamic table to print data's:")
dynamic_table = driver.find_element(By.ID, "taskTable")
cols = dynamic_table.find_elements(By.TAG_NAME, "th")
rows = dynamic_table.find_elements(By.TAG_NAME, "tr")
for i in range(1,len(cols)):
    for j in range(1,len(rows)):
        dynamic_name_col = rows[j].find_elements(By.TAG_NAME, "td")[0]
        dynamic_name = dynamic_name_col.text
        if name == dynamic_name:
            cols_data= rows[j].find_elements(By.TAG_NAME, "td")[i]
            headers=rows[0].find_elements(By.TAG_NAME, "th")[i]
            header_name=headers.text
            print(f"{header_name} of {name} process:",cols_data.text)
            break