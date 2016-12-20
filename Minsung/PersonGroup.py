from Minsung.util import *

def create(person_group_id, name = None, user_data = None):
    name = person_group_id if name is None else name
    url = 'persongroups/{}'.format(person_group_id)
    json ={
        'name' : name,
        'userData' : user_data,
    }
    return request('PUT', url, json = json)

def delete(person_group_id):
    url = 'persongroups/{}'.format(person_group_id)
    return request('DELETE', url)

def get(person_group_id):
    url = 'persongroups/{}'.format(person_group_id)
    return request('GET', url)

def get_status(person_group_id):
    url = 'persongroups/{}/training'.format(person_group_id)
    return request('GET', url)

def lists(start = None, end = None):
    url = 'persongroups'
    params ={
        'start' : start,
        'end' : end,
    }
    return request('GET', url, params=params)

def train(person_group_id):
    url = 'persongroups/{}/train'.format(person_group_id)
    return request('POST', url)

def update(person_group_id, name = None, user_data = None):
    url = 'persongroups/{}'.format(person_group_id)
    json ={
        'name': name,
        'userData': user_data,
    }
    return request('PATCH', url, json=json)