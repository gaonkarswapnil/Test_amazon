import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    # print("open")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.com/")
    request.cls.driver = driver
    yield
    driver.close()
    # print("close")

