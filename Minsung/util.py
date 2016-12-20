import os.path
import time

import requests

import cognitive_face as CF

KEY = '7fc4c113fee941e1b9e964ab98f559a7'
_BASE_URL = 'https://api.projectoxford.ai/face/v1.0/'
TIME_SLEEP = 1

class CognitiveFaceException(Exception):
    def __init__(self, status_code, code, msg):
        super(CognitiveFaceException, self).__init__()
        self.status_code = status_code
        self.code = code
        self.msg = msg

    def __str__(self):
        return (
            'Error when calling Cognitive Face API:\n'
            '\tstatus_code: {}\n'
            '\tcode: {}\n'
            '\tmessage: {}\n'
        ).format(self.status_code, self.code, self.msg)

def request(method, url, data=None, json=None, headers=None, params=None):
    if not url.startswith('https://'):
        url = _BASE_URL + url
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = 'application/json'
    headers['Ocp-Apim-Subscription-Key'] = KEY

    response = requests.request(method, url, params=params, data=data,
                                json=json, headers=headers)
    result = None

    if response.status_code not in (200, 202):
        print('status_code: {}'.format(response.status_code))
        print('response: {}'.format(response.text))
        error_msg = response.json()['error']
        raise CognitiveFaceException(
            response.status_code,
            error_msg.get('code'),
            error_msg.get('message'))


    if response.text:
        result = response.json()
    else:
        result = {}

    return result


def Image(image):
    if hasattr(image, 'read'):
        headers = {'Content-Type': 'application/octet-stream'}
        data = image.read()
        return headers, data, None
    elif os.path.isfile(image):
        headers = {'Content-Type': 'application/octet-stream'}
        data = open(image, 'rb').read()
        return headers, data, None
    else:
        headers = {'Content-Type': 'application/json'}
        json = {'url': image}
        return headers, None, json


def training(person_group_id):

    index = 1
    while True:
        res = CF.person_group.get_status(person_group_id)
        if res['status'] in ('succeeded', 'failed'):
            break
        print('The training of Person Group {} is onging: #{}'.format(
            person_group_id, index))
        time.sleep(2**index)
        index += 1


def deleteFaceLists():
    face_lists = CF.face_list.lists()
    time.sleep(TIME_SLEEP)
    for face_list in face_lists:
        face_list_id = face_list['faceListId']
        CF.face_list.delete(face_list_id)
        print('Deleting Face List {}'.format(face_list_id))
        time.sleep(TIME_SLEEP)


def deletePersonGroups():
    person_groups = CF.person_group.lists()
    time.sleep(TIME_SLEEP)
    for person_group in person_groups:
        person_group_id = person_group['personGroupId']
        CF.person_group.delete(person_group_id)
        print('Deleting Person Group {}'.format(person_group_id))
        time.sleep(TIME_SLEEP)
