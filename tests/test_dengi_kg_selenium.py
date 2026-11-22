import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function', autouse=True)
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_selenium(driver):
    driver.get('https://astondev.ru/')
    search_box_1 = driver.find_element(By.NAME, 'name')
    search_box_1.send_keys('Александр')
    search_box_2 = driver.find_element(By.NAME, 'company')
    search_box_2.send_keys('Aston')
    search_box_3 = driver.find_element(By.NAME, 'phone')
    search_box_3.send_keys('78879978787')
    search_box_4 = driver.find_element(By.NAME, 'email')
    search_box_4.send_keys('test@mail.ru')
    search_box_5 = driver.find_element(By.NAME, 'message')
    search_box_5.send_keys('Test message')
    send_form = driver.find_element(By.CSS_SELECTOR, '#form_button')
    send_form.click()



    # search_box.send_keys(Keys.ENTER)