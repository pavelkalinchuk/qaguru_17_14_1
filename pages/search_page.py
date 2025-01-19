from selene import be, have, by
from selene.support.shared import browser


from pages.base_page import BasePage


class SearchPage(BasePage):
    def search_profession(self, profession):
        self.should_search_field().click().type(profession).press_enter()
        browser.element('.bloko-modal-close-button').click()
        browser.element('.search-catalog-header-magritte').should(be.visible)

    @staticmethod
    def should_specialization(specialization):
        checkbox = browser.element(by.xpath(
            "//div[@class='magritte-text___pbpft_3-0-22 magritte-text_style-primary___AQ7MW_3-0-22 "
            f"magritte-text_typography-label-2-regular___ia7GB_3-0-22']//div[text()='{specialization}']"))
        checkbox.should(have.text(specialization))

    @staticmethod
    def test_checkbox_tester():
        # Находим и проверяем чекбокс "Тестировщик"
        # browser.driver.execute_script("document.body.style.zoom='45%'")
        browser.driver.execute_script("window.scrollBy(0,500)", "")
        browser.driver.execute_script("window.scrollBy(0,500)", "")
        browser.driver.execute_script("window.scrollBy(0,500)", "")
        checkbox_xpath = ("//input[@class='magritte-checkbox-input___Y41Ta_3-0-29 "
                          "magritte-checkbox-input-unchecked___Mupry_3-0-29' and @type='checkbox' and @value='124']")
        # checkbox_xpath = "//input[@class='magritte-checkbox-input___Y41Ta_3-0-29 magritte-checkbox-input-unchecked___Mupry_3-0-29' and @type='checkbox' and @value='124']"

        # Кликаем на чекбокс "Тестировщик"
        browser.element(checkbox_xpath).click()


    @staticmethod
    def test_vacancies_for_testers():
        # Прокручиваем страницу на верх
        browser.driver.execute_script("window.scrollTo(0, 0);")
        # Находим элемент по атрибуту data-qa
        title_element = browser.element(by.css('[data-qa="title"]'))
        # Проверяем текст элемента
        title_element.should(have.text('635 вакансий «тестировщик»'))

