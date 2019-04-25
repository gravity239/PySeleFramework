from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver():

    def create_driver(self, remote_host, capabilities):
        options = webdriver.ChromeOptions()
        if remote_host is None:
            return webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                options=options,
                                desired_capabilities=capabilities)
        else:
            return webdriver.Remote(command_executor=remote_host,
                                desired_capabilities=options.to_capabilities())
            
