#-*- coding: utf-8 -*-

import time
from crawler import *
from database import *

crawler = Crawler()
db = DataBase()

while True:
    try:
        old = db.get_count() + 1
        latest = crawler.get_latest_no() + 1

        for i in range(old, latest):
            profile = crawler.get_profile(i)
            if not profile is None:
                db.put(profile)

        time.sleep(3600)
    except:
        for e in sys.exc_info
            print e
        continue
