from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from chaojiying import Chaojiying_Client
import time

driver_path = r"C:\chromedriver.exe"
# option = Options()
# option.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="J-userName"]').send_keys('17882506110')
driver.find_element_by_xpath('//*[@id="J-password"]').send_keys('1234445')
#滑动模块
btn = driver.find_element_by_xpath('//*[@id="nc_3_n1z"]')
ActionChains(driver).drag_and_drop_by_offset(btn,300,0).perform()

