#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 17:10
# @Author  : huanghe
# @Site    : 
# @File    : test_ad_materia.py
# @Software: PyCharm
import unittest
import os,sys
from baselib.logging.pylogging import setup_logging
from seleniumlib.browser import Browser
from zq_lib.AquaPassAdv.login_page import LoginPage
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from time import sleep
setup_logging()
import time

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = Browser(timeout=60)
        login_page = LoginPage(self.driver)
        login_page.url='http://10.50.4.115:8080/paasadv/'
        login_page.visit()
        login_page.wait(10)
        login_page.set_value(element=login_page.rec_user_input(),text="root")
        login_page.set_value(element=login_page.rec_passwd_input(),text="123")
        login_page.click_login_btn()
        self.first_page = login_page.get_first_page()

    def tearDown(self):
        ...
        self.driver.quit()

#创建图片素材
    def test_create_mpicture_materia(self):
        now = time.strftime("%Y%m%d%H%M%S")
        #进入广告页面
        sleep(2)
        self.first_page.rec_material_btn()
        self.ad_materia_page = self.first_page.click_material_btn()
        sleep(0.5)
        self.ad_materia_page.rec_mpicture_btn()
        self.mpicture_page = self.ad_materia_page.click_mpicture_btn()
        self.mpicture_page.rec_create_btn()
        self.create_mpicture_materia_page = self.mpicture_page.click_create_btn()
        sleep(0.5)
        self.create_mpicture_materia_page.click_upload()
        os.system('D:/auit/materia.exe')
        sleep(5)
        self.create_mpicture_materia_page.set_value(self.create_mpicture_materia_page.receive_material_name_input(), text=(now + '图片素材'))
        self.create_mpicture_materia_page.set_value(self.create_mpicture_materia_page.receive_sucai_width_input(), "123")
        self.create_mpicture_materia_page.set_value(self.create_mpicture_materia_page.receive_sucai_height_input(), "123")
        self.create_mpicture_materia_page.select_weight(text='20')
        self.create_mpicture_materia_page.click_confirm_btn()
        sleep(5)
        self.create_mpicture_materia_page.switch_alert()
        self.create_mpicture_materia_page.get_windows_img()



    if __name__ == '__main':
        unittest.main()