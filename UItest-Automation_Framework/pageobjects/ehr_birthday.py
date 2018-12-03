from framework.base_page import BasePage
from framework.mysql import MySQL

database = MySQL()
emp_name = 'liliuyang'
emp_code = 'GS0415'


class BirthdayPage(BasePage):
    # 员工工号 input
    emp_code_input = "xpath=>.//*[@id='app']/div/form/div[1]/div/div[1]/input"
    # 员工生日选择按钮
    user_birthday_button = "xpath=>.//*[@id='app']/div/form/div[3]/div/div/input"
    # 日期选择框
    date_button = "xpath=>html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[5]/td[6]/div"
    # 农历/公历选择框
    lunar_calendar_button = "xpath=>.//*[@id='app']/div/form/div[4]/div/div/span[2]"
    # 阳历重置按钮
    solar_calendar_clear_button = "xpath=>.//*[@id='app']/div/form/div[5]/div/button[1]"
    # 阴历重置按钮
    lunar_calendar_clear_button = "xpath=>.//*[@id='app']/div/form/div[6]/div/button[1]"
    # 阳历提交按钮
    solar_calendar_submit_button = "xpath=>.//*[@id='app']/div/form/div[5]/div/button[2]"
    # 阴历提交按钮
    lunar_calendar_submit_button = "xpath=>.//*[@id='app']/div/form/div[6]/div/button[2]"

    # 输入员工工号
    def type_emp_code(self, text):
        self.type(self.emp_code_input, text)

    # 日期框选择
    def click_date(self):
        self.click(self.date_button)

    # 员工生日选择
    def click_user_birthday(self):
        self.click(self.user_birthday_button)

    # 农历选择按钮
    def click_lunar_calendar(self):
        self.click(self.lunar_calendar_button)

    # 阳历重置按钮
    def click_solar_calendar_clear(self):
        self.click(self.solar_calendar_clear_button)

    # 阴历重置按钮
    def click_lunar_calendar_clear(self):
        self.click(self.lunar_calendar_clear_button)

    # 阳历提交按钮
    def click_solar_calendar_submit(self):
        self.click(self.solar_calendar_submit_button)

    # 阴历重置按钮
    def click_lunar_calendar_submit(self):
        self.click(self.lunar_calendar_submit_button)


class BirthdaySql(object):
    """
    生日类型&生日日期
    """
    def get_birthday_sql(self):
        birthday_information = list(database.query_dic({
            'select': 'birthday_type AS 生日类型, actual_birthday AS 实际生日',
            'from': 'emp_main',
            'where': 'emp_code = "%s"' % emp_code
        })[0])
        if birthday_information[0] == 1:
            birthday_information[0] = '阳历'
        elif birthday_information[0] == 0:
            birthday_information[0] = '农历'
        return birthday_information
