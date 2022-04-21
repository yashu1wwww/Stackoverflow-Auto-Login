from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stackoverflow.com/users/login")

input=driver.find_element_by_xpath('//*[@id="email"]')
input.send_keys('virat6670@gmail.com')

input=driver.find_element_by_xpath('//*[@id="password"]')
input.send_keys('viratkohli')

input=driver.find_element_by_xpath('//*[@id="submit-button"]')
input.click()
