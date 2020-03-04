import requests
import uuid
import random
import os
from pathlib import Path
from os.path import dirname, abspath
title = random.choice(["Linear Regression", "Ordinal Regression"])
author = random.choice( ["Mitesh", "Ashish", "Shashi"])
idval = random.randrange(10, 20, 2)

import sys

input_datUrl = os.environ.get('TRAINING_DATA_URL', 'https://genpurposestorage.blob.core.windows.net/imagescontainer/TrainingData2.csv')

pythonVer = sys.version[:5]
requirementsList = open('requirements.txt').readlines()
requirements = ' '.join([req.split()[0] for req in requirementsList])

description = 'Python v'+pythonVer+' '+requirements

modelUploadBase = "https://52.165.161.123:8000/user/ashkuma/notebooks/demo/"
directory = os.path.split(os.getcwd())[1]
fileName = "/SampleModelGeneratorScriptCopy.ipynb"
filePath = modelUploadBase + directory + fileName

payload = [('fileName','model'+str(uuid.uuid4())),('id',str(idval)),('author',author),('title',title),('description',description),('link',filePath),('tags','regression'),
          ('trainingData',input_datUrl)]

from urllib.parse import urlencode
params = urlencode(payload)

f = open('azdevopsdemo.pkl','rb')
MODEL_UPLOAD_URL = "https://functionappdemoazure.azurewebsites.net/api/LayoutBlobStorageTrigger"
Hit_url = MODEL_UPLOAD_URL+'?'+params
headers = {'Content-Type': 'application/json'}
requests.post(Hit_url, headers=headers, data=f.read())