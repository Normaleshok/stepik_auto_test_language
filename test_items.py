import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_items(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button is not None, "Кнопка добавления в корзину не найдена"

