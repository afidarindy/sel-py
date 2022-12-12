# First Test Scenario
# Scenario : Searching for Orchid Flower in Google
# Given I am in Google homepage
# When I search for "Orchid Flower"
# Then I should see search result of "Orchid Flower"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://google.co.id')
driver.find_element("name", "q").send_keys('Orchid Flower' + Keys.ENTER)

# check the result with this to get exact string in title
# assert 'Orchid Flower' == driver.title

# or this to get the string inside title
assert 'Orchid Flower' in driver.title

driver.quit()