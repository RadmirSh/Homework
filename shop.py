import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver

# driver = webdriver.Chrome(
#     executable_path='C:/chromedriver.exe')
# driver.maximize_window()
#
# driver.get(
#     "http://practice.automationtesting.in/")
# driver.find_element_by_link_text('My Account').click()
# login_email = driver.find_element_by_id('username')
# login_email.send_keys('asd@mail.ru')
# login_password = driver.find_element_by_id('password')
# login_password.send_keys('Qwe061??]]')
# driver.find_element_by_tag_name("input[name='login']").click()
# time.sleep(3)
# driver.find_element_by_link_text('Shop').click()
# driver.find_element_by_tag_name("a[data-product_id='181']").click()
# name_of_book= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.XPATH, "//*[@id='product-181']/div[2]/h1"), "HTML5 Forms"))
#
# # driver.quit()
# ---------------------------------------------------------------
# driver = webdriver.Chrome(
#     executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get(
#     "http://practice.automationtesting.in/")
# driver.find_element_by_link_text('My Account').click()
# login_email = driver.find_element_by_id('username')
# login_email.send_keys('asd@mail.ru')
# login_password = driver.find_element_by_id('password')
# login_password.send_keys('Qwe061??]]')
# driver.find_element_by_tag_name("input[name='login']").click()
# driver.find_element_by_link_text('Shop').click()
# driver.find_element_by_link_text("HTML").click()
# books_count = driver.find_elements_by_class_name("product")
# if len(books_count) == 3:
#     print("В корзине 3 товара")
# else:
#     print("Ошибка. Количество товаров в корзине: " + str(len(books_count)))

# driver.quit()
# ---------------------------------------------------------------
# driver = webdriver.Chrome(
#     executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get(
#     "http://practice.automationtesting.in/")
# driver.find_element_by_link_text('My Account').click()
# login_email = driver.find_element_by_id('username')
# login_email.send_keys('asd@mail.ru')
# login_password = driver.find_element_by_id('password')
# login_password.send_keys('Qwe061??]]')
# driver.find_element_by_tag_name("input[name='login']").click()
# driver.find_element_by_link_text('Shop').click()
# element_field = driver.find_element_by_class_name('orderby')
# element_check = element_field.get_attribute("value")
# if element_check == "menu_order":
#     print("выбрано дефолтное значение")
# else:
#     print("выбрано значение не по умолчанию")
# element = driver.find_element_by_class_name("orderby")
# select = Select(element)
# select.select_by_value("price-desc")
# element_field_two = driver.find_element_by_class_name('orderby')
# element_check = element_field_two.get_attribute("value")
# if element_check == "price-desc":
#     print("выбрана сортировка от большей к меньшей цене")
# else:
#     print("выбрана иная сортировка")
# driver.quit()
# ---------------------------------------------------------------
# driver = webdriver.Chrome(
#     executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get(
#     "http://practice.automationtesting.in/")
# driver.find_element_by_link_text('My Account').click()
# login_email = driver.find_element_by_id('username')
# login_email.send_keys('asd@mail.ru')
# login_password = driver.find_element_by_id('password')
# login_password.send_keys('Qwe061??]]')
# driver.find_element_by_tag_name("input[name='login']").click()
# driver.find_element_by_link_text('Shop').click()
# driver.find_element_by_tag_name("a[data-product_id='169']").click()
# old_price_element = driver.find_element_by_css_selector("del>span")
# element_get_text = old_price_element.text
# assert element_get_text == "₹600.00"
# new_price_element = driver.find_element_by_css_selector('ins>span')
# element_get_text = new_price_element.text
# assert element_get_text == "₹450.00"
# driver.find_element_by_tag_name("img[alt='Android Quick Start Guide']").click()
# preview_element = WebDriverWait(driver, 2).until(
#     EC.presence_of_element_located((By.ID, "fullResImage")))
# close_element = WebDriverWait(driver, 2).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "pp_close")))
# driver.find_element_by_class_name('pp_close').click()
# driver.quit()
# ---------------------------------------------------------------
# driver = webdriver.Chrome(
#     executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get(
#     "http://practice.automationtesting.in/")
# driver.find_element_by_link_text('Shop').click()
# driver.find_element_by_tag_name('a[data-product_id="182"]').click()
# time.sleep(10)
# element = driver.find_element_by_id("wpmenucartli")
# element_get_text = element.text
# assert "₹180.00" in element_get_text
# driver.find_element_by_id("wpmenucartli").click()
# subtotal_element = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.TAG_NAME, "td[data-title='Subtotal']"), "180.00"))
# total_element = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.TAG_NAME, "strong"), "183.60"))
# driver.quit()
# ---------------------------------------------------------------
# driver = webdriver.Chrome(
#     executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get(
#     "http://practice.automationtesting.in/")
# driver.find_element_by_link_text('Shop').click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_tag_name("a[data-product_id='182']").click()
# time.sleep(3)
# driver.find_element_by_tag_name("a[data-product_id='180']").click()
# element_basket = driver.find_element_by_id("wpmenucartli").click()
# time.sleep(3)
# driver.find_element_by_class_name('product-remove .remove').click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='page-34']/div/div[1]/div[1]/a").click()
# driver.find_element_by_tag_name("input[title='Qty']").clear()
# quantity = driver.find_element_by_tag_name("input[title='Qty']")
# quantity.send_keys('3')
# driver.find_element_by_name('update_cart').click()
# element_quantity = driver.find_element_by_tag_name("input[title='Qty']")
# element_check = element_quantity.get_attribute("value")
# assert element_check == "3"
# time.sleep(3)
# driver.find_element_by_name('apply_coupon').click()
# time.sleep(10)
# coupon_element = driver.find_element_by_id('page-34')
# element_get_text = coupon_element.text
# assert "Please enter a coupon code" in element_get_text
# driver.quit()
# ---------------------------------------------------------------
driver = webdriver.Chrome(
    executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get(
    "http://practice.automationtesting.in/")
driver.find_element_by_link_text('Shop').click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_tag_name("a[data-product_id='182']").click()
time.sleep(3)
driver.find_element_by_id("wpmenucartli").click()
proceed_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "a[href='https://practice.automationtesting.in/checkout/']")))
driver.find_element_by_tag_name("a[href='https://practice.automationtesting.in/checkout/']").click()
name_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "billing_first_name")))
name_element_enter = driver.find_element_by_id("billing_first_name")
name_element_enter.send_keys('Asya')
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys('Askina')
email = driver.find_element_by_id("billing_email")
email.send_keys('asd@mail.ru')
phone = driver.find_element_by_id("billing_phone")
phone.send_keys('456321')
driver.find_element_by_id("s2id_billing_country").click()
enter = driver.find_element_by_id('s2id_autogen1_search')
enter.send_keys('Hungary')
driver.find_element_by_id('select2-results-1').click()
adress = driver.find_element_by_id('billing_address_1')
adress.send_keys('Hanty')
city = driver.find_element_by_id('billing_city')
city.send_keys('Manty')

driver.find_element_by_id("s2id_billing_state").click()
enter_county = driver.find_element_by_id('s2id_autogen2_search')
enter_county.send_keys('Pest')
driver.find_element_by_class_name('select2-result-label .select2-match').click()

postcode = driver.find_element_by_id('billing_postcode')
postcode.send_keys('Fgtr')

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
driver.find_element_by_id('payment_method_cheque').click()
driver.find_element_by_id('place_order').click()

thanks_element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"),
                                     "Thank you. Your order has been received."))
method_element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "method"),
                                     "Check Payments"))
# driver.quit()