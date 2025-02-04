import pytest
from pages.hvac_page import HvacPage
from pages.links.links import HvacPageLinks


@pytest.mark.smoke
class TestHvacPageQuiz:
    """
    Smoke tests for the HVAC page
    """

    url = HvacPageLinks.url
    zip_code = '10001'

    @pytest.mark.parametrize("input_location", (
        "top", "middle", "bottom"
    ))
    def test_01_get_quiz(self, browser, input_location):
        """
        Checks that after we enter a zip code we will go to the quiz
        """
        type_of_project = 'Replacement/installation'

        print('Open HVAC page')
        hvac_page = HvacPage(browser, self.url)
        hvac_page.open()

        print('Fill in zip code')
        hvac_page.fill_in_zip_input(self.zip_code, location=input_location)
        hvac_page.confirm_zip(location=input_location)

        print("Should be quiz")
        hvac_page.select_type_of_project(type_of_project)
