from insta_bot import InstaFollower

# necessary constants
PATH = "C:/Users/syed usama rehan/chromedriver_win32/chromedriver.exe"
log_in_page = "https://www.instagram.com/accounts/login/"
INSTA_USERNAME = "usamatest32"
INSTA_PASSWORD = "Angela$32"
SIMILAR_ACCOUNT = "https://www.instagram.com/sarahcruddastv/"

# class object
bot = InstaFollower(executable_path=PATH)

# logging in method
bot.login(username=INSTA_USERNAME, password=INSTA_PASSWORD, page=log_in_page)

# method of finding follower's pop-up
bot.find_followers(account=SIMILAR_ACCOUNT)

# method for following those followers
bot.follow()
