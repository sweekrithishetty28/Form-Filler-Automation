from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

wait=WebDriverWait(driver,10)

driver.find_element(By.ID,"firstName").send_keys("Sweekrithi")
driver.find_element(By.ID,"lastName").send_keys("Shetty")
driver.find_element(By.ID,"userEmail").send_keys("sweekrithishetty1@gmail.com")

gender=driver.find_element(By.XPATH,"//label[contains(text(),'Female')]")
gender.click()


driver.find_element(By.ID,"userNumber").send_keys("8971982621")

driver.find_element(By.ID,"dateOfBirthInput").click()

Select(driver.find_element(By.CLASS_NAME,"react-datepicker__month-select")).select_by_visible_text("August")

Select(driver.find_element(By.CLASS_NAME,"react-datepicker__year-select")).select_by_visible_text("2004")
driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day--028')]").click()

search_box=driver.find_element(By.ID,"subjectsInput")
search_box.send_keys("Computer Science")
search_box.send_keys(Keys.RETURN)

hobby=driver.find_element(By.XPATH,"//label[contains(text(),'Reading')]")
hobby.click()
hobby=driver.find_element(By.XPATH,"//label[contains(text(),'Music')]")
hobby.click()

upload=driver.find_element(By.ID,"uploadPicture")
upload.send_keys(r"C:\Users\Asus\Pictures\Screenshots\Screenshot (71).png")


driver.find_element(By.ID,"currentAddress").send_keys("Mangalore")

driver.execute_script("window.scrollBy(0, 300)")
state=driver.find_element(By.ID,"react-select-3-input")
state.send_keys("NCR")
state.send_keys(Keys.RETURN)


city=driver.find_element(By.ID,"react-select-4-input")
city.send_keys("Delhi")
city.send_keys(Keys.RETURN)

driver.find_element(By.ID, "submit").click()
time.sleep(2)
driver.save_screenshot("form_submission.png")

time.sleep(5)
driver.quit()
