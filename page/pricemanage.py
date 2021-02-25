from admin.base_page import BasePage


class PriceManage(BasePage):
    def click_price_manage_button(self):  #点击询报价管理按钮
        self.driver.find_element_by_xpath("//li[3]/div/span").click()

    def launch_ask_price_plan(self):  #进入计划采购询价列表
        self.driver.find_element_by_xpath("//li[3]/ul/li[2]/span").click()

    def launch_ask_price_urgent(self):  #进入应急采购询价列表
        self.driver.find_element_by_xpath("//li[3]/ul/li[1]/span").click()