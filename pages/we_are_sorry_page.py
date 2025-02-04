from pages.base_page import BasePage
from .locators.locators import WeAreSorryPageLocators


class WeAreSorryPage(BasePage):
    """
    We are sorry Page
    """

    def check_page_title(self, title_text: str = '', timeout: float = 5):
        """
        Checks page title

        :param title_text: text of title
        :param timeout: timeout of waiting
        """

        default_title = "We're sorry, but we couldn't find any contractors\nmatching your project requirements."
        title_text = title_text if title_text else default_title

        locator = WeAreSorryPageLocators.title
        self.should_be_visible(locator, timeout=timeout, msg="Couldn't go to page We are sorry")
        title = self.get_element(locator)
        self.should_contain_text(title, title_text, msg=f"We are sorry title hasn't text '{title_text}'")
