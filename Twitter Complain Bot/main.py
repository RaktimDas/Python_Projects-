from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
DOWNLOAD_SPEED = 15
UPLOAD_SPEED = 10
TWITTER_EMAIL = "gamerfunky619@gmail.com"
PASSWORD = "gamerrd9854"
PHONE = "8638194454"
chrome_driver_path = "J:\chromedriver_win32/chromedriver"
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/?lang=en"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.download = 0
        self.upload = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        sleep(3)
        go_button = self.driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go_button.click()
        sleep(60)
        self.download = self.driver.find_element_by_class_name(
            "download-speed")
        sleep(6)
        print(f"The Download Speed is {self.download.text} Mbps.")
        sleep(6)
        self.upload = self.driver.find_element_by_class_name(
            "upload-speed")
        sleep(6)
        print(f"The Upload Speed is {self.upload.text} Mbps.")

    def tweet_at_provider(self):
        # if (self.download.text) < DOWNLOAD_SPEED and (self.upload.text) < UPLOAD_SPEED:
        self.driver.get(TWITTER_URL)
        sleep(3)
        sign_in = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span")
        sign_in.click()
        login = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span')
        login.click()
        sleep(6)
        email = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(PHONE)
        email.send_keys(Keys.ENTER)
        sleep(3)
        verification = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        verification.send_keys(TWITTER_EMAIL)
        verification.send_keys(Keys.ENTER)
        sleep(3)
        password = self.driver.find_element_by_name(
            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input')
        password.send_keys(PASSWORD)
        sleep(3)
        password.send_keys(Keys.ENTER)
        sleep(6)
        my_tweet = f"Hey Internet Provider @jio, why is my internet speed slow {self.download.text}download/{self.upload.text}upload, when I pay for {DOWNLOAD_SPEED}download speed/{UPLOAD_SPEED}upload speed?"
        write_tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div['
            '2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div['
            '1]/div/div/div/div[2]/div/div/div/div')
        write_tweet.send_keys(my_tweet)
        sleep(3)
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
            '2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div['
            '3]/div')
        tweet_button.click()
        sleep(10)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
