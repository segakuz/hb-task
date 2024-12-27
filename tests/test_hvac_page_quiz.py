from pages.hvac_page import HvacPage
from pages.we_are_sorry_page import WeAreSorryPage
from pages.links.links import HvacPageLinks
from utils.functions import generate_email, generate_name, generate_phone_number


class TestHvacPageQuiz:
    """
    Tests quiz on the HVAC page
    """

    url = HvacPageLinks.url
    zip_code = '10001'
    email = generate_email()
    name = generate_name()
    phone_number = generate_phone_number()

    def test_01_pass_quiz_without_energy_source_step(self, browser):
        """
        Tests hvac page quiz with only first answers, without the energy source step
        """

        type_of_project = 'Replacement/installation'
        involved_equipment = 'Air conditioner'
        equipment_age = 'Less than 5years'
        type_of_property = 'Detached, semi-detached, row house'
        house_area = 188
        homeowner = True

        print('Open HVAC page')
        hvac_page = HvacPage(browser, self.url)
        hvac_page.open()

        print('Fill in zip code')
        hvac_page.fill_in_zip_input(self.zip_code)
        hvac_page.confirm_zip()

        print('Select type of project')
        hvac_page.select_type_of_project(type_of_project)
        hvac_page.click_button('next')

        print('Select involved equipment')
        hvac_page.select_involved_equipment(involved_equipment)
        hvac_page.click_button('next')

        print('Select equipment age')
        hvac_page.select_equipment_age(equipment_age)
        hvac_page.click_button('next')

        print('Select type of property')
        hvac_page.select_type_of_property(type_of_property)
        hvac_page.click_button('next')

        print('Fill in house area')
        hvac_page.set_house_area(house_area)
        hvac_page.click_button('next')

        print('Select whether you are a homeowner')
        hvac_page.select_homeowner_or_not(homeowner=homeowner)
        hvac_page.click_button('next')

        print('Fill in name and email')
        hvac_page.fill_in_name_and_email(self.name, self.email)
        hvac_page.click_button('next')

        print('Fill in phone number')
        hvac_page.fill_in_phone_number(self.phone_number)
        hvac_page.click_button('submit')

        print('Should be "We are sorry" page')
        we_are_sorry_page = WeAreSorryPage(browser, browser.current_url)
        we_are_sorry_page.check_page_title(timeout=30)

    def test_02_pass_quiz_with_multiple_equipment(self, browser):
        """
        Tests hvac page quiz with energy source, multiple equipment
        """

        input_location = 'middle'
        type_of_project = 'Replacement/installation'
        involved_equipment = ['Air conditioner', 'Water heater', 'Heat pump']
        energy_source = 'Electricity'
        equipment_age = '5 to 10years'
        type_of_property = 'Mobile, modular, manufactured home'
        house_area = 40
        homeowner = True

        print('Open HVAC page')
        hvac_page = HvacPage(browser, self.url)
        hvac_page.open()

        print('Fill in zip code')
        hvac_page.fill_in_zip_input(self.zip_code, location=input_location)
        hvac_page.confirm_zip(location=input_location)

        print('Select type of project')
        hvac_page.select_type_of_project(type_of_project)
        hvac_page.click_button('next')

        print('Select involved equipment')
        hvac_page.select_involved_equipment(involved_equipment)
        hvac_page.click_button('next')

        print('Select energy source')
        hvac_page.select_energy_source(energy_source)
        hvac_page.click_button('next')

        print('Select equipment age')
        hvac_page.select_equipment_age(equipment_age)
        hvac_page.click_button('next')

        print('Select type of property')
        hvac_page.select_type_of_property(type_of_property)
        hvac_page.click_button('next')

        print('Fill in house area')
        hvac_page.set_house_area(house_area)
        hvac_page.click_button('next')

        print('Select whether you are a homeowner')
        hvac_page.select_homeowner_or_not(homeowner=homeowner)
        hvac_page.click_button('next')

        print('Fill in name and email')
        hvac_page.fill_in_name_and_email(self.name, self.email)
        hvac_page.click_button('next')

        print('Fill in phone number')
        hvac_page.fill_in_phone_number(self.phone_number)
        hvac_page.click_button('submit')

        print('Should be "We are sorry" page')
        we_are_sorry_page = WeAreSorryPage(browser, browser.current_url)
        we_are_sorry_page.check_page_title(timeout=30)

    def test_03_pass_quiz_not_sure_answers(self, browser):
        """
        Tests hvac page quiz with not sure answers
        """

        type_of_project = 'Not sure'
        involved_equipment = 'Not sure'
        energy_source = 'Not sure'
        equipment_age = 'Not sure'
        type_of_property = 'Commercial'
        house_area = ''
        not_sure = True
        homeowner = True

        print('Open HVAC page')
        hvac_page = HvacPage(browser, self.url)
        hvac_page.open()

        print('Fill in zip code')
        hvac_page.fill_in_zip_input(self.zip_code)
        hvac_page.confirm_zip()

        print('Select type of project')
        hvac_page.select_type_of_project(type_of_project)
        hvac_page.click_button('next')

        print('Select involved equipment')
        hvac_page.select_involved_equipment(involved_equipment)
        hvac_page.click_button('next')

        print('Select energy source')
        hvac_page.select_energy_source(energy_source)
        hvac_page.click_button('next')

        print('Select equipment age')
        hvac_page.select_equipment_age(equipment_age)
        hvac_page.click_button('next')

        print('Select type of property')
        hvac_page.select_type_of_property(type_of_property)
        hvac_page.click_button('yes')

        print('Fill in house area')
        hvac_page.set_house_area(house_area, not_sure=not_sure)
        hvac_page.click_button('next')

        print('Select whether you are a homeowner')
        hvac_page.select_homeowner_or_not(homeowner=homeowner)
        hvac_page.click_button('next')

        print('Fill in name and email')
        hvac_page.fill_in_name_and_email(self.name, self.email)
        hvac_page.click_button('next')

        print('Fill in phone number')
        hvac_page.fill_in_phone_number(self.phone_number)
        hvac_page.click_button('submit')

        print('Should be "We are sorry" page')
        we_are_sorry_page = WeAreSorryPage(browser, browser.current_url)
        we_are_sorry_page.check_page_title(timeout=30)

    def test_04_pass_quiz_with_warnings(self, browser):
        """
        Tests hvac page quiz with answers which show warnings
        """

        input_location = 'bottom'
        type_of_project = 'Repair'
        type_of_project_warning = ('Unfortunately, our contractors only do HVAC replacement. '
                                   'Would you still like to continue?')
        involved_equipment = 'Heat pump'
        energy_source = 'Gas'
        equipment_age = 'Older than 10years'
        type_of_property = 'Apartment buildingor condominium'
        type_of_property_warning = ('Our contractors only work with detached, semi-detached, row houses or mobile, '
                                    'modular and manufactured homes. Would you still like to continue?')
        house_area = 60
        homeowner = False
        homeowner_warning = ('Our contractors require the homeowner or someone authorized to make property changes '
                             'be present during the estimate. Would you like to continue?')

        print('Open HVAC page')
        hvac_page = HvacPage(browser, self.url)
        hvac_page.open()

        print('Fill in zip code')
        hvac_page.fill_in_zip_input(self.zip_code, location=input_location)
        hvac_page.confirm_zip(location=input_location)

        print('Select type of project')
        hvac_page.select_type_of_project(type_of_project)
        hvac_page.should_be_step_warning(type_of_project_warning)
        hvac_page.click_button('yes')

        print('Select involved equipment')
        hvac_page.select_involved_equipment(involved_equipment)
        hvac_page.click_button('next')

        print('Select energy source')
        hvac_page.select_energy_source(energy_source)
        hvac_page.click_button('next')

        print('Select equipment age')
        hvac_page.select_equipment_age(equipment_age)
        hvac_page.click_button('next')

        print('Select type of property')
        hvac_page.select_type_of_property(type_of_property)
        hvac_page.should_be_step_warning(type_of_property_warning)
        hvac_page.click_button('yes')

        print('Fill in house area')
        hvac_page.set_house_area(house_area)
        hvac_page.click_button('next')

        print('Select whether you are a homeowner')
        hvac_page.select_homeowner_or_not(homeowner=homeowner)
        hvac_page.should_be_step_warning(homeowner_warning)
        hvac_page.click_button('yes')

        print('Fill in name and email')
        hvac_page.fill_in_name_and_email(self.name, self.email)
        hvac_page.click_button('next')

        print('Fill in phone number')
        hvac_page.fill_in_phone_number(self.phone_number)
        hvac_page.click_button('submit')

        print('Should be "We are sorry" page')
        we_are_sorry_page = WeAreSorryPage(browser, browser.current_url)
        we_are_sorry_page.check_page_title(timeout=30)
