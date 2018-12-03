# coding = utf-8
import time
import unittest

from pageobjects.ehr_loginpage import LoginPage
from pageobjects.ehr_detailspage import DetailsPage
from pageobjects.ehr_detailspage import DetailsSql
from framework.browser_engine import BrowserEngine


class EhrDetail(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):
        """
        测试固件setUp()代码，主要是测试前准备
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        loginpage = LoginPage(cls.driver)
        loginpage.type_empspell('liliuyang')
        loginpage.type_emppassword('888888')
        loginpage.click_login_button()
        time.sleep(5)

    @ classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_01_check_basic_information(self):
        """
         检查基本信息数据
         :return:
         """
        detailspage = DetailsPage(self.driver)
        detailssql = DetailsSql()
        try:
            assert detailspage.get_basic_information_page() == detailssql.get_basic_information_sql()
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_02_check_addr_information(self):
        """
        检查户籍信息数据
        :return:
        """
        detailspage = DetailsPage(self.driver)
        detailssql = DetailsSql()
        try:
            assert detailspage.get_addr_information_page() == detailssql.get_addr_information_sql()
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_04_check_family_information(self):
        """
         检查家庭信息数据
         :return:
         """
        detailspage = DetailsPage(self.driver)
        detailssql = DetailsSql()
        list1 = detailspage.get_family_information_page().split()
        list3 = []
        for j in range(0, int(len(list1) / 4)):
            list2 = []
            for i in range(j * 4, (j + 1) * 4):
                list2 += [list1[i]]
            list3 += [list2]
        print(list3)

        try:
            assert detailspage.get_basic_information_page() == detailssql.get_basic_information_sql()
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))


if __name__ == '__main__':
    unittest.main()
