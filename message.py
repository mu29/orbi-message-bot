#-*- coding: utf-8 -*-

import json
import requests
from settings import *
from database import *

def send_message(teacher):
    try:
        response = requests.post(
            url = MESSAGE_SERVER_URL,
            headers = {
                'x-waple-authorization': MESSAGE_API_KEY,
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            },
            data = {
                'subject': teacher['name'] + u' 선생님께',
                'msg_body': MESSAGE.format(teacher['name']),
                'send_phone': SEND_PHONE,
                'dest_phone': teacher['phone'],
            },
        )
        if response.status_code == 200:
            print u'[{0}] {1} 선생님에게 메시지 전송'.format(teacher['id'], teacher['name'])
        else:
            print ('Error ' + response.status_code)
    except requests.exceptions.RequestException:
        print(u'메시지 전송 실패')


db = DataBase()

teacher_id = 0
count = 0
error_count = 0
while True:
    try:
        teacher_id += 1
        if not db.is_available(teacher_id):
            continue

        send_message(db.get_teacher(teacher_id))
        db.update_available(teacher_id)
        count += 1
        if count >= MESSAGE_COUNT:
            break
    except:
        if teacher_id >= db.get_count():
            break
        for e in sys.exc_info():
            print e
        error_count += 1
        continue

result_message = u'{0}번째 선생님까지 메시지 전송. 남은 선생님 {1}명, 오류 {2}건'.format(teacher_id, db.get_count() - teacher_id, error_count)
requests.post(
    url = SLACK_BOT_URL,
    data = json.dumps({ "text" : result_message }),
)
print result_message
