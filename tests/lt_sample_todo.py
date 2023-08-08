import pytest
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.common.action_chains import ActionChains



@pytest.mark.usefixtures('driver')
class TestLink:

    def test_title(self, driver):
        
        driver.get(r'https://www.lambdatest.com/selenium-playground/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//a[contains(text(),'Simple Form Demo')]").click()
        title = driver.driver.current_url
        assert “simple-form-demo” in title, "tetx is not present n the URL"
        val = “Welcome to LambdaTest”
        driver.find_element(By.XPATH, "//input[@id='user-message']").send_keys(val)
        driver.find_element(By.ID, "#showInput").click()
        text = driver.find_element(By.CSS_SELECTOR, '#message').text
        assert text == val
       

    def test_item(self, driver):
        """
        Verify item submission
        :return: None
        """
        
        driver.get('https://www.lambdatest.com/selenium-playground/')
        driver.find_element(By.XPATH,"//a[contains(text(),'Drag & Drop Sliders')]").click()
        time.sleep(2)
        ActionChains(driver).move_by_offset(946, 349).pause(2).click().perform()
        exp_val= '95'
        obtained_val = driver.find_element(By.ID,"rangeSuccess").text
        assertEqual(exp_val, obtained_val, "Value is not equal to 95")

      
