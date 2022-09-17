import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# driver = webdriver.Chrome(
#     executable_path='C:/chromedriver.exe')
# driver.maximize_window()

# driver.get(
#     "http://practice.automationtesting.in/")
# driver.find_element_by_link_text('My Account').click()
# reg_email = driver.find_element_by_id('reg_email')
# reg_email.send_keys('asd@mail.ru')
# reg_password = driver.find_element_by_id('reg_password')
# reg_password.send_keys('Qwe061??]]')
# driver.find_element_by_tag_name("input[name='register']").click()
# time.sleep(3)
# driver.quit()
# ---------------------------------------------------------------
driver = webdriver.Chrome(
    executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.get(
    "http://practice.automationtesting.in/")
driver.find_element_by_link_text('My Account').click()
login_email = driver.find_element_by_id('username')
login_email.send_keys('asd@mail.ru')
login_password = driver.find_element_by_id('password')
login_password.send_keys('Qwe061??]]')
driver.find_element_by_tag_name("input[name='login']").click()
time.sleep(3)
logout_element = driver.find_element_by_link_text('Logout')
logout_element_get_text = logout_element.text
assert logout_element_get_text == "Logout"
# driver.quit()
