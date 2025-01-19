import pickle

from dotenv import load_dotenv
import os
from selene import browser
import pytest
from selenium import webdriver
from allure_attach import *


# Загрузка переменных окружения из файла .env
load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--window-size=1920,1080')
    selenoid_capabilities = {
        "browserName": "chrome",  # тип браузера
        "browserVersion": "125",  # версия браузера
        "selenoid:options": {  # установка разрешения на запись видео во время теста
            "enableVNC": True,
            "enableVideo": True,
        }
    }

    # Получение учетных данных из переменных окружения
    selenoid_user = os.getenv('SELENOID_USER')
    selenoid_password = os.getenv('SELENOID_PASSWORD')
    selenoid_host = os.getenv('SELENOID_HOST')

    driver_options.capabilities.update(selenoid_capabilities)

    selenoid_url = f'https://{selenoid_user}:{selenoid_password}@{selenoid_host}/wd/hub'
    driver = webdriver.Remote(command_executor=selenoid_url, options=driver_options)

    browser.config.driver = driver
    browser.config.base_url = 'https://hh.ru'
    browser.open('/')

    # Изменяем масштаб страницы
    # browser.driver.execute_script("document.body.style.zoom='45%'")
    # browser.driver.execute_script("window.scrollBy(0,1500)", "")

    yield browser

    # прикрепляем скриншоты, логи браузера, html-код страницы, видеозапись теста
    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)
    add_video(browser)

    print("\nТестирование завершено. Закрываем браузер!")
    browser.quit()
