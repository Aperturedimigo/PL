from Minsung.util import *

def add_face(image, face_list_id, user_data=None, target_face=None):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': KEY
    }
    json = {
        "url": image
    }
    params = {
        'userData': user_data,
        'targetFace': target_face,
    }
    data = requests.post('https://api.projectoxford.ai/face/v1.0/facelists/{}/persistedFaces'.format(face_list_id),
                         headers=headers, params=params, json=json)
    return data.text




def create(face_list_id, name=None, user_data=None):
    name = face_list_id if name is None else name
    url = 'facelists/{}'.format(face_list_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    return request('PUT', url, json=json)


def delete_face(face_list_id, persisted_face_id):
    url = 'facelists/{}/persistedFaces/{}'.format(
        face_list_id, persisted_face_id
    )

    return request('DELETE', url)


def delete(face_list_id):
    url = 'facelists/{}'.format(face_list_id)

    return request('DELETE', url)


def get(face_list_id):
    url = 'facelists/{}'.format(face_list_id)

    return request('GET', url)


def lists():
    url = 'facelists'

    return request('GET', url)


def update(face_list_id, name=None, user_data=None):
    url = 'facelists/{}'.format(face_list_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    return request('PATCH', url, json=json)
