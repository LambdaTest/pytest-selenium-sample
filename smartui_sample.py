import os
import pytest
from selenium import webdriver
from os import environ
@pytest.fixture(scope='function')
def driver(request):
    test_name = request.node.name
    build = os.environ.get('BUILD', "Sample PYTEST Build")
    tunnel_id = os.environ.get('TUNNEL', False)
    username = environ.get('LT_USERNAME', None)
    access_key = environ.get('LT_ACCESS_KEY', None)

    selenium_endpoint = f"http://{username}:{access_key}@hub.lambdatest.com/wd/hub"
    chrome_options = webdriver.ChromeOptions()
    option = {
        "platform": "Windows 10",
        "version": "latest",
        "name": test_name,
        "build": build,
        "video": True,
        "visual": True,
        "network": True,
        "console": True,
        "smartUI.project": "Pytest-Sample",
        "selenium_version": "4.0.0"
    }
    chrome_options.set_capability("LT:Options", option)
    browser = webdriver.Remote(
        command_executor=selenium_endpoint,
        options=chrome_options
    )
    yield browser
    browser.quit()

def test_demo_site(driver):
    try:
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        print('Loading URL')
        driver.get("https://www.amazon.com/")
        driver.execute_script('smartui.takeScreenshot="Viewport Screenshot"')
        print("1st screenshot")
        driver.implicitly_wait(10)
        driver.execute_script('smartui.takeFullPageScreenshot="FullPage Screenshot"')
        print("2nd screenshot")
    except Exception as e:
        pytest.fail(f"Test failed: {str(e) if str(e) else 'Unknown error'}")
