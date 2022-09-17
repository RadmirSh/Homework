import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.get(
    "http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_tag_name('h3').click()
driver.find_element_by_tag_name("a[href='#tab-reviews']").click()
driver.find_element_by_class_name("star-5").click()
review_comment = driver.find_element_by_id('comment')
review_comment.send_keys('Nice book!')
time.sleep(1)
review_name = driver.find_element_by_id('author')
review_name.send_keys('Nikolay')
time.sleep(1)
review_email = driver.find_element_by_id('email')
review_email.send_keys('asd@mail.ru')
time.sleep(1)
review_submit = driver.find_element_by_id('submit')
review_submit.click()
time.sleep(2)
driver.quit()