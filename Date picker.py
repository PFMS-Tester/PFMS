from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select

# Set up the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
# Open a specific URL
driver.get("https://demoqa.com/automation-practice-form")
#time.sleep(5)
actions = ActionChains(driver)
actions.scroll_by_amount(0,300).perform()
time.sleep(5)
# On finding and clicking any button on the page
driver.find_element(By.ID, "dateOfBirthInput").click()
'''datefield = driver.find_element(By.ID, "dateOfBirthInput")
datefield.send_keys(Keys.CONTROL, "a") # Select all pre-existing text/input value
datefield.send_keys(Keys.BACKSPACE)    # Remove that text
datefield.send_keys("01012011")
ActionChains(driver).move_to_element(datefield).click().send_keys('30081986').perform()
time.sleep(10)'''

month = driver.find_element(By.XPATH, "//div[@class='react-datepicker__month-dropdown-container react-datepicker__month-dropdown-container--select']/select")
option = Select(month)
option.select_by_value("4")
time.sleep(2)
year = driver.find_element(By.XPATH, "//div[@class='react-datepicker__year-dropdown-container react-datepicker__year-dropdown-container--select']/select")
option2 = Select(year)
option2.select_by_value("2029")
time.sleep(2)
date = driver.find_element(By.XPATH, "//following::div[@class='react-datepicker__month']/child::div[4]/child::div[2]").click()
time.sleep(2)

