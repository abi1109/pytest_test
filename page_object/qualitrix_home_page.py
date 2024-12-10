from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from webcolors import hex_to_name
from locators import qualitrix_locators
from page_object import colors


class QualitrixHomePage:

    def __init__(self, driver):
        self.driver = driver

    def launch_the_app(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        print("Qualitrix Application is launched Successfully")

    def Validate_header_menu(self):
        assert len(self.driver.find_elements(By.XPATH, qualitrix_locators.Qualitrix_logo())) == 1
        assert self.driver.find_element(By.XPATH, qualitrix_locators.Qualitrix_logo()).is_displayed() == True
        print("Qualitrix logo is present")

    def validate_button_color(self):
        Get_a_quote = self.driver.find_element(By.XPATH, qualitrix_locators.get_a_quote())
        get_a_quote_color = Get_a_quote.value_of_css_property("color")
        get_a_quote_bg_color = Get_a_quote.value_of_css_property("background-color")
        print("Text color of the element : " + get_a_quote_color)
        print("Backgorund color of the element : " + get_a_quote_bg_color)

        # hex value of colors
        hex_element_color = Color.from_string(get_a_quote_color).hex
        hex_background_color = Color.from_string(get_a_quote_bg_color).hex
        print("Hex value of Element Color : " + hex_element_color)
        print("Hex value of Background Color : " + hex_background_color)

        # color name using library
        element_color_name = self.get_color_name(hex_element_color)
        print(element_color_name)
        background_color_name = self.get_color_name(hex_background_color)
        print(background_color_name)

        # color name predefined
        element_color_name = colors.find_color_name(hex_element_color)
        print(element_color_name)
        background_color_name = colors.find_color_name(hex_background_color)
        print(background_color_name)

        # get_css_properties
        start_up = self.driver.find_element(By.XPATH, qualitrix_locators.start_up())
        print(start_up.value_of_css_property("padding"))
        print(start_up.value_of_css_property("text-align"))

        # comapny elements
        Company = self.driver.find_element(By.XPATH, qualitrix_locators.company_name())
        element_padding = Company.value_of_css_property("padding")
        element_font_size = Company.value_of_css_property("font-size")
        print("Padding value : " + element_padding)
        print("Font Size : " + element_font_size)
        if element_padding == colors.css_parameters("padding"):
            print("Padding value of the element is as expected")
        else:
            assert False, "Padding value doesn't matches with the expected value"
        assert element_font_size == colors.css_parameters("font-size"), "Font Size of the element is not as expected"

    def get_color_name(self, color):
        try:
            color_name = hex_to_name(color)
            return color_name
        except ValueError:
            print("The hex value you provided couldn't be mapped with any known colors")
            return "Unknown Color"