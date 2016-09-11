#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ConfigCommon:
    """基本配置"""
    pass


class ConfigMysql:
    """Mysql 连接信息"""
    port = 3306
    host = '127.0.0.1'
    user_name = 'root'
    password = ''


class ConfigDBNames:
    ablog = 'ablog'


class ConfigBlog:
    port = 8882
