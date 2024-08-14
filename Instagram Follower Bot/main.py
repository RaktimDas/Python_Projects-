"""
FOR ALL OF THIS TO WORK YOU NEED TO INSTALL CHROMEDRIVER AND USE IT'S PATH HERE.

IT IS TO KEEP IN MIND  THAT THE CLASSES AND THE PATHS USED HERE MIGHT CHANGE IN THE TARGET PAGE OR MIGHT NOT 
AND FOR THE XPATH AND REST TO WORK KEEP THE WINDOW TO MAXIMIZE THE (CODE IS INCLUDED), SO TRY THE CLASSES AND PATHS DIRECTLY FROM THERE
AND EXPERIENCE YOURSELF.

THE MAIN PART IS THE DON'T USE YOUR MAIN INSTAGRAM ACCOUNT CREATE A DUMMY(FOR PRACTICE) AND USE IT. YOU CAN USE IT ONCE , 
WHEN THE WHOLE PROGRAM WORKS AND THE BOT STATRS FOLLOWING THE FOLLOWERS THEN THE CODE WORKS AND YOU ARE SUCCESSFULL AND IF 
YOU WANT TO TRY AGAIN YOU HAVE TO CREATE A ANOTHER DUMMY ACCOUNT CAUSE THE FIRST ONE WILL BE CARTEGORISED AS BOT BY INSTAGRAM AND
YOU WON'T BE ABLE TO USE THAT FOR THE SAME.

GOOD LUCK CODING.
"""
# IMPORTING THE REQUIRED MODULES
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
chrome_driver_path = "INSERT YOUR CHROMEDRIVER PATH"
USER = "ENTER YOUR INSTAGRAM USERNAME OR EMAIL"
PASSWORD = "ENTER YOUR INSTAGRAM PASSWORD"
SIMILAR_ACCOUNT_URL = "https://www.instagram.com/ENTER THE NAME OF THE TARGETED ACCOUNT HERE/"
INSTAGRAM_URL = "https://www.instagram.com/"
# USING THE TIME MODULE TO PUT DELAY BETWEEN THE INTERVAL
# CLREATING A CLASS CALLED INSTAFOLLOWER


class InstaFollower:
    def __init__(self, path):
        # CHOOSING CHROME AS THE BROWER AND PUTTING THE PATH
        self.driver = webdriver.Chrome(executable_path=path)
        # MAXIMIZING THE AUTOMATION WINDOW
        self.driver.maximize_window()
    # INITIALIZING THE LOGIN FUNCTION THROUGH WHICH WE WILL LOG INTO INSTAGRAM USING THE URL THEN USERNAME AND PASSWORD

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        sleep(5)
        # SEARCHING FOR THE USERNAME
        email = self.driver.find_element_by_name("username")
        email.send_keys(USER)
        # SEARCHING FOR THE PASSWORD
        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)
        sleep(2)
        # CLICKING THE LOGIN  KEY
        password.send_keys(Keys.ENTER)
        sleep(5)
    # FINDING THE SIMILAR ACCOUNT FOLLOWERS AND PULLING THEM OUT

    def find_followers(self):
        # THE ACCOUNT URL
        self.driver.get(SIMILAR_ACCOUNT_URL)
        sleep(5)
        # THE FOLLOWERS LIST AFTER CLICKING THE FOLLOWER ICON
        followers_list = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        followers_list.click()
        sleep(10)
        # FOLLOWER WORD XPATH OR ITS HTML TREE
        modal = self.driver.find_element_by_xpath(
            "/html/body/div[6]/div/div/div[1]/div/h1")
        # THIS 3 LINES ARE USED FOR SCROLLING THE FOLLOWERS LIST THEY ARE BASICALLY JAVASCRIPT NOTATION
        # HERE ONLY 10 FOLLOWERS ARE TO BE FOLLOWED SO THE RANGE IS 10
        for i in range(5):
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollHeight', modal)
            sleep(2)
        # LAST STEP TO FOLLOW ALL THE FOLLOWERS OF THE SIMILAR ACCOUNT

    def follow(self):
        # FINDING THE CLASS OF THE LI OR DIV OF THE FOLLOW BUTTON
        follow = self.driver.find_elements_by_class_name("Pkbci")
        # ITERATING THROUGH ALL THE BUTTONS IN THE FOLLOW VARIABLE
        # USING EXCEPTION ERROR
        # IN THE TRY BLOCK THE BUTTON WILL CLICK ALL THE FOLLOW BUTTONS
        # IF THERE IS AN EXCEPTION AND THE OTHER USER IS ALREADY BEING FOLLOWED THEN THE EXCEPTION BLOCK WILL HANDLE THE ERROR RAISED
        for button in follow:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath(
                    "/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel_button.click()
                sleep(1)

            finally:
                sleep(1)
                print("The Automation was successful")
        else:
            print("The Program Crahsed.")


# LASTLY THE CLASS IS BEING CALLED AND THE FUNCTION INSIDE IT ARE BEING ACCESSED
insta_bot = InstaFollower(chrome_driver_path)
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
