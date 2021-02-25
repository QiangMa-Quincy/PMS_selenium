from page.requirements import RequirementsAll

class TestRequirements(RequirementsAll): #继承RequirementsAll的方法
    def test_launch_plan_list(self):
        self.click_requirements()
        self.launch_plan_buy()

        response = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[2]/table/thead/tr').text  #断言，计划采购事件页面列表的内容
        print(response)
        assert "事件表ID" in response

    def test_launch_urgent_list(self):
        self.click_requirements()
        self.launch_urgent()

        response = self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[2]/table/thead/tr').text  #断言，计划采购事件页面列表的内容
        print(response)
        assert "事件编号" in response #应急采购里没有事件表ID

