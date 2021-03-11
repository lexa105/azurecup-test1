from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import cv2
import numpy as np
import urllib.request


def img_url(remote_image_url_faces):
    resp = urllib.request.urlopen(remote_image_url_faces)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    return cv2.resize(image, dim, interpolation=inter)


#subscription key k Azure + koncový bod
subscription_key = "d2f4441154804aae9654f31190f5ab06"
endpoint = "https://gfp-vision.cognitiveservices.azure.com/"

#  Overeni clienta
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


#remote_image_url_faces = input("Zadej sem link obrázku ")
remote_image_url_faces = input("Zadejte link ")

'''
Detect Faces - remote
This example detects faces in a remote image, gets their gender and age, 
and marks them with a bounding box.
'''
print("===== Detect Faces - remote =====")
# Get an image with faces

# Select the visual feature(s) you want.
remote_image_features = ["faces"]
# Call the API with remote URL and features
detect_faces_results_remote = computervision_client.analyze_image(remote_image_url_faces, remote_image_features)

# Print the results with gender, age, and bounding box
print("Faces in the remote image: ")
if (len(detect_faces_results_remote.faces) == 0):
    
    print("No faces detected.")
else:
    for face in detect_faces_results_remote.faces:
        print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
        face.face_rectangle.left, face.face_rectangle.top, \
        face.face_rectangle.left + face.face_rectangle.width, \
        face.face_rectangle.top + face.face_rectangle.height))






print("\n")
print("===== Opening in OpenCV =====")



image = img_url(remote_image_url_faces)
cv2.rectangle(image, (face.face_rectangle.left, face.face_rectangle.top), (face.face_rectangle.left + face.face_rectangle.width, face.face_rectangle.top + face.face_rectangle.height), (0, 255, 0), 3)

cv2.imshow('faces', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
