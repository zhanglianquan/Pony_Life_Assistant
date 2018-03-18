# coding=utf-8
# Author: zlq
# Copyright (C) 2018/03/18.


"""
    项目启动需要的一些设置模块:比如数据库设置的一些参数
"""

# database setting
database = {
    "mongodb": {
        "name": "test_db",
        "username": "",
        "password": "",
        "host": "127.0.0.1",
        "port": 27017,
    }
}


# tornado setting
tornado = {
    "debug": True,
    "autoreload": True,
    "cookie_secret": "cookie_secret_code",
}


