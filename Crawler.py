#-*- coding: utf-8 -*-

import urllib
import urllib2
from settings import *
from profile import *
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self):
        self.base_url = 'http://tutor.orbi.kr/'
        self.login_url = 'https://login.orbi.kr/user/login/tutor'
        self.cookie = COOKIE

    def get_url(self, no):
        return self.base_url + 'teacher/' + str(no) + '/bookmark'

    def get_pure_url(self, no):
        return self.base_url + 'teacher/' + str(no)

    def get_cookie(self):
        login_query = urllib.urlencode(USER_INFO)
        request = urllib2.Request(self.login_url, login_query)
        response = urllib2.urlopen(request)
        cookie = response.headers.get('Set-Cookie')
        return cookie

    def get_latest_no(self):
        url = self.base_url + 'search/teachers?page=1'
        document = urllib.urlopen(url)
        soup = BeautifulSoup(document, 'html.parser')

        teachers = soup.find_all('a', { 'class' : 'teacher-wrapper' })
        latest_teacher = teachers[len(teachers) - 12]
        no = latest_teacher['href'].split('?')[0][9:]
        return int(no)

    def get_soup(self, url):
        request = urllib2.Request(url)
        request.add_header('cookie', self.cookie)
        response = urllib2.urlopen(request)
        soup = BeautifulSoup(response.read(), 'html.parser')
        return soup

    def get_profile(self, no):
        url = self.get_url(no)
        soup = self.get_soup(url)

        enable = soup.find('li', { 'class' : 'student-item' })
        if not enable is None:
            return None

        phone = soup.find('div', { 'class' : 'bookmark-phone' })
        if phone is None:
            soup = self.get_soup(self.get_pure_url(no))
            phone = soup.find('div', { 'class' : 'bookmark-phone' })

        phone = phone.string
        data = soup.find('div', { 'class' : 'profile-summary' })
        subject = data.contents[1].string
        name = data.contents[3].contents[3].contents[0].string.strip()
        age = data.contents[5].contents[3].string
        school = data.contents[7].contents[3].string
        profile = Profile(name, subject, age, school, phone)
        print school + " " + name
        return profile
