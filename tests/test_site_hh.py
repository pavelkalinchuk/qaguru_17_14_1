import allure

from pages.base_page import BasePage
from pages.search_page import SearchPage

basepage = BasePage()
searchpage = SearchPage()


def test_logo():
    with allure.step("Проверяем корректность открытой страницы наличием логотипа 'hh'"):
        basepage.should_logo()


def test_search_field():
    with allure.step("Проверяем наличие поля поиска на странице"):
        basepage.should_search_field()


def test_search_profession():
    with allure.step("Проверяем поиск по вакансии \"Тестировцик\""):
        searchpage.search_profession('Тестировщик')


def test_should_specialization():
    with allure.step("Проверяем наличие специализации \"Тестировщик\" на странице"):
        searchpage.should_specialization('Тестировщик')


def test_enable_checkbox_tester():
    with allure.step("Устанавливаем чекбокс на специализации \"Тестировщик\""):
        searchpage.test_checkbox_tester()


def test_should_vacancies_testers():
    with allure.step("Проверям количество активных вакансий по специаслизации \"Тестировщик\""):
        searchpage.test_vacancies_for_testers()
