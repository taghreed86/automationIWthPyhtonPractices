from selenium.webdriver.common.by import By

from Utility.BaseClass import BaseClass


class SubmitForm(BaseClass):
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    iceCreamCheckBox = (By.XPATH, "//label[@for='exampleCheck1']")
    genderList = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    employmentStatus = (By.ID, "inlineRadio2")
    submitBtn = (By.XPATH, "//input[@value='Submit']")
    successMsg = (By.XPATH , "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self, _driver):
        self.driver = _driver

    def getName(self):
        return self.driver.find_element(*SubmitForm.name)

    def getEmail(self):
        return self.driver.find_element(*SubmitForm.email)

    def getPassword(self):
        return self.driver.find_element(*SubmitForm.password)

    def getIceCreamCheckBox(self):
        return self.driver.find_element(*SubmitForm.iceCreamCheckBox)

    def getGenderList(self):
        return self.driver.find_element(*SubmitForm.genderList)

    def getEmploymentStatus(self):
        return self.driver.find_element(*SubmitForm.employmentStatus)

    def getSubmitBtn(self):
        return self.driver.find_element(*SubmitForm.submitBtn)

    def getSuccessMsg(self):
        return self.driver.find_element(*SubmitForm.successMsg)





