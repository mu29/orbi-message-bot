#-*- coding: utf-8 -*-

import requests
from settings import *
from database import *

def send_message(phone):
    try:
        response = requests.post(
            url = MESSAGE_SERVER_URL,
            headers = {
                'x-waple-authorization': MESSAGE_API_KEY,
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            },
            data = {
                'msg_body': MESSAGE,
                'send_phone': SEND_PHONE,
                'dest_phone': phone,
            },
        )
        if response.status_code == 200:
            print phone + u'으로 메시지 전송'
        else:
            print ('Error ' + response.status_code)
    except requests.exceptions.RequestException:
        print(u'메시지 전송 실패')


db = DataBase()

teacher_id = 0
count = 0
while True:
    try:
        teacher_id += 1
        if not db.is_available(teacher_id):
            continue

        send_message(db.get_phone(teacher_id))
        db.update_available(teacher_id)
        count += 1
        if count > MESSAGE_COUNT:
            break
    except:
        if teacher_id >= db.get_count():
            break
        for e in sys.exc_info():
            print e
        continue

print u'메시지 전송 완료'
