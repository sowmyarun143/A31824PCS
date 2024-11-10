'''
Created on 26-Oct-2024

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

"""4 Fetch data from static web table""" 
# book_name1=driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]')
# print(book_name1.text)
table_name = driver.find_element(By.NAME,"BookTable")
rows = table_name.find_elements(By.TAG_NAME, "tr")
for j in range(0,4):
    for i in range(1,len(rows)):
        col = rows[i].find_elements(By.TAG_NAME, "td")[j]
        print(col.text)
while True:
    user_book_name = input("Enter the book name which is in the static web table to know the price:")
    table_name = driver.find_element(By.NAME,"BookTable")
    rows = table_name.find_elements(By.TAG_NAME, "tr")
    for i in range(1,len(rows)):
        col = rows[i].find_elements(By.TAG_NAME, "td")[0]
        book_name = col.text
        if user_book_name == f"{book_name}\t":
            price = rows[i].find_elements(By.TAG_NAME,"td")[3]
            print(price.text)  
            break   