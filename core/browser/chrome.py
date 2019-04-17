from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver():

    def create_driver(self):
        options = webdriver.ChromeOptions()
        return webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                            options=options,
                            desired_capabilities=None)
        
