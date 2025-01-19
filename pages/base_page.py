from selene.support.shared import browser
from selene import be


class BasePage:
    @staticmethod
    def should_logo():
        browser.element('.supernova-logo').should(be.visible)

    @staticmethod
    def should_search_field():
        search_field = browser.element('#a11y-search-input').should(be.visible)
        return search_field

