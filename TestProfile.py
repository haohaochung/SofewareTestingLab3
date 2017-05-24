import unittest
import BasePage
import LoginPage
import ProfilePage
import time
from selenium import webdriver


class TestProfile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://140.124.183.106:3000/")
        LoginPage.LoginPage(self.driver).socify_login()
        self.profile = ProfilePage.ProfilePage(self.driver)
        self.profile.go_to_edit_profile_page()
        self.image = BasePage.BasePage.pict_location

    def test_1_upload_avatar_and_cover_1(self):
        self.profile.upload_avatar_and_cover(self.image+'\me.jpg', self.image+'\koala.jpg')
        assert "me.jpg" in self.driver.find_element_by_xpath('//*[@id="user-info"]/div[1]/a/img').get_attribute("src")
        assert "koala.jpg" in self.driver.find_element_by_xpath('/html/body/div/div[1]').get_attribute("style")

    def test_1_upload_avatar_and_cover_2(self):
        self.profile.upload_avatar_and_cover(self.image + '\g.txt', self.image + '\g.txt')
        assert "g.txt" in self.driver.find_element_by_xpath('//*[@id="user-info"]/div[1]/a/img').get_attribute("src")
        assert "g.txt" in self.driver.find_element_by_xpath('/html/body/div/div[1]').get_attribute("style")

    def test_1_upload_avatar_and_cover_3(self):
        self.profile.upload_avatar_and_cover(self.image + '\giphy.gif', self.image + '\giphy.gif')
        assert "giphy.gif" in self.driver.find_element_by_xpath('//*[@id="user-info"]/div[1]/a/img').get_attribute("src")
        assert "giphy.gif" in self.driver.find_element_by_xpath('/html/body/div/div[1]').get_attribute("style")

    def test_1_upload_avatar_and_cover_4(self):
        self.profile.upload_avatar_and_cover('', '')
        assert "" in self.driver.find_element_by_xpath('//*[@id="user-info"]/div[1]/a/img').get_attribute(
            "src")
        assert "" in self.driver.find_element_by_xpath('/html/body/div/div[1]').get_attribute("style")

    def test_2_edit_profile_1(self):
        self.profile.edit_profile("105598031","I am haohao", "Taipei", "0912345678", "1994/07/02")
        self.assertEqual("105598031", self.driver.find_element_by_xpath('//*[@id="user-info"]/div[1]/h5/a').text)
        self.assertEqual("22 years old", self.driver.find_element_by_xpath('//*[@id="user-info"]/h5[2]').text)
        self.assertEqual("Taipei", self.driver.find_element_by_xpath('//*[@id="user-info"]/h5[3]').text)

    def test_2_edit_profile_2(self):
        self.profile.edit_profile("", "", "", "", "")
        time.sleep(2)
        self.assertEqual("Edit Profile", self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/h3').text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()