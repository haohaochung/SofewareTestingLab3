import os
class BasePage(object):
    pict_location = os.getcwd()+'\pict'

    def __init__(self, driver):
        self.driver = driver

    def go_to_main_page(self):
        self.driver.find_element_by_xpath('/html/body/nav/div/div[1]/a').click()