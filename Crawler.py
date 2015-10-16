#-*- coding: utf-8 -*-

import urllib
import urllib2
from settings import *
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self):
        self.base_url = 'http://tutor.orbi.kr/teacher/'
        self.cookie = COOKIE

    def get_url(self, no):
        return self.base_url + str(no) + '/bookmark'

    def get_cookie(self):
        url = 'https://login.orbi.kr/user/login/tutor'
        login_query = urllib.urlencode(USER_INFO)
        request = urllib2.Request(url,login_query)
        response = urllib2.urlopen(request)
        cookie = response.headers.get('Set-Cookie')
        return cookie

    def get_profile(self, no):
        url = self.get_url(no)
        request = urllib2.Request(url)
        request.add_header('cookie', self.cookie)
        response = urllib2.urlopen(request)

        print response.read()
        soup = BeautifulSoup(response.read(), 'html.parser')
