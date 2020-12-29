# -*- coding: utf-8 -*-
# @Author : feier
# @File : conftest.py
import pytest
import yaml
from pythoncode.calculator import Calculator
import os

# 通过 os.path.dirname 获取当前文件所在目录的路径
yaml_file_path = os.path.dirname(__file__) + "/data.yml"

# 打开yaml文件，并获取key值对应列表
with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    # 获取文件中key为datas的数据
    add_data = datas['add']
    sub_data = datas['sub']
    mul_data = datas['mul']
    div_data = datas['div']
    # 获取文件中key为myids的数据
    #add_ids = datas["myids"]

@pytest.fixture(scope='module', params=add_data)  # scope为作用域  params为参数列表
def get_add_data(request):
    print('开始计算')
    data = request.param  # 获取参数列表中value值
    yield data
    print('计算结束')

@pytest.fixture(scope='module',params=sub_data)
def get_sub_data(request):
    print('开始计算')
    data = request.param  # 获取参数列表中value值
    yield data
    print('计算结束')

@pytest.fixture(scope='module',params=mul_data)
def get_mul_data(request):
    print('开始计算')
    data = request.param  # 获取参数列表中value值
    yield data
    print('计算结束')

@pytest.fixture(scope='module',params=div_data)
def get_div_data(request):
    print('开始计算')
    data = request.param  # 获取参数列表中value值
    yield data
    print('计算结束')

@pytest.fixture(scope="class")
def get_calc():
    print("获取计算器实例")
    calc = Calculator() # 生命Caculator对象
    return calc