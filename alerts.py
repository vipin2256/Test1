from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


 
def test_google_search_page():
    driver = webdriver.Chrome(executable_path='C:\Python27\Scripts\chromedriver.exe')
    #driver.get("https://bobcares.com/")
    driver.get('https://s4.inhouse.net/')
    driver.implicitly_wait(30)
    driver.find_element_by_name("Login").click()
    #driver.switch_to_alert().accept()
    try:
        alert = driver.switch_to_alert()
        alert.accept()
        print "alert accepted"
    except:
        print "no alert"

test_google_search_page() 

