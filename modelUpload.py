import requests
import uuid
import random
import os
from pathlib import Path
from os.path import dirname, abspath
import json
title = random.choice(["Linear Regression", "Ordinal Regression"])
author = random.choice( ["Mitesh", "Ashish", "Shashi"])
idval = random.randrange(10, 20, 2)

import sys


def getMetrics():
    obj = None;
    try:
        with open("metrics.json","r") as m:
            
            obj = json.load(m)
    except:
        pass

    return json.dumps(obj);


input_datUrl = os.environ.get('TRAINING_DATA_URL', 'https://genpurposestorage.blob.core.windows.net/imagescontainer/TrainingData2.csv')

pythonVer = sys.version[:5]
requirementsList = open('requirements.txt').readlines()
requirements = ' '.join([req.split()[0] for req in requirementsList])

description = 'Python v'+pythonVer+' '+requirements

modelUploadBase = "https://52.165.161.123:8000/user/ashkuma/notebooks/demo/"
directory = "testmlrepo"
fileName = "/SampleModelGeneratorScriptCopy.ipynb"
filePath = modelUploadBase + directory + fileName

tags = "age prediction, prediction"

metrics = getMetrics();


payload = [('fileName','model'+str(uuid.uuid4())),('id',str(idval)),('author',author),('title',title),('description',description),('link',filePath),('tags',tags),
          ('trainingData',input_datUrl),('metrics',metrics)]

from urllib.parse import urlencode
params = urlencode(payload)

f = open('azdevopsdemo.pkl','rb')
MODEL_UPLOAD_URL = "https://functionappdemoazure.azurewebsites.net/api/LayoutBlobStorageTrigger"
Hit_url = MODEL_UPLOAD_URL+'?'+params
headers = {'Content-Type': 'application/json'}
requests.post(Hit_url, headers=headers, data=f.read())