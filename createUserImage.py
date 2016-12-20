import Minsug.Face_list as fl
import yaml


def createMainImage(face_list_id, image):
    fl.create(face_list_id)
    data = yaml.load(fl.add_face(image, face_list_id))
    with open('ps1.txt', 'w') as f:
        f.write(data["persistedFaceId"])
        f.close()

def deleteFaceListID(face_list_id):
    fl.delete(face_list_id)

def getSecondImage(face_list_id, image):
    data = yaml.load(fl.add_face(image, face_list_id))
    with open('ps2.txt', 'w') as f:
        f.write(data['persistedFaceId'])
        f.close()
