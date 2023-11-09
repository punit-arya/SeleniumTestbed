import selenium
import selenium.webdriver.common.by as swcb

driver = selenium.webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
print("Title: ", driver.title)
# driver.implicitly_wait(50)
text_box = driver.find_element(by=swcb.By.NAME, value="my-text")
submit_button = driver.find_element(by=swcb.By.CSS_SELECTOR, value="button")
text_box.send_keys("Selenium")
submit_button.click()
message = driver.find_element(by = swcb.By.ID, value = "message")
text = message.text
driver.quit()
