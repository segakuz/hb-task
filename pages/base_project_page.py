from .locators.locators import BaseProjectPageLocators
from .locators.locators import BaseComponentLocators
from .base_page import BasePage
import time


class BaseProjectPage(BasePage):
    """
    Base page for project pages
    """

    def open(self):
        """
        Base method to open project page
        """

        super().open()
        self.should_be_zip_code_input()

    def get_zip_code_input_field_locator(self, location: str = 'top'):
        """
        Returns zip code input field locators by location

        :param location: location of the field (top, middle, bottom)
        :returns: tuple(locator)
        """

        match location:
            case 'top':
                return BaseProjectPageLocators.zip_input_header
            case 'middle':
                return BaseProjectPageLocators.zip_input_middle
            case 'bottom':
                return BaseProjectPageLocators.zip_input_bottom
            case _:
                raise ValueError('Incorrect location, acceptable values are: top, middle, bottom')

    def get_zip_confirm_button_locator(self, location: str = 'top'):
        """
        Returns zip confirm button locators by location

        :param location: location of the field (top, middle, bottom)
        :returns: tuple(locator)
        """

        match location:
            case 'top':
                return BaseProjectPageLocators.confirm_zip_top
            case 'middle':
                return BaseProjectPageLocators.confirm_zip_middle
            case 'bottom':
                return BaseProjectPageLocators.confirm_zip_bottom
            case _:
                raise ValueError('Incorrect location, acceptable values are: top, middle, bottom')

    def fill_in_zip_input(self, text: str|int, location: str = 'top'):
        """
        Fills in the input field

        :param text: text
        :param location: location of the field (top, middle, bottom)
        """

        locator = self.get_zip_code_input_field_locator(location)
        self.scroll_into_view(locator)
        zip_code_input = self.get_element(locator)
        zip_code_input.send_keys(text)
        self.should_contain_text_in_value(zip_code_input, text)

    def confirm_zip(self, location: str = 'top'):
        """
        Clicks the estimate button

        :param location: location of the button (top, middle, bottom)
        """

        self.should_be_visible_confirm_zip_button(location)
        confirm_button = self.get_element(self.get_zip_confirm_button_locator(location))
        confirm_button.click()

    def should_be_zip_code_input(self, location: str = 'top'):
        """
        Checks the appearance of the zip code input field

        :param location: location of the field (top, middle, bottom)
        """

        assert self.is_element_visible(self.get_zip_code_input_field_locator(location)), \
            f"ZIP code input field in the '{location}' is not visible"

    def should_be_visible_confirm_zip_button(self, location: str = 'top'):
        """
        Checks the appearance of the confirm zip top button

        :param location: location of the field (top, middle, bottom)
        """

        assert self.is_element_visible(self.get_zip_confirm_button_locator(location)), \
            f"Confirm ZIP button in the '{location}' is not visible"

    def click_button(self, button_name: str):
        """
        Clicks the specified button

        :param button_name: button name (next, yes, no, submit)
        """

        match button_name:
            case 'next':
                locator = BaseComponentLocators.next_button
            case 'yes':
                locator = BaseComponentLocators.yes_button
            case 'no':
                locator = BaseComponentLocators.no_button
            case 'submit':
                locator = BaseComponentLocators.submit_request_button
            case _:
                raise ValueError('Incorrect button, acceptable values are: next, yes, no, submit')

        self.should_be_visible(locator, msg=f"The '{button_name}' button is not visible")
        button = self.get_element(locator)
        self.should_not_be_disabled(button, msg=f"The '{button_name}' button is disabled, but shouldn't")
        button.click()

    def select_step_item(self, item_name: str, name_of_step: str, elements_locator: tuple[str, str]):
        """
        Selects the item in step

        :param item_name: name of the item
        :param name_of_step: name of the step
        :param elements_locator: locator of elements
        """

        time.sleep(0.5)
        items = self.get_elements(elements_locator)
        assert items, f"Didn't find any items in the '{name_of_step}' step"

        found_item = None
        for item in items:
            if item_name in item.text.replace('\n', ''):
                found_item = item
        assert found_item, f"Couldn't find any item by text '{item_name}'"

        self.should_be_clickable(found_item)
        found_item.click()
        self.should_be_checked(found_item, input_inside=True)

    def should_be_step_warning(self, text: str):
        """
        Checks that the step has warning

        :param text: text of warning
        """

        locator = BaseComponentLocators.step_warning
        self.should_be_visible(locator, msg="There is no warning in the step")
        warning = self.get_element(locator)
        self.should_contain_text(warning, text, msg=f"Step's warning hasn't text '{text}'")
