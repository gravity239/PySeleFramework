class SharedWebDriver():

    @property
    def driver(self):
        return self._webdriver

    @driver.setter
    def driver(self, value):
        self._webdriver = value

    def __init__(self):
        self._webdriver = None

