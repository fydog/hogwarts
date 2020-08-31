from test_yaml.page.base_page import BasePage


class Search(BasePage):
    def search(self, value):
        self._params["value"]=value
        self.steps("../datas/search.yml")