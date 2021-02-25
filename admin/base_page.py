from selenium import webdriver

from page.localstorage import LocalStorage

url= "https://openapi.xianniu.cn/pms_web/"
#https://openapi.xianniu.cn/pms_web/index.html#/login  登陆地址

class BasePage:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(url)
        #增加登陆信息
        self.driver.find_element_by_xpath("//div[1]/input").send_keys("dingyuxin")  # 输入用户名
        self.driver.find_element_by_xpath("//div[1]/input[@type = 'password']").send_keys("123456")  # 输入密码
        self.driver.find_element_by_xpath("//button/span").click()  # 点击登陆按钮
        return

    def teardown(self):
        pass
        #self.driver.quit()