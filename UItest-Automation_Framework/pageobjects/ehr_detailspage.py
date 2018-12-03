from framework.base_page import BasePage
from framework.mysql import MySQL

database = MySQL()
emp_name = 'liliuyang'
emp_code = 'GS0303'


class DetailsPage(BasePage):
    # 编辑按钮
    edit_button = "xpath=>.//*[@id='app']/div/div[3]/div/div/div[1]/button[1]"
    # 取消编辑按钮
    clear_edit_buttom = "xpath=>.//*[@id='app']/div/div[3]/div/div/div[1]/button[2]"
    # 个人信息 input
    emp_details_input = "ss=>.el-input__inner"
    # 爱好特长 input
    interes_text_input = "ss=>.el-textarea__inner"
    # 家庭情况
    family_information_input = "s=>.el-table__body"

    """
    基本信息
    """

    def get_basic_information_page(self):
        basic_information = []
        for i in range(0, 25):
            basic_information += [self.get_hide_attribute(self.emp_details_input, i, "value")]
        basic_information += [self.get_hide_attribute(self.interes_text_input, 0, "value")]
        return basic_information

    """
    户籍信息
    """
    def get_addr_information_page(self):
        addr_information = []
        for i in range(25, 29):
            addr_information += [self.get_hide_attribute(self.emp_details_input, i, "value")]
        return addr_information

    """
    银行信息
    """
    def get_bank_information_page(self):
        bank_information = []
        for i in range(29, 32):
            bank_information += [self.get_hide_attribute(self.emp_details_input, i, "value")]
        return bank_information

    """
    家庭情况
    """
    def get_family_information_page(self):
        family_information = (self.text(self.family_information_input))
        return family_information

    """
    
    """


class DetailsSql(object):

    """
    基本信息
    """
    def get_basic_information_sql(self):
        basic_information = list(database.query_dic({
            'select': 'emp_code AS 工号,	emp_name AS 姓名, cast(age as char) AS 年龄, gender AS 性别, nation_desc AS 民族,'
                      'p_visage_desc AS 政治面貌, date_format(birthday, "%Y-%m-%d") AS 生日, cast(qq_num as char) AS QQ号码,'
                      'personal_mail AS 电子邮箱, cast(phone_num as char) AS 手机号码, marital_status AS 婚姻状况,'
                      'cast(child_num as char) AS 子女数量, city_desc AS 驻地城市, cast(company_age as char)AS 司龄,'
                      'formal_desc AS 在职状态, DATE_FORMAT(last_hire_date, "%Y-%m-%d") AS 入职日期,'
                      'DATE_FORMAT(last_formal_date, "%Y-%m-%d") AS 转正日期,job_desc AS 职位, account_name AS 所属组织,'
                      'dept_name_path AS 部门路径, p_emp_name AS 直属上级,p_emp_code AS 直属上级工号, contact_name AS 紧急联系人,'
                      'contact_relation AS 关系,cast(contact_phone_num as char) AS 电话,	interest AS 爱好特长',
            'from': 'emp_main',
            'where': 'emp_code = "%s"' % emp_code
        })[0])
        if basic_information[3] == '1':
            basic_information[3] = '男'
        elif basic_information[3] == '0':
            basic_information[3] = '女'
        if basic_information[10] == '1':
            basic_information[10] = '未婚'
        elif basic_information[10] == '0':
            basic_information[10] = '已婚'
        return basic_information

    """
    户籍信息
    """
    def get_addr_information_sql(self):
        addr_information = list(database.query_dic({
            'select': 'identity_num AS 身份证号, identity_type AS 户口性质, identity_addr AS 身份证地址, addr AS 现住址',
            'from': 'emp_sub_addr',
            'where': 'emp_code = "%s"' % emp_code
        })[0])
        # 户口性质
        if addr_information[1] == '1':
            addr_information[1] = '城镇'
        elif addr_information[1] == '0':
            addr_information[1] = '农村'
        return addr_information
