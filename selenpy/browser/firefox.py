from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class FirefoxDriver():
    
    def create_driver(self, remote_host, capabilities):
        options = webdriver.FirefoxOptions()
        if remote_host is None:
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                            options=options,
                            desired_capabilities=capabilities)
        else:
            return webdriver.Remote(command_executor=remote_host,
                                desired_capabilities=options.to_capabilities())
