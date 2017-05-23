import BasePage
import time


class PostPage(BasePage.BasePage):

    def create_post(self, content, picture):
        self.driver.find_element_by_xpath("//*[@id='post-content']").send_keys(content)
        self.driver.find_element_by_name('post[attachment]').send_keys(picture)
        self.driver.find_element_by_name("commit").click()

    def edit_post(self, content):
        self.driver.find_element_by_xpath('//*/div[2]/div[3]/div/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="post-content"]').clear()
        self.driver.find_element_by_xpath('//*[@id="post-content"]').send_keys(content)
        self.driver.find_element_by_name("commit").click()

    def comment_post(self, content):
        self.driver.find_element_by_xpath('//*/div[3]/div/div[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="comment-text"]').send_keys(content)
        self.driver.find_element_by_name("commit").click()
        time.sleep(2)

    def like_post(self):
        self.driver.find_element_by_xpath('//*/div[3]/div/div[1]/form/button').click()
        time.sleep(2)

    def delete_post(self):
        self.driver.find_element_by_xpath('//*/div[2]/div[3]/div/a[2]').click()

    def get_deleted_post_id(self):
        self.deleteId = self.driver.find_element_by_xpath('//*[@id="activities"]/div/div').get_attribute("id")
        time.sleep(2)

    def check_delete_post(self):
        for id in self.driver.find_elements_by_xpath('//*[@id="activities"]//div'):
            if id.get_attribute("id") == self.deleteId:
                print id.get_attribute("id")
                return False
        return True


