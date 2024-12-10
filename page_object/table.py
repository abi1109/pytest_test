from locators import table_locators


class TableVerification:

    def __init__(self, driver):
        self.driver = driver

    def launch_the_app(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        print("Table Verification Application is launched Successfully")

    def validate_table_elements(self):
        pass