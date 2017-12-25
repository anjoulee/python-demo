# -*- coding: utf-8 -*-

### 了解ConfigParser
### 使用Python管理ini文件：实现查询，添加，删除，保存
### ini 配置文件格式
###   节：            [session]
###   参数（键=值）     name=value

import os

import os.path

import ConfigParser


### 1:dump ini
### 2:del section
### 3:del item
### 4:modify item
### 5:add section
### 6:save modify

class student_info(object):
    def __init__(self, recordfile):
        print recordfile
        self.logfile = recordfile
        self.cfg = ConfigParser.ConfigParser()

    def cfg_load(self):
        self.cfg.read(self.logfile)

    def cfg_dump(self):
        se_list = self.cfg.sections()
        print '++++++++++++++++++++++'
        for se in se_list:
            print se
            print self.cfg.items(se)

    def delete_item(self, section, key):
        self.cfg.remove_option(section, key)

    def delete_section(self, sescion):
        self.cfg.remove_section(sescion)

    def add_section(self, section):
        self.cfg.add_section(section)

    def set_item(self, section, key, value):
        self.cfg.set(section, key, value)

    def save(self):
        fp = open(self.logfile, 'w')
        self.cfg.write(fp)
        fp.close()


if __name__ == '__main__':
    info = student_info('imooc1.txt')
    info.cfg_load()
    info.cfg_dump()
    info.set_item('userinfo', 'pwd', '123')
    info.cfg_dump()
    info.add_section('login')
    info.set_item('login', '2017-12-15', '20')
    info.cfg_dump()
    info.save()
