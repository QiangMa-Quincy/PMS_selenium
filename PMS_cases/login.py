from selenium.webdriver.common.by import By

from admin.base_page import BasePage

class TestLogin(BasePage):  #启动页面
    def test_login_OK(self):
        ele1 = self.driver.find_element_by_xpath("//div[1]/input").send_keys("dingyuxin") #输入用户名
        ele2 = self.driver.find_element_by_xpath("//div[1]/input[@type = 'password']").send_keys("123456") #输入密码
        ele3 = self.driver.find_element_by_xpath("//button/span").click() #点击登陆按钮
        r = self.driver.find_element_by_xpath("//*[@id='content']/div/div") #登陆后页面的内容
        print(r.text)
        assert '欢迎来到PMS-运营管理平台' in  r.text #断言，可参照https://blog.csdn.net/wanggaoxingh/article/details/79398043