'''
Created on 19-Oct-2024
"""frames"""
#https://demo.automationtesting.in/Frames.html

relative xpath = starting with // 
absolute xpath = starting from begging single slash(/)
@author: Hp
'''
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# from selenium_basics.mouse_actions import my_actions
"""1. Launch Chrome browser"""
options = ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("start-maximized")
driver = Chrome(options = options)
"""2. Navigate to frames Site"""
driver.get("https://demo.automationtesting.in/Frames.html")
driver.implicitly_wait(10)
"""3 Create action chains class object"""
my_actions=ActionChains(driver)
# """switch to iframe"""
# driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
# driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("sowmya")
# driver.switch_to.default_content()#switch back to outside the iframe
# driver.switch_to.parent_frame()#switch back to parent frame
"""iframe with in an iframe"""
# iframe_in_iframe_button=driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe")#by using link_text
# # iframe_in_iframe_button = driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a")
# iframe_in_iframe_button.click()

# driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@id='Multiple']/iframe"))#by xpath
# driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/section/div/div/iframe"))
# driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("Arun")

# driver.switch_to.frame(1)#by index
# driver.switch_to.frame(0)
# driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("Arun")

"""Mouse Hover"""
interactions_dropdown_btn = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[6]/a')
my_actions.move_to_element(interactions_dropdown_btn).perform()
drop_down_btn = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[1]/a')
my_actions.click_and_hold(drop_down_btn).perform()
static_btn = driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[6]/ul/li[1]/ul/li[1]/a')
my_actions.click(static_btn).perform()
source = driver.find_element(By.ID,"node")
target = driver.find_element(By.ID,"droparea")
my_actions.drag_and_drop(source, target).perform()
source1 = driver.find_element(By.ID,"angular")
my_actions.drag_and_drop(source1, target).perform()
source2 = driver.find_element(By.ID,"mongo")
my_actions.drag_and_drop(source2,target).perform()