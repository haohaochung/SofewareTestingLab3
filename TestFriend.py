import unittest
import LoginPage
import FriendPage
from selenium import webdriver


class TestFriend(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://140.124.183.106:3000/")
        LoginPage.LoginPage(self.driver).socify_login()
        self.friend = FriendPage.FriendPage(self.driver)

    def test_1_follow_friend(self):
        self.friend.go_to_find_friend_page()
        self.friend.follow_friend()
        self.friend.go_to_friend_page()
        self.assertTrue(self.friend.check_follow_friend())

    def test_2_unfollow_friend(self):
        self.friend.go_to_friend_page()
        self.friend.unfollow_friend()
        self.friend.go_to_friend_page()
        self.assertFalse(self.friend.check_follow_friend())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()