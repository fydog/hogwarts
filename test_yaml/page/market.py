from test_yaml.page.base_page import BasePage
from test_yaml.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../datas/market.yml")
        return Search(self._driver)