import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('driver')
class TestLink:

    def test_title(self, driver):
        """
        Verify click and title of page
        :return: None
        """
        driver.get('https://lambdatest.github.io/sample-todo-app/')
        driver.implicitly_wait(10)
        driver.find_element(By.NAME, "li1").click()
        driver.find_element(By.NAME, "li2").click()

        title = "Sample page - lambdatest.com"
        assert title == driver.title

    def test_item(self, driver):
        """
        Verify item submission
        :return: None
        """
        driver.get('https://lambdatest.github.io/sample-todo-app/')
        sample_text = "Happy Testing at LambdaTest"
        email_text_field = driver.find_element(By.ID, "sampletodotext")
        email_text_field.send_keys(sample_text)

        driver.find_element(By.ID, "addbutton").click()

        li6 = driver.find_element(By.CSS_SELECTOR, "input[name='li6'] + span").text
        assert sample_text == li6
