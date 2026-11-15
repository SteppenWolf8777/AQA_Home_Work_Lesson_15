import pytest
from selenium import webdriver
from selenium.webdriver import Keys
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
    submit_a_request = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[class^="chakra-button"]'))
    )
    submit_a_request.click()
    search_box = driver.find_element(By.NAME, 'name')
    search_box.send_keys('Alexandr')
    search_box = driver.find_element(By.NAME, 'company')
    search_box.send_keys('Aston')
    search_box = driver.find_element(By.NAME, 'phone')
    search_box.send_keys('78879978787')

    search_box.send_keys(Keys.ENTER)