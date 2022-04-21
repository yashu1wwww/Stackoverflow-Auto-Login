from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stackoverflow.com/users/login")

input=driver.find_element_by_xpath('//*[@id="email"]')
input.send_keys('yashwanth6675@gmail.com')

input=driver.find_element_by_xpath('//*[@id="password"]')
input.send_keys('Yash2@#$%')

input=driver.find_element_by_xpath('//*[@id="submit-button"]')
input.click()


