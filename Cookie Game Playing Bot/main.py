from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "J:\chromedriver_win32/chromedriver"
URL = "http://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
cookie = driver.find_element_by_id("cookie")
items = driver.find_element_by_css_selector("#store div")
items_ids = [item.get_attribute for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:

        all_prices = driver.find_element_by_css_selector("#store b")
        items_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("_")[1].strip().replace(",", ""))
                items_prices.append(cost)
        cookie_upgrades = {}
        for n in range(len(items_prices)):
            cookie_upgrades[items_prices[n]] = items_ids[n]
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element_by_id(to_purchase_id).click()
        timeout = time.time() + 5
        if time.time() > five_min:
            cookie_per_sec = driver.find_element_by_id("cps").text
            print(cookie_per_sec)
            break
