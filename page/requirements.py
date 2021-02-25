from admin.base_page import BasePage
from selenium import webdriver


class RequirementsAll(BasePage):
    def click_requirements(self):
        self.driver.find_element_by_xpath("//li[2]/div/span").click()  #需求大厅
        return self.launch_plan_buy

    def launch_urgent(self):
        self.driver.find_element_by_xpath("//li[2]/ul/li[1]/span").click() #应急采购事件
        return

    def launch_plan_buy(self):
        self.driver.find_element_by_xpath("//li[2]/ul/li[2]/span").click() #计划采购事件
        return
