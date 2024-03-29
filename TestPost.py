import unittest
import LoginPage
import PostPage
import BasePage
import time
from selenium import webdriver


class TestPost(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://140.124.183.106:3000/")
        LoginPage.LoginPage(self.driver).socify_login()
        self.post = PostPage.PostPage(self.driver)
        self.image = BasePage.BasePage.pict_location

    def test_1_create_post_1(self):
        self.post.create_post("I am happy", self.image+'\koala.jpg')
        self.assertEqual("I am happy", self.driver.find_element_by_xpath('//*/div[2]/span/p').text)
        assert "koala.jpg" in self.driver.find_element_by_xpath('//*/div[2]/div[1]/img').get_attribute("src")
        self.post.delete_post()

    def test_1_create_post_2(self):
        self.post.create_post("@@#$%", self.image + '\giphy.gif')
        self.assertEqual("@@#$%", self.driver.find_element_by_xpath('//*/div[2]/span/p').text)
        assert "giphy.gif" in self.driver.find_element_by_xpath('//*/div[2]/div[1]/img').get_attribute("src")
        self.post.delete_post()

    def test_1_create_post_3(self):
        self.post.create_post("", self.image + "\g.txt")
        time.sleep(2)
        assert "Content can't be blank" in self.driver.find_element_by_xpath('/html/body/div[1]').text

    def test_1_create_post_4(self):
        self.post.create_post("", "")
        time.sleep(2)
        assert "Content can't be blank" in self.driver.find_element_by_xpath('/html/body/div[1]').text

    def test_2_edit_post(self):
        self.post.create_post("Hello", self.image+'\koala.jpg')
        self.post.edit_post("I Love Koala")
        self.assertEqual("I Love Koala", self.driver.find_element_by_xpath('//*/div[2]/span/p').text)
        self.post.go_to_main_page()
        self.post.delete_post()

    def test_3_comment_post_1(self):
        self.post.create_post("Hello", self.image+'\koala.jpg')
        self.post.comment_post("I Love Koala too")
        self.assertEqual("I Love Koala too", self.driver.find_element_by_xpath('//*/div[2]/div[1]/span/p').text)
        self.post.go_to_main_page()
        self.post.delete_post()

    def test_3_comment_post_2(self):
        self.post.create_post("Hello", self.image + '\koala.jpg')
        self.post.comment_post("")
        self.assertEqual("commit", self.driver.find_element_by_xpath('//*[@id="new_comment"]/input[2]').get_attribute("name"))
        self.post.go_to_main_page()
        self.post.delete_post()

    def test_4_like_post(self):
        self.post.create_post("Hello", self.image+'\koala.jpg')
        self.post.like_post()
        self.assertEqual("1 like", self.driver.find_element_by_xpath('//*/div[2]/div[3]/span[1]').text)
        self.post.delete_post()

    def test_5_delete_post(self):
        self.post.create_post("Hello", self.image+'\koala.jpg')
        self.post.get_deleted_post_id()
        self.post.delete_post()
        self.post.go_to_main_page()
        self.assertTrue(self.post.check_delete_post())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
