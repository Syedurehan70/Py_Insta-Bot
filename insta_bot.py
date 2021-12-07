import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class InstaFollower:
    def __init__(self, executable_path):
        # driver path
        self.chrome_driver_path = Service(executable_path)
        # driver object
        self.driver = webdriver.Chrome(service=self.chrome_driver_path)

    def login(self, username, password, page):
        # getting log in page
        self.driver.get(page)

        # catching username and password elements and putting I.D and pass in it
        time.sleep(3)
        user_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_input.send_keys(username)
        user_input.send_keys(Keys.ENTER)

        time.sleep(2)
        pass_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_input.send_keys(password)
        pass_input.send_keys(Keys.ENTER)

        # clicking not now for not saving login details
        time.sleep(3)
        not_now_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_button.click()

    def find_followers(self, account):
        # getting target profile page
        time.sleep(5)
        self.driver.get(account)

        # clicking on followers tab, to get the followers pop-up
        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]'
                                                       '/a')
        followers.click()

        # just like time sleep, here driver will wait for 2 sec, until expected condition (EC) which until element is
        # clickable is achieved it won't proceed further, xpath is the div containing list of all followers
        time.sleep(2)
        pop_up_window = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        "//div[@class='isgrP']")))

        # scrolling followers 10 times, (can be changed up to the need)
        for i in range(10):
            # what execute_script is doing it's executing a javascript in python file
            # now the modal (popup) which is pop_up_window in this program, the script is executed on it
            # in script modal is argument[0]
            # script is saying, scroll the top element of modal (argument[0]), by the height of modal in every loop
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up_window)
            time.sleep(5)

    def follow(self):
        # saving all follow buttons
        time.sleep(2)
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".isgrP button")

        # running loop to click them one by one
        for button in follow_buttons:
            try:
                button.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel_button.click()

            time.sleep(10)

        # closing window after operation finished
        self.driver.quit()
