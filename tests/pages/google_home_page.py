from element.text_box import TextBox


class GoogleHomePage():
    
    _txt_search = TextBox("name=q")

    def __init__(self):
        pass
    
    def open_google(self):
        pass

    def search(self, key_word):
        self._txt_search.send_keys(key_word)
