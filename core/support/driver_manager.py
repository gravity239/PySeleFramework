from abc import abstractmethod


class DriverManager():

    def __init__(self):
        pass
    
    @abstractmethod
    def create_driver(self, driver_key):
        pass
