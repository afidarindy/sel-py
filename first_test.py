# Before writing these scripts, make sure :
# 1. To have python installed
# 2. Download Chromedriver
# 3. Install selenium with "pip install selenium"
# 4. Install pytest with "pip install pytest"

# How to run :
# pytest file_name.py

# First Test Scenario
    # Scenario : Searching for Orchid Flower in Google
    # Given I am in Google homepage
    # When I search for "Orchid Flower"
    # Then I should see search result of "Orchid Flower"

# Second Test Scenario
    # Scenario : Searching for Afida Rindy in Google
    # Given I am in Google homepage
    # When I search for "Afida Rindy"
    # Then I should see search result of "Afida Rindy"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://google.co.id')
    yield driver
    driver.quit()

def test_googling(driver):
    driver.find_element("name", "q").send_keys('Orchid Flower' + Keys.ENTER)

    # check the result with this to get exact string in title
    # assert 'Orchid Flower' == driver.title

    # or this to get the string inside title
    assert 'Orchid Flower' in driver.title

def test_googling2(driver):
    driver.find_element("name", "q").send_keys('Afida Rindy' + Keys.ENTER)

    # check the result with this to get exact string in title
    # assert 'Orchid Flower' == driver.title

    # or this to get the string inside title
    assert 'Afida Rindy' in driver.title