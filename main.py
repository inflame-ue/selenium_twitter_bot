# imports
from selenium import webdriver
import speedtest
import time

# constants
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = ""  # Your chrome driver path here
TWITTER_EMAIL = ""  # Your email for twitter
TWITTER_PASSWORD = ""  # Your password for twitter(you can use environmental variables)
URL = "https://twitter.com/home"


# class block
class InternetSpeedTwitterBot:
    """
    This is the class that creates a twitter bot.
    """

    def __init__(self):
        """Initialize the bot(selenium)"""
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        self.speed_test = speedtest.Speedtest()

    def get_internet_speed(self):
        print("Fetching speeds...")
        upload = round(self.speed_test.upload() / 1000000, 2)
        download = round(self.speed_test.download() / 1000000, 2)
        return [upload, download]

    def tweet_at_provider(self):
        # open twitter
        self.driver.get(URL)
        time.sleep(3)

        # log in
        self.driver.find_element_by_xpath("//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div["
                                          "2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input").send_keys(
            TWITTER_EMAIL)
        time.sleep(3)

        self.driver.find_element_by_xpath("//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div").click()
        time.sleep(3)

        self.driver.find_element_by_xpath("//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input").send_keys(TWITTER_PASSWORD)
        time.sleep(3)

        self.driver.find_element_by_xpath("//*[@id=\"layers\"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div").click()
        time.sleep(20)

        # tweet
        input = self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        input.click()
        input.send_keys(f"Hey Internet Provider, why is my internet speed {internet_speeds[1]}/{internet_speeds[0]} when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        time.sleep(3)

        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]").click()


# initialise the bot
bot = InternetSpeedTwitterBot()
internet_speeds = bot.get_internet_speed()

bot.tweet_at_provider()

