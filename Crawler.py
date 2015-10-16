#-*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup
from Result import *

class Crawler:
    def __init__(self):
        self.base_url = 'http://tutor.orbi.kr/teacher/'

    def get_url(self, no):
        return self.base_url + str(no) + '/bookmark'

    def get_profile(self, no):
