import time
import BasePage


class LoginPage(BasePage.BasePage):

    def socify_login(self):
        self.driver.find_element_by_xpath("//*[@id='navbar-top']/ul/li[3]/a").click()
        email = self.driver.find_element_by_id("user_email")
        password = self.driver.find_element_by_id("user_password")
        email.send_keys("t105598031@ntut.org.tw")
        password.send_keys("105598031")
        time.sleep(1)
        login_button = self.driver.find_element_by_name("commit")
        login_button.click()




