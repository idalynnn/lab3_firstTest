import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    d = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    d.maximize_window()
    yield d
    d.quit()
