#-*- coding: utf-8 -*-

import urllib
import urllib2
from settings import *
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self):
        self.base_url = 'http://tutor.orbi.kr/teacher/'
        self.login_url = 'https://login.orbi.kr/user/login/tutor'
        self.cookie = COOKIE

    def get_url(self, no):
        return self.base_url + str(no)# + '/bookmark'

    def get_cookie(self):
        login_query = urllib.urlencode(USER_INFO)
        request = urllib2.Request(self.login_url, login_query)
        response = urllib2.urlopen(request)
        cookie = response.headers.get('Set-Cookie')
        return cookie

    def get_profile(self, no):
        url = self.get_url(no)
        request = urllib2.Request(url)
        request.add_header('cookie', self.cookie)
        response = urllib2.urlopen(request)
        soup = BeautifulSoup(response.read(), 'html.parser')

        phone = soup.find('div', { 'class' : 'bookmark-phone' })
        data = soup.find('div', { 'class' : 'profile-summary' })
        subject = data.contents[1].string
        name = data.contents[3].contents[3].contents[0].string.strip()
        age = data.contents[5].contents[3].string
        school = data.contents[7].contents[3].string
        profile = Profile(name, subject, age, school, phone)

        return profile
