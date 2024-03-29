import unittest
import LoginPage
import EventPage
import time
from selenium import webdriver


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://140.124.183.106:3000/")
        LoginPage.LoginPage(self.driver).socify_login()
        self.event = EventPage.EventPage(self.driver)

    def test_1_create_event_1(self):
        self.event.go_to_create_event_page()
        self.event.create_event("See a Movie", "2017/06/01 12:00")
        self.assertEqual("See a Movie", self.driver.find_element_by_xpath('//*/div[2]/h3').text)
        self.event.delete_event()

    def test_1_create_event_2(self):
        self.event.go_to_create_event_page()
        self.event.create_event("@@#$%", "2017/06/01 12:00")
        self.assertEqual("@@#$%", self.driver.find_element_by_xpath('//*/div[2]/h3').text)
        self.event.delete_event()

    def test_1_create_event_3(self):
        self.event.go_to_create_event_page()
        self.event.create_event("", "")
        self.assertEqual("commit", self.driver.find_element_by_xpath('//*[@id="new_event"]/div[3]/input').get_attribute("name"))

    def test_2_edit_event(self):
        self.event.go_to_create_event_page()
        self.event.create_event("See a Movie", "2017/06/01 12:00")
        self.event.edit_event("Singing")
        self.assertEqual("Singing", self.driver.find_element_by_xpath('//*/div[2]/h3').text)
        self.event.delete_event()

    def test_3_comment_event_1(self):
        self.event.go_to_create_event_page()
        self.event.create_event("See a Movie", "2017/06/01 12:00")
        self.event.comment_event("I want, too")
        self.assertEqual("I want, too", self.driver.find_element_by_xpath('//*/div[2]/div[1]/span/p').text)
        self.event.delete_event()

    def test_3_comment_event_2(self):
        self.event.go_to_create_event_page()
        self.event.create_event("See a Movie", "2017/06/01 12:00")
        self.event.comment_event("")
        self.assertEqual("commit", self.driver.find_element_by_xpath('//*[@id="new_comment"]/input[2]').get_attribute("name"))
        self.event.delete_event()

    def test_4_like_event(self):
        self.event.go_to_create_event_page()
        self.event.create_event("See a Movie", "2017/06/01 12:00")
        self.event.like_event()
        self.assertEqual("1 like", self.driver.find_element_by_xpath('//*/div[2]/div[2]/span[1]').text)
        self.event.delete_event()

    def test_5_delete_event(self):
        self.event.go_to_create_event_page()
        self.event.create_event("See a Movie", "2017/06/01 12:00")
        self.event.get_deleted_event_id()
        self.event.delete_event()
        self.event.go_to_main_page()
        self.assertTrue(self.event.check_delete_event())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()