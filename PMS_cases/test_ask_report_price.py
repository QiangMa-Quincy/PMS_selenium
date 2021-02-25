from page.pricemanage import PriceManage


class TestAskReportPrice(PriceManage):
    def test_launch_price_list_plan(self):  #进入计划采购询价列表
        self.click_price_manage_button()
        self.launch_ask_price_plan()

        response = self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[2]/table/thead/tr').text #断言
        print(response)
        assert "序号" in response

    def test_launch_price_list_urgent(self):    #进入应急采购询价列表
        self.click_price_manage_button()
        self.launch_ask_price_urgent()

        response = self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[2]/table/thead/tr').text #断言
        print(response)
        assert "序号" in response
