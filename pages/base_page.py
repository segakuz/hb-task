from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class BasePage:
    """
    Base for all pages
    """

    def __init__(self, browser, url: str, timeout: int = 5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Opens the page
        """

        self.browser.get(self.url)

    def get_element(self, locator: tuple) -> WebElement:
        """
        Returns the found element

        :param locator: tuple of search strategy and selector
        :returns: WebElement
        """

        return self.browser.find_element(*locator)

    def get_element_from_element(self, element: WebElement, locator: tuple) -> WebElement:
        """
        Returns the element found in element

        :param element: WebElement
        :param locator: tuple of search strategy and selector
        :returns: WebElement
        """

        return element.find_element(*locator)

    def get_elements(self, locator: tuple) -> list[WebElement]:
        """
        Returns the found elements

        :param locator: tuple of search strategy and selector
        :returns: List[WebElement]
        """

        return self.browser.find_elements(*locator)

    def wait(self, timeout: float = 2, poll_frequency: float = 1,
             ignored_exceptions = (TimeoutException, )) -> WebDriverWait:
        """
        Returns WebDriverWait

        :param timeout: number of seconds before timing out
        :param poll_frequency: sleep interval between calls
        :param ignored_exceptions: iterable structure of exception classes ignored during calls
        :returns: WebDriverWait
        """

        return WebDriverWait(self.browser, timeout, poll_frequency, ignored_exceptions)

    def is_element_visible(self, locator: tuple[str, str], timeout: float = 2):
        """
        Checks that the element is visible

        :param locator: tuple of search strategy and selector
        :param timeout: timeout of waiting
        :returns: bool
        """

        try:
            self.wait(timeout=timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, locator: tuple[str, str], timeout: float = 2):
        """
        Checks that the element is present (does not mean it is visible)

        :param locator: tuple of search strategy and selector
        :param timeout: timeout of waiting
        returns: bool
        """

        try:
            self.wait(timeout=timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_element_clickable(self, element: WebElement, timeout: float = 2):
        """
        Checks that the element is clickable

        :param element: WebElement
        :param timeout: timeout of waiting
        :returns: bool
        """

        try:
            self.wait(timeout=timeout).until(EC.element_to_be_clickable(element))
        except TimeoutException:
            return False
        return True

    def should_be_clickable(self, element: WebElement, timeout: float = 2, msg: str = ""):
        """
        Checks that the element is clickable

        :param element: WebElement
        :param timeout: timeout of waiting
        :param msg: message
        """

        assert self.is_element_clickable(element, timeout), \
            msg if msg else f"Couldn't wait for the element to become clickable in {timeout} seconds"

    def should_contain_text(self, element: WebElement, text: str, msg: str = ""):
        """
        Checks that the element has the text

        :param element: WebElement
        :param text: expected text
        :param msg: message
        """

        assert text == element.text, \
            msg if msg else f"Element does not contain text {text}"

    def should_contain_text_in_value(self, element: WebElement, text: str, msg: str = ""):
        """
        Checks that the element has the text in the value attribute

        :param element: WebElement
        :param text: expected text
        :param msg: message
        """

        assert text == element.get_attribute('value'), \
            msg if msg else f"Element's value does not contain text {text}"

    def should_be_visible(self, locator: tuple[str, str], timeout: float = 2, msg: str = ""):
        """
        Checks that the element is visible

        :param locator: tuple of search strategy and selector
        :param timeout: timeout of waiting
        :param msg: message
        """

        assert self.is_element_visible(locator, timeout), \
        msg if msg else f'Element with locator {locator} should be visible, but it is invisible'

    def should_be_present(self, locator: tuple[str, str], timeout: float = 2, msg: str = ""):
        """
        Checks that the element is present

        :param locator: tuple of search strategy and selector
        :param timeout: timeout of waiting
        :param msg: message
        """

        assert self.is_element_present(locator, timeout), \
        msg if msg else f'Element with locator {locator} should be presented, but it is not'

    def should_be_checked(self, element: WebElement, input_inside: bool = False, msg: str = ''):
        """
        Checks the input is checked

        :param element: WebElement
        :param input_inside: should we look for input inside the element?
        :param msg: message
        """

        if input_inside:
            input_elm = self.get_element_from_element(element, (By.TAG_NAME, 'input'))
        else:
            input_elm = element
        assert input_elm.get_attribute('checked'), \
            msg if msg else "Input isn't checked"

    def should_not_be_disabled(self, element: WebElement, msg: str = ''):
        """
        Checks the element is not disabled

        :param element: WebElement
        :param msg: message
        """

        assert not element.get_attribute('disabled'), \
            msg if msg else "The element is disabled, but shouldn't"

    def scroll_into_view(self, locator: tuple[str, str]):
        """
        Scrolls element into view

        :param locator: tuple of search strategy and selector
        """

        self.should_be_present(locator)
        element = self.get_element(locator)
        self.browser.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -100);", element)
