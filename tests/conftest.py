import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome, firefox, or all",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )


def pytest_generate_tests(metafunc):
    if "browser_name" in metafunc.fixturenames:
        browser_opt = metafunc.config.getoption("browser").lower()
        browsers = ["chrome", "firefox"] if browser_opt == "all" else [browser_opt]
        metafunc.parametrize("browser_name", browsers)


@pytest.fixture
def driver(browser_name, request):
    headless = request.config.getoption("headless")

    if browser_name == "chrome":
        options = ChromeOptions()
        # Matikan popup password leak detection Chrome agar tidak mengganggu test
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        }
        options.add_experimental_option("prefs", prefs)
        if headless:
            options.add_argument("--headless=new")
        web_driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        web_driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()