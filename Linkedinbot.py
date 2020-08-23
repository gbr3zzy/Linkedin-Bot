import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LinkedinBot:
    def __init__(self , username , password):
        self.driver = webdriver.Chrome()
        time.sleep(6)

        self.base_url = 'https://www.linkedin.com'
        self.login_url = self.base_url + '/login'
        self.feed_url = self.base_url + '/feed'

        self.username = username
        self.password = password

    def _nav(self , url):
        self.driver.get(url)
        time.sleep(6)

    def login(self , username , password):
        """ Login to LinkedIn account """
        self._nav(self.login_url)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()
        time.sleep(6)

    ##
    def search(self , text , connect=False):
        """ Search execeuted from home screen """

        search = self.driver.find_element_by_xpath('//*[@id="ember17"]/input')
        search.send_keys(text)
        search.send_keys(Keys.ENTER)

        # Waiting for search results to load
        time.sleep(4)

        if connect:
            self._search_connect()

    def _search_connect(self):
        """ Called after search method to send connections to all on page """

        connect = self.driver.find_element_by_class_name('search-result__action-button')
        connect.click()
        time.sleep(2)
        self.driver.find_element_by_class_name('ml1').click()


if __name__ == '__main__':
    username = ''
    password = ''
    text = ''
    search_text = ''

    bot = LinkedinBot("" , "")
    bot.login("" , "")
    bot.search('student')
    bot.search(search_text , connect=True)

