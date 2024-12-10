import pytest
from page_object.table import TableVerification


@pytest.mark.usefixtures("browser_cbt")
class Test_Table:

    def test_table(self, readJson):
        Table_Verification = TableVerification(self.driver)
        Table_Verification.launch_the_app(readJson['url_table'])
        Table_Verification.validate_table_elements()
