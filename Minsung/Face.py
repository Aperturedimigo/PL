from Minsung.util import *

def detect(image, face_id=True):
    url = 'detect'
    headers ={
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': KEY,
    }

    params = {
        'returnFaceId': face_id,
    }

    return request('POST', url, headers=headers, params=params, data=image)


def find_similars(face_id, face_list_id):

    url = 'findsimilars'
    headers ={
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': KEY,
    }

    json ={
    "faceId":face_id,
    "faceListId":face_list_id,
    "maxNumOfCandidatesReturned":100,
    "mode": "matchPerson"
}

    return request('POST', url, json=json, headers=headers)


def group(face_ids):

    url = 'group'
    json = {
        'faceIds': face_ids,
    }

    return request('POST', url, json=json)


def identify(face_ids, person_group_id, max_candidates_return=1,
             threshold=None):

    url = 'identify'
    json = {
        'personGroupId': person_group_id,
        'faceIds': face_ids,
        'maxNumOfCandidatesReturned': max_candidates_return,
        'confidenceThreshold': threshold,
    }

    return request('POST', url, json=json)


def verify(face_id, another_face_id):

    url = 'verify'
    json = {
            'faceId1': face_id,
            'faceId2': another_face_id,
        }



    return request('POST', url, json=json)