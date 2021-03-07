from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time



#subscription key k Azure + koncový bod
subscription_key = "d2f4441154804aae9654f31190f5ab06"
endpoint = "https://gfp-vision.cognitiveservices.azure.com/"

#  Overeni clienta
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


remote_image_url = input("Zadej sem link obrázku ")

'''
Describe an Image - remote
This example describes the contents of an image with the confidence score.
'''
print("===== Describe an image - remote =====")
# Call API
description_results = computervision_client.describe_image(remote_image_url)

# Get the captions (descriptions) from the response, with confidence level
print("Description of remote image: ")
if (len(description_results.captions) == 0):
    print("No description detected.")
else:
    for caption in description_results.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
