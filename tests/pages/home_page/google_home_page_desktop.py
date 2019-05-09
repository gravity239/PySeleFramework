import allure
from selenpy.support import browser
from tests.common.utilities import Utilities
from tests.pages.home_page.google_home_page import GoogleHomePage

class GoogleHomePageDesktop(GoogleHomePage):

    @allure.step
    def open_google(self):
        self.log("Navigate to https://google.com")
        browser.open_url("https://google.com")
        browser.wait_for_title_contains("Google")

    @allure.step
    def search(self, key_word):
        self.log("Search for: " + key_word)
        self._txt_search.wait_for_visible()
        self._txt_search.send_keys(key_word)

    @allure.step
    def search_parent(self, key_word):
        self.log("Search for: " + key_word)
        self._txt_search_parent.wait_for_visible()
        self._txt_search_parent.send_keys(key_word)

    @allure.step
    def get_searched_value(self):
        return self._txt_search.value

    @allure.step("Validate the searched value")
    def validate_searched_value(self, expected_searched_value):
        result = False
        try:
            actual_searched_value = self.get_searched_value()
            result = expected_searched_value == actual_searched_value
            if result is False:
                self.log("expected value: " + expected_searched_value + ", actual value: " + actual_searched_value)
        except Exception as ex:
            self.log(ex)
        finally:
            if result is False:
                Utilities.attach_screenshot_for_allure_report()
            return {"Validate that searched value is correct": result}

