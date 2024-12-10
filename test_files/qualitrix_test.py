import pytest
from page_object.qualitrix_home_page import QualitrixHomePage


@pytest.mark.usefixtures("browser_cbt")
class Test_Qualitrix_e2e:

    def test_homepage_validation(self, readJson):
        HomePage = QualitrixHomePage(self.driver)
        url = readJson['url_qualitrix']
        print(url)
        HomePage.launch_the_app(url)
        HomePage.Validate_header_menu()
        HomePage.validate_button_color()
