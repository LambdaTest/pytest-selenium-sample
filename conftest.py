from os import environ

import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver(request):
# parallize_test_accross_combinations
    desired_caps = {}
    browser = request.param

    desired_caps.update(browser)
    test_name = request.param["platform"] + "_" + request.param["browserName"] + "_" + request.param["version"]
    build = environ.get('BUILD', "Sample PY Build Chrome")

    tunnel_id = environ.get('TUNNEL', False)
    username = environ.get('LT_USERNAME', None)
    access_key = environ.get('LT_ACCESS_KEY', None)

    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    chrome_options = webdriver.ChromeOptions()
    option = {
        "platform": "Windows 10",
        "version": "latest",
        "name": test_name,
        "Build": build,
        "video": True,
        "visual": True,
        "network": True,
        "console": True
    }
    chrome_options.set_capability("LT:Options", option)
    browser = webdriver.Remote(
        command_executor=selenium_endpoint,
        options=chrome_options
    )
    yield browser

    def fin():
        # browser.execute_script("lambda-status=".format(str(not request.node.rep_call.failed if "passed" else
        # "failed").lower()))
        if request.node.rep_call.failed:
            browser.execute_script("lambda-status=failed")
            browser.quit()
        else:
            browser.execute_script("lambda-status=passed")
            browser.quit()

    request.addfinalizer(fin)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for LambdaTest reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
