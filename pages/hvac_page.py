from .base_project_page import BaseProjectPage
from .locators.locators import HvacPageLocators


class HvacPage(BaseProjectPage):
    """
    HVAC Page
    """

    def select_type_of_project(self, type_name: str):
        """
        Selects the type of project

        :param type_name: name of the type
        """

        self.select_step_item(type_name, 'Types of project', HvacPageLocators.types_of_project)

    def select_involved_equipment(self, equipment_name: str|list):
        """
        Selects the involved equipment

        :param equipment_name: name of the equipment or list of names
        """

        if isinstance(equipment_name, list):
            for equipment in equipment_name:
                self.select_step_item(equipment, 'Involved equipment', HvacPageLocators.involved_equipments)
        else:
            self.select_step_item(equipment_name, 'Involved equipment', HvacPageLocators.involved_equipments)

    def select_energy_source(self, source_name: str):
        """
        Selects the energy source

        :param source_name: name of the equipment
        """

        self.select_step_item(source_name, 'Energy source', HvacPageLocators.energy_sources)

    def select_equipment_age(self, age: str):
        """
        Selects the equipment age

        :param age: age of the equipment
        """

        self.select_step_item(age, 'Equipment age', HvacPageLocators.equipment_ages)

    def select_type_of_property(self, type_name: str):
        """
        Selects the type of property

        :param type_name: name of the equipment
        """

        self.select_step_item(type_name, 'Type of property', HvacPageLocators.types_of_property)

    def set_house_area(self, square_feet: int|str = '', not_sure: bool = False):
        """
        Sets the house area

        :param square_feet: the number of square feet
        :param not_sure: set not sure checkbox
        """

        assert not square_feet or not not_sure, 'You should pass at least one truthy argument'

        if square_feet:
            area_input = self.get_element(HvacPageLocators.square_feet_input)
            area_input.send_keys(square_feet)
            self.should_contain_text_in_value(area_input, str(square_feet))
        elif not square_feet or not_sure:
            not_sure_label = self.get_element(HvacPageLocators.not_sure_label)
            not_sure_label.click()
            not_sure = self.get_element(HvacPageLocators.not_sure_checkbox)
            self.should_be_checked(not_sure)

    def select_homeowner_or_not(self, homeowner: bool):
        """
        Selects whether you are a homeowner

        :param homeowner: True or False
        """

        if homeowner:
            yes_label = self.get_element(HvacPageLocators.homeowner_yes_label)
            yes_label.click()
            yes_input = self.get_element(HvacPageLocators.homeowner_yes_input)
            self.should_be_checked(yes_input)
        else:
            no_label = self.get_element(HvacPageLocators.homeowner_no_label)
            no_label.click()
            no_input = self.get_element(HvacPageLocators.homeowner_no_input)
            self.should_be_checked(no_input)

    def fill_in_name_and_email(self, name: str, email: str):
        """
        Fills in name and email

        :param name: name
        :param email: email
        """

        name_input = self.get_element(HvacPageLocators.name_input)
        name_input.send_keys(name)
        self.should_contain_text_in_value(name_input, name)

        email_input = self.get_element(HvacPageLocators.email_input)
        email_input.send_keys(email)
        self.should_contain_text_in_value(email_input, email)

    def fill_in_phone_number(self, phone_number: str):
        """
        Fills in phone number

        :param phone_number: phone number (10 digits)
        """

        assert len(phone_number) == 10, "The length of the phone number must be 10 digits"

        phone_number_input = self.get_element(HvacPageLocators.phone_number_input)
        phone_number_input.click()
        phone_number_input.send_keys(phone_number)

        formatted_phone = f"+1({phone_number[0:3]}){phone_number[3:6]}-{phone_number[6:10]}"
        self.should_contain_text_in_value(phone_number_input, formatted_phone)
