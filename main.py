from insta_bot import InstaFollower
import os

# necessary constants
PATH = os.environ.get("your_chrome_driver")
log_in_page = "https://www.instagram.com/accounts/login/"
INSTA_USERNAME = os.environ.get("username")
INSTA_PASSWORD = os.environ.get("password")
TARGET_ACCOUNT = os.environ.get("any_account_of_10K_followers")

# class object
bot = InstaFollower(executable_path=PATH)

# logging in method
bot.login(username=INSTA_USERNAME, password=INSTA_PASSWORD, page=log_in_page)

# method of finding follower's pop-up
bot.find_followers(account=TARGET_ACCOUNT)

# method for following those followers
bot.follow()
