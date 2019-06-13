from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys

repository_name = sys.argv[1]

driver = webdriver.Firefox()
driver.get("https://github.com/login")
login_element = driver.find_element_by_id("login_field")
password_element = driver.find_element_by_id("password")
login_button = driver.find_element_by_name("commit")

login_element.send_keys("User-Name") #Enter your Username Here
password_element.send_keys("Password") #Enter your Password Here
login_button.click()

driver.get("https://github.com/new")

repository_name_element = driver.find_element_by_id("repository_name")
repository_name_element.send_keys(repository_name)
time.sleep(2)

create_repo_button = driver.find_element_by_css_selector("button.btn:nth-child(10)")
create_repo_button.click()
time.sleep(5)

driver.close()
