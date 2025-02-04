from selenium.webdriver.common.by import By


class BaseProjectPageLocators:
    """
    Locators for base project page
    """
    zip_input_header = (By.CSS_SELECTOR, '#zipCode')
    zip_input_middle = (By.CSS_SELECTOR, '#zip_content1')
    zip_input_bottom = (By.CSS_SELECTOR, '#zip_footer1')
    confirm_zip_top = (By.CSS_SELECTOR, '.ga-zip-confirm-top')
    confirm_zip_middle = (By.CSS_SELECTOR, '.ga-zip-confirm-middle')
    confirm_zip_bottom = (By.CSS_SELECTOR, '.ga-zip-confirm-bottom')


class BaseComponentLocators:
    """
    Common locators for base component
    """
    step_warning = (By.CSS_SELECTOR, '#StepBodyId [class*="text-orangeDeep"]')
    next_button = (By.CSS_SELECTOR, '[data-autotest-next]')
    yes_button = (By.CSS_SELECTOR, '[data-autotest-yes]')
    no_button = (By.CSS_SELECTOR, '[data-autotest-no]')
    submit_request_button = (By.CSS_SELECTOR, '[data-autotest-submit-my-request]')


class HvacPageLocators:
    """
    Locators for HVAC page
    """
    types_of_project = (By.CSS_SELECTOR, '.typesOfProject .typeOfProject__item')
    involved_equipments = (By.CSS_SELECTOR, '.involvedEquipment .involvedEquipment__item')
    energy_sources = (By.CSS_SELECTOR, '.energySource .energySource__item')
    equipment_ages = (By.CSS_SELECTOR, '.equipmentAge .equipmentAge__item')
    types_of_property = (By.CSS_SELECTOR, '.typeOfProperty .typeOfProperty__item')

    square_feet_input = (By.CSS_SELECTOR, '#squareFeet')
    not_sure_checkbox = (By.CSS_SELECTOR, '[data-autotest-notsure]')
    not_sure_label = (By.CSS_SELECTOR, '[data-autotest-notsure] + label')

    homeowner_yes_input = (By.CSS_SELECTOR, '[data-autotest-owner-yes]')
    homeowner_yes_label = (By.CSS_SELECTOR, '[data-autotest-owner-yes] + label')
    homeowner_no_input = (By.CSS_SELECTOR, '[data-autotest-owner-no]')
    homeowner_no_label = (By.CSS_SELECTOR, '[data-autotest-owner-no] + label')

    name_input = (By.CSS_SELECTOR, '[data-autotest-fullname-text]')
    email_input = (By.CSS_SELECTOR, '[data-autotest-email-email]')
    phone_number_input = (By.CSS_SELECTOR, '[data-autotest-phonenumber-tel]')


class WeAreSorryPageLocators:
    """
    Locators for We are sorry page
    """
    title = (By.CSS_SELECTOR, '.weAreSorry__title')
