from test_yaml.page.base_page import BasePage
from test_yaml.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../datas/main.yml")
        return Market(self._driver)