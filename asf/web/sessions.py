from selenium import webdriver

driver = webdriver.Chrome()
try:
    driver.get('https://the-internet.herokuapp.com/')
finally:
    driver.quit()