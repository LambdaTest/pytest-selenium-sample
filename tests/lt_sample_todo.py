import json
import os
import pathlib

import pytest
from selenium.webdriver.common.by import By
import sys


class TestLinkChrome:
    def load_params_from_json(json_path):
        with open(json_path) as f:
            return json.load(f)

    @pytest.mark.parametrize("driver", load_params_from_json(str(pathlib.Path(__file__).parent.parent) + "/configurations.json"), indirect=True)
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

    @pytest.mark.parametrize("driver", load_params_from_json(str(pathlib.Path(__file__).parent.parent) + "/configurations.json"), indirect=True)
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

        li6 = driver.find_elements(By.CSS_SELECTOR, "[class='list-unstyled'] li")
        assert sample_text in str(li6[5].text)
