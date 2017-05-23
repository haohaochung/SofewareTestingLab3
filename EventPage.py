import BasePage
import time


class EventPage(BasePage.BasePage):
    def go_to_create_event_page(self):
        self.driver.find_element_by_xpath('//*[@id="links"]/h5[2]/a').click()

    def create_event(self, event_name, event_time):
        self.driver.find_element_by_name("event[name]").send_keys(event_name)
        self.driver.find_element_by_id("event_event_datetime").send_keys(event_time)
        self.driver.find_element_by_name("commit").click()

    def edit_event(self, event_name):
        self.driver.find_element_by_xpath('//*/div[2]/div[2]/div/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="event_name"]').clear()
        self.driver.find_element_by_xpath('//*[@id="event_name"]').send_keys(event_name)
        self.driver.find_element_by_name("commit").click()

    def comment_event(self, comment):
        self.driver.find_element_by_xpath('//*/div[3]/div/div[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="comment-text"]').send_keys(comment)
        self.driver.find_element_by_name("commit").click()
        time.sleep(2)

    def like_event(self):
        self.driver.find_element_by_xpath('//*/div[3]/div/div[1]/form/button').click()
        time.sleep(2)

    def delete_event(self):
        self.driver.find_element_by_xpath('//*/div[2]/div[2]/div/a[2]').click()
        time.sleep(2)

    def get_deleted_event_id(self):
        self.deleteId = self.driver.find_element_by_xpath('//*[@id="activities"]/div/div').get_attribute("id")
        time.sleep(2)

    def check_delete_event(self):
        for id in self.driver.find_elements_by_xpath('//*[@id="activities"]//div'):
            if id.get_attribute("id") == self.deleteId:
                print id.get_attribute("id")
                print self.deleteId
                return False
        return True
