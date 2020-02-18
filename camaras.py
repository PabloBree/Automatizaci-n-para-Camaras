from selenium import webdriver

import unittest
import time


class Items(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie('IEDriverServer.exe')
        #self.driver.implicitly_wait(10)
        self.driver.get('https://www.freeip.com')


    def test_view_score(self):
        self.driver.find_element_by_id('username').send_keys('randomKEY')
        #self.driver.find_element_by_name('username').send_keys('SparcMac')
        #self.driver.find_element_by_name('submit').click()
        time.sleep(7)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()





