import requests

userName = "user"
faceListId = "aperture_" + userName
# Valid character is letter in lower case or digit or '-' or '_', maximum length is 64.

keyfile = open("./key.txt")
key = keyfile.readline()

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': key,
}

body = {
    "name": "aperture",
}

r = requests.put("https://api.projectoxford.ai/face/v1.0/facelists/{}".format(faceListId), json=body, headers=headers)
print(r.json())