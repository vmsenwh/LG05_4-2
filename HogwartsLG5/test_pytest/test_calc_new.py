# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_calc_new.py
import pytest
import allure
import log


@allure.feature('运算器测试类')
class TestCalc:

    # 测试add函数
    @pytest.mark.run(order=1)
    @allure.story('add运算用例')
    def test_add(self, get_calc, get_add_data):
        result = None
        try:
            # 调用add函数,返回的结果保存在result里面
            result = get_calc.add(get_add_data[0],get_add_data[1])
            # 判断result结果是否等于期望的值
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            log.logging.info(e)
        assert result == get_add_data[2]

    # 测试div函数
    @pytest.mark.run(order=4)
    @allure.story('div运算用例')
    def test_div(self, get_calc, get_div_data):
        result = None
        try:
            # 调用div函数，返回的结果保存在result里面
            result = get_calc.div(get_div_data[0],get_div_data[1])
            if isinstance(result,float):
                result = round(result,2)
        except Exception as e:
            log.logging.info(e)
        assert result == get_div_data[2]

    # 测试sub函数
    @pytest.mark.run(order=2)
    @allure.story('sub运算用例')
    def test_sub(self,get_calc,get_sub_data):
        result = None
        try:
            # 调用sub函数，返回的结果保存在result里面
            result = get_calc.sub(get_sub_data[0],get_sub_data[1])
            if isinstance(result,float):
                result = round(result,2)
        except Exception as e:
            log.logging.info(e)
        assert result == get_sub_data[2]

    # 测试mul函数
    @pytest.mark.run(order=3)
    @allure.story('mul运算用例')
    def test_mul(self, get_calc, get_mul_data):
        result = None
        try:
            # 调用sub函数，返回的结果保存在result里面
            result = get_calc.mul(get_mul_data[0], get_mul_data[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            log.logging.info(e)
        assert result == get_mul_data[2]

if __name__ == '__main__':
    #pytest.main(['test_calc_new.py','-vs'])
    #log.logging.info(os.getcwd())
    pytest.main(['test_calc_new.py', '-sq','--alluredir=../allure_Report/xml'])  # 生成报表数据