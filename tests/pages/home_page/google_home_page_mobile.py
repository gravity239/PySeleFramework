import allure

from selenpy.support import browser
from tests.pages.home_page.google_home_page_desktop import GoogleHomePageDesktop


class GoogleHomePageMobile(GoogleHomePageDesktop):

    @allure.step
    def open_google(self):
        self.log("Navigate to https://bing.com")
        browser.open_url("https://bing.com")
        browser.wait_for_title_contains("Bing")

