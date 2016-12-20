from Minsung.util import *

def add_Face(image, person_group_id, person_id, user_data = None, target_face = None):
    url = 'persongroups/{}/persons/{}/persistedFaces'.format(person_group_id, person_id)
    headers, data, json = Image(image)
    params = {
        'userData': user_data,
        'targetFace': target_face
    }
    return request('POST', url, headers=headers, params=params, json=json, data=data)

def create(person_group_id, name, user_data=None):
    url = 'persongroups/{}/persons'.format(person_group_id)
    json = {
        'name': name,
        'userData': user_data,
    }
    return request('POST', url, json=json)

def delete(person_group_id, person_id):
    url = 'persongroups/{}/persons/{}'.format(person_group_id, person_id)
    return request('DELETE', url)

def delete_face(person_group_id, person_id, persisted_face_id):
    url = 'persongroups/{}/persons/{}/persistedFaces/{}'.format(
        person_group_id, person_id, persisted_face_id
    )
    return request('DELETE', url)

def get(person_group_id, person_id):
    url = 'persongroups/{}/persons/{}'.format(person_group_id, person_id)
    return request('GET', url)

def get_face(person_group_id, person_id, persisted_face_id):
    url = 'persongroups/{}/persons/{}/persistedFaces/{}'.format(
        person_group_id, person_id, persisted_face_id
    )
    return request('GET', url)

def lists(person_group_id):
    url = 'persongroups/{}/persons'.format(person_group_id)
    return request('GET', url)

def update(person_group_id, person_id, name=None, user_data=None):
    url = 'persongroups/{}/persons/{}'.format(person_group_id, person_id)
    json = {
        'name': name,
        'userData': user_data,
    }
    return request('PATCH', url, json=json)

def update_face(person_group_id, person_id, persisted_face_id, user_data=None):
    url = 'persongroups/{}/persons/{}/persistedFaces/{}'.format(
        person_group_id, person_id, persisted_face_id
    )
    json = {
        'userData': user_data,
    }
    return request('PATCH', url, json=json)
"""
Complete Person.py
Complete Person.py
"""