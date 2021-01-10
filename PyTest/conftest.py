import pytest
from selenium import webdriver

def pytest_addoption(parser):
        parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "opera":
        _driver = webdriver.Opera(executable_path="/home/taghreed/Downloads/operadriver_linux64/operadriver")

    elif browser_name == "firefox":
        _driver = webdriver.Firefox(executable_path="/home/taghreed/Downloads/geckodriver-v0.28.0-linux64/geckodriver")

    elif browser_name == "chrome":
        _driver = webdriver.Chrome(executable_path="/home/taghreed/Downloads/chromedriver_linux64/chromedriver")

    _driver.maximize_window()
    _driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls._driver = _driver

    yield
    _driver.save_screenshot("/home/taghreed/PycharmProjects/PageObjectModelTesting/Screenshots/final.png")
    _driver.close()
