import allure
from allure_commons.types import AttachmentType
from selenpy.support.factory import *
import selenium

class Utilities(object):

    @staticmethod
    def attach_screenshot_for_allure_report():
        from datetime import datetime
        str_time = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
        try:
            allure.attach(get_shared_driver().get_screenshot_as_png(),
                          name="Screenshot_" + str_time,
                          attachment_type=AttachmentType.PNG)

        except selenium.common.exceptions.UnexpectedAlertPresentException:
            DriverManager.get_shared_driver().switch_to_alert().accept()
            allure.attach(get_shared_driver().get_screenshot_as_png(),
                          name="Screenshot_" + str_time,
                          attachment_type=AttachmentType.PNG)


