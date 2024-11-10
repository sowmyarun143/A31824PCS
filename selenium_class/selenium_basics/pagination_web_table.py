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

"""Pagination Web Table"""
# pag_table_name = driver.find_element(By.ID,"productTable")
# pag_rows = pag_table_name.find_elements(By.TAG_NAME, "tr")
# # print(pag_rows)
# print("number of Rows:",len(pag_rows))
# # print(pag_rows[1].text)
# number_of_pages=driver.find_elements(By.XPATH, '//*[@id="pagination"]/li')
# print("number of pages:",len(number_of_pages))
# for i in range(1,(len(number_of_pages)+1)):
#     pag_web_tbl_no = driver.find_element(By.XPATH,f'//*[@id="pagination"]/li[{i}]/a')
#     pag_web_tbl_no.click()
#     print("current page:",pag_web_tbl_no.text)
#     pag_table_name = driver.find_element(By.ID,"productTable")
#     pag_rows = pag_table_name.find_elements(By.TAG_NAME, "tr")
#     number_of_cols = driver.find_elements(By.XPATH,'//*[@id="productTable"]/thead/tr/th')
#     # print("number of columns:",len(number_of_cols))
#     for col in range(0,len(number_of_cols)):
#         for row in range(1,len(pag_rows)):
#             # print(pag_rows[row].text)
#             pag_cols = pag_rows[row].find_elements(By.TAG_NAME,"td")
#             pag_col = pag_cols[col]
#             # print(pag_col)
#             print(pag_col.text)
            
user_name = input("Enter the name which is in the pagination web table to know the price:")
number_of_pages=driver.find_elements(By.XPATH, '//*[@id="pagination"]/li')
for i in range(1,(len(number_of_pages)+1)):
    pag_web_tbl_no = driver.find_element(By.XPATH,f'//*[@id="pagination"]/li[{i}]/a')
    pag_web_tbl_no.click()
    current_page= pag_web_tbl_no.text
    print("current page:",current_page)
    pag_table_name = driver.find_element(By.ID,"productTable")
    pag_rows = pag_table_name.find_elements(By.TAG_NAME, "tr")
    for row in range(1,len(pag_rows)):
        pag_col = pag_rows[row].find_elements(By.TAG_NAME,"td")[1]
        pag_name = pag_col.text
        if user_name == pag_name:
            price = pag_rows[i].find_elements(By.TAG_NAME,"td")[2]
            print(price.text) 
            break
        