import requests

# parameters : faceListId, userData,
userName = "user"
faceListId = "aperture_" + userName


keyfile = open("./key.txt")
key = keyfile.readline()

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': key,
}

body = {
    'url' :  'https://scontent-icn1-1.xx.fbcdn.net/v/t1.0-9/14713625_1781339335442468_3974977702287855879_n.jpg?oh=9b640f377a6508384e4bd820457edbd2&oe=58993815'
}

r = requests.post("https://api.projectoxford.ai/face/v1.0/facelists/{}/persistedFaces".format(faceListId), json=body,
                 headers=headers)


# persistedFaceId of the added face, which is persisted and will not expire.
# Different from faceId which is created in Face - Detect and will expire in 24 hours after the detection call.

print(r.json())