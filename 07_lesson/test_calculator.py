import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from calculator import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver: WebDriver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open()
    calculator_page.input_field()
    calculator_page.click_calculator_button("7")
    calculator_page.click_calculator_button("+")
    calculator_page.click_calculator_button("8")
    calculator_page.click_calculator_button("=")
    calculator_page.wait_for_result()