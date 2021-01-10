import pytest
from selenium.webdriver.support.select import Select

from TestData.HomeTestData import TestData


@pytest.mark.usefixtures("setup")
class BaseClass:
    dataobj = TestData()
    dynamicTestData = dataobj.getTestData()


    @pytest.fixture(params= dynamicTestData)
    def setData(self,request):
        return request.param

    def setGender(self, gender, locator):
        select_gender = Select(locator)
        select_gender.select_by_visible_text(gender)

    #def takeScreenShot(self):


