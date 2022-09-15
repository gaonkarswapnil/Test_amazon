import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestAmazon:
    def test(self):
        # For Search Box and Search Button
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Chair")
        self.driver.find_element(By.ID, "nav-search-submit-button").click()

        # For opening File
        self.driver.find_element(By.CSS_SELECTOR, "h2").click()

        # For taking the product name and print it
        product_name = self.driver.find_element(By.ID, "title").text
        print(product_name)
