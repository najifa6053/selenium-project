import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager    


def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


def fill_text_inputs(driver):
    driver.get("https://demoqa.com/text-box")
    name_text = driver.find_element(By.ID, "userName").send_keys("Najifa Alam Esha")
    time.sleep(1)
    email_text = driver.find_element(By.ID, "userEmail").send_keys("najifa@example.com")
    time.sleep(1)
    current_address = driver.find_element(By.ID, "currentAddress").send_keys("Dhaka, Bangladesh")
    permanent_address = driver.find_element(By.ID, "permanentAddress").send_keys("Dhaka, Bangladesh")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    output_name = driver.find_element(By.ID, "name")
    assert "Najifa Alam Esha" in output_name.text
    print("Text input test passed.")

def radio_button_test(driver):
    driver.get("https://demoqa.com/radio-button")
    yes_radio = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_radio.click()
    time.sleep(1)
    impressive_radio = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
    impressive_radio.click()
    time.sleep(1)
    no_radio = driver.find_element(By.XPATH, "//label[@for='noRadio']")
    no_radio.click() 
    time.sleep(1)

    output_yes = driver.find_element(By.XPATH, "//span[@class='text-success']")
    assert "Impressive" in output_yes.text


if __name__ == "__main__":
    driver = setup_driver()
    #fill_text_inputs(driver)
    radio_button_test(driver)