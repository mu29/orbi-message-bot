#-*- coding: utf-8 -*-

import sys
import time
from crawler import *
from database import *

crawler = Crawler()
db = DataBase()

while True:
    old = db.get_count() + 1
    latest = crawler.get_latest_no() + 1

    for i in range(old, latest):
        try:
            profile = crawler.get_profile(i)
            if not profile is None:
                db.put(profile)
        except:
            for e in sys.exc_info():
                print e
            continue

    time.sleep(3600)
