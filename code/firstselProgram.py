import time
from selenium.webdriver.common.by import By
from selenium import webdriver


def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    get_title = driver.title
    print(get_title)
    # driver.find_element(By.ID, "btn-make-appointment").click()
    driver.find_element(By.CLASS_NAME, "btn btn-dark btn-lg")
    new_title = driver.title

    print(new_title)
    time.sleep(5)
