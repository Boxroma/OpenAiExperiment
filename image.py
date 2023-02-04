import openai
import os
import sys
import subprocess
import requests
import uuid

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

prompt = sys.argv

def openImage(path):
    imageViewerFromCommandLine = {'linux':'xdg-open',
                                  'win32':'explorer',
                                  'darwin':'open'}[sys.platform]
    subprocess.run([imageViewerFromCommandLine, path])
    
response = openai.Image.create(
    # engine="text-davinci-003",
    prompt=str(prompt),
    n=4,
    size="1024x1024"
)

os.mkdir("output")

folderName = "output/" + str(uuid.uuid4())
os.mkdir(folderName)

count = 1
for object in response['data']:
    
    fileName = "%s/image_%d.jpg"%(str(folderName),count)
    img_data = requests.get(object['url']).content
    with open(fileName, 'wb') as handler:
        handler.write(img_data)
        
    openImage(fileName)
    
    count += 1