import json
try:
    import unzip_requirements
except ImportError:
    pass
from requests_toolbelt.multipart import decoder

import boto3
import os
# import tarfile
import io
import base64
import json
import cv2
import random

#gindex = 0
def gans(event, context):
    try:
        gindex = random.randint(20,68)
        #gindex = gindex % 68
        filename = "images/" + str(gindex) + ".png"
        print(filename)
        img = cv2.imread(filename,-1)
        dim = (350, 350)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        _, im_arr = cv2.imencode('.png', resized)  # im_arr: image in Numpy one-dim array format.
        #im_bytes = im_arr.tobytes()
        fields = {"gans": base64.b64encode(img_arr).decode("utf-8")} #back to binary
        return {
            "statusCode": 200,
            "headers": {
                'content-type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True
            },
            "body": json.dumps(fields)
        }
    
    except Exception as e:
        print(repr(e))
        return {
            "statusCode": 500,
            "headers": {
                'content-type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True
            },
            "body": json.dumps({"error": repr(e)})
        }

