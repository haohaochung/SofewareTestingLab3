import BasePage
import time


class FriendPage(BasePage.BasePage):

    def go_to_find_friend_page(self):
        self.driver.find_element_by_xpath('//*[@id="links"]/h5[6]/a').click()
        time.sleep(3)

    def go_to_friend_page(self):
        self.driver.find_element_by_xpath('//*[@id="links"]/h5[4]/a').click()
        time.sleep(3)

    def follow_friend(self):
        self.follower = self.driver.find_element_by_xpath('//*[@id="users"]/div[2]/div[1]/h5/a').text
        self.driver.find_element_by_xpath('//*[@id="users"]/div[2]/div[2]/div/div/form/button').click()

    def check_follow_friend(self):
        self.isFollowed = False
        for follow in self.driver.find_elements_by_xpath('//*[@id="friends"]//h5/a'):
            if follow.text == self.follower:
                self.isFollowed = True
                break
        return self.isFollowed

    def unfollow_friend(self):
        self.follower = self.driver.find_element_by_xpath('//*[@id="friends"]/div[1]/div[1]/h5/a').text
        self.driver.find_element_by_xpath('//*[@id="friends"]/div[1]/div[2]/div/div/form/button').click()
