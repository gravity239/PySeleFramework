from .test_base import TestBase
from selenpy.support import browser
from selenpy.element.iframe import IFrame
from selenpy.element.combo_box import ComboBox


class ComboBoxTest(TestBase):
    
    _result = IFrame("id=iframeResult")
    _select = ComboBox("//select")

    def test_combobox(self):
        browser.open_url("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
        self._result.switch_to()
        self._select.select_by_value("audi")
        assert self._select.first_selected_text == "Audi"
    
