# coding = utf-8
import time
from selenium.common.exceptions import NoSuchElementException
import os
from framework.logger import Logger
import HTMLTestRunner

# create a logger instance
logger = Logger(logger='BasePage').getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 结束测试，退出浏览器
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def froward(self):
        self.driver.froward()
        logger.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Close and quit the browser.")
        except Exception as e:
            logger.info("Failed to quit the browser with %s" % e)

    # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接报错到我们项目根目录的一个文件夹.\Screenshots下
        :return:
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('Had take screenshot and save to folder: /screenshots')
        except Exception as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # 输出报告
    # def output_report(self):
    #     """
    #     在这里我们定义输出报告的方法
    #     :return:
    #     """
    #     # 设置报告文件保存路径
    #     report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
    #     # 获取系统当前时间
    #     now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    #     # 设置报告名称格式
    #     HtmlFile = report_path + now + 'HTMLtemplate.html'
    #     fp = open(HtmlFile, "wb")
    #     # try:
    #     #     self.driver.get_screenshot_as_file(screen_name)
    #     #     logger.info('Had take screenshot and save to folder: /screenshots')
    #     # except Exception as e:
    #     #     logger.error("Failed to take screenshot! %s" % e)
    #     #     self.get_windows_img()

    # 定位单个元素方法
    def find_element(self, selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
        submit_btn = "id=>su"
        login_lnk = "xpath => //*[@id='u1']/a[7]"  #百度首页登录连接定位
        如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element\' %s \' successful"
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot

        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.fine_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'css_selector':
            try:
                element = self.driver.find_element_by_css_selector(selector_value)
                logger.info("Had find\' %s\' successful"
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                self.get_windows_img()
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    # 定位多个元素的方法
    def find_elements(self, selector, value1):
        """
                这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
                submit_btn = "id=>su"
                login_lnk = "xpath => //*[@id='u1']/a[7]"  #百度首页登录连接定位
                如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
                :param value1:
                :param selector:
                :return:
                """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if selector_by == "ss" or selector_by == 'css_selectors':
            try:
                element = self.driver.find_elements_by_css_selector(selector_value)[value1]
                logger.info("Had find\' %s\' successfulby %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                self.get_windows_img()

        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element


    # 输入
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in type in input box with %s" % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.info("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 获取文本
    def text(self, selector):
        el = self.find_element(selector)
        logger.info("Current element text is %s" % el.text)
        return el.text

    # 获取指定文本
    def texts(self, selector, value):
        el = self.find_elements(selector)
        logger.info("Current element text is %s" % el[value].text)
        return el[value].text

    # 获取隐藏属性
    def get_hide_attribute(self, selector, value, text):
        el = self.find_elements(selector, value)
        logger.info("Current hide element value is %s" % el.get_attribute(text))
        return el.get_attribute(text)

    # 获取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
