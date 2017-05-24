import BasePage


class ProfilePage(BasePage.BasePage):

    def go_to_edit_profile_page(self):
        self.driver.find_element_by_xpath('//*[@id="navbar-top"]/ul/li/a').click()
        self.driver.find_element_by_xpath('//*[@id="navbar-top"]/ul/li/ul/li[2]/a').click()

    def upload_avatar_and_cover(self, avatar, cover):
        self.driver.find_element_by_id("user_avatar").clear()
        self.driver.find_element_by_id("user_avatar").send_keys(avatar)
        self.driver.find_element_by_id("user_cover").clear()
        self.driver.find_element_by_id("user_cover").send_keys(cover)
        self.driver.find_element_by_name("commit").click()

    def edit_profile(self,name,  about, location, phone, dob):
        self.driver.find_element_by_name("user[name]").clear()
        self.driver.find_element_by_name("user[name]").send_keys(name)
        self.driver.find_element_by_name("user[about]").clear()
        self.driver.find_element_by_name("user[about]").send_keys(about)
        self.driver.find_element_by_name("user[location]").clear()
        self.driver.find_element_by_name("user[location]").send_keys(location)
        self.driver.find_element_by_name("user[phone_number]").clear()
        self.driver.find_element_by_name("user[phone_number]").send_keys(phone)
        self.driver.find_element_by_name("user[dob]").clear()
        self.driver.find_element_by_name("user[dob]").send_keys(dob)
        self.driver.find_element_by_name("commit").click()
