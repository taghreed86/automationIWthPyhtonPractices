import pytest
import time

from Utility.BaseClass import BaseClass
from Utility.Pages.SubmitFormPage import SubmitForm
from selenium.webdriver.support.select import Select


class TestSubmitForm(BaseClass):
    def test_formSubmition(self,setData):
        submit = SubmitForm(self._driver)
        submit.getName().send_keys(setData["firstname"])
        submit.getEmail().send_keys(setData["email"])
        submit.getPassword().send_keys(setData["password"])
        submit.getIceCreamCheckBox().click()
        self.setGender(setData["gender"], submit.getGenderList())
        submit.getEmploymentStatus().click()
        submit.getSubmitBtn().click()
        successTxt = submit.getSuccessMsg().text
        assert "Success!" in successTxt
        time.sleep(4)
        self._driver.refresh()




