from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

FB_EMAIL = ""
FB_PASSWORD = ""

chrome_driver_path = "J:\chromedriver_win32/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element_by_xpath(
    '//*[@id="o771500765"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]')
login_button.click()

sleep(2)
fb_login = driver.find_element_by_xpath(
    '//*[@id="o-1268705039"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
fb_login.click()

# Switch to Facebook login window
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Login and hit enter
email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)
