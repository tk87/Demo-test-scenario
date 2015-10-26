from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()
driver.get ("http://demo.opencart.com")


Currency = driver.find_element_by_id ("currency").click()
GBP = driver.find_element_by_name ("GBP").click()
Ipod_search = driver.find_element_by_name ("search").send_keys("Ipod")
driver.find_element_by_xpath(".//*[@id='search']/span/button").click()

Compare1 = driver.find_element_by_xpath (".//*[@id='content']/div[4]/div[1]/div/div[3]/button[3]").click()
Compare2 = driver.find_element_by_xpath (".//*[@id='content']/div[4]/div[2]/div/div[3]/button[3]").click()
Compare3 = driver.find_element_by_xpath (".//*[@id='content']/div[4]/div[3]/div/div[3]/button[3]").click()
Comapre4 = driver.find_element_by_xpath (".//*[@id='content']/div[4]/div[4]/div/div[3]/button[3]").click()

Compare_all = driver.find_element_by_id ("compare-total").click()

Remove_out_of_stock = driver.find_element_by_xpath (".//*[@id='content']/table/tbody[2]/tr/td[2]/a").click()
driver.implicitly_wait(10)

Add_to_cart = driver.find_element_by_xpath (".//*[@id='content']/table/tbody[2]/tr/td[4]/input").click()

Cart_menu = driver.find_element_by_xpath (".//*[@id='top-links']/ul/li[4]/a/i").click()
