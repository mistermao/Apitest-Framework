# coding = utf-8
import time
import unittest

from pageobjects.ehr_birthday import BirthdayPage
from pageobjects.ehr_birthday import BirthdaySql
from framework.browser_engine import BrowserEngine


class EhrBirthday(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        """
        测试固件setUp()代码，主要是测试前准备
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @ classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_01_solar_calendar_submit(self):
        """
         公历生日提交
         :return:
         """
        birthdaypage = BirthdayPage(self.driver)
        birthdaysql = BirthdaySql()
        birthdaypage.type_emp_code("GS0415")
        birthdaypage.click_user_birthday()
        birthdaypage.click_date()
        birthdaypage.click_solar_calendar_submit()
        try:
            assert birthdaysql.get_birthday_sql()[0] == '阳历'
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_lunar_calendar_submit(self):
        """
        农历生日提交
        :return:
        """
        birthdaypage = BirthdayPage(self.driver)
        birthdaysql = BirthdaySql()
        birthdaypage.type_emp_code("GS0415")
        birthdaypage.click_user_birthday()
        birthdaypage.click_date()
        birthdaypage.click_lunar_calendar()
        birthdaypage.click_lunar_calendar_submit()
        try:
            assert birthdaysql.get_birthday_sql()[0] == '农历'
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))



if __name__ == '__main__':
    unittest.main()
