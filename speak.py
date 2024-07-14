import requests
from pypdf import PdfReader 

reader = PdfReader('example_short.pdf') 
pages = reader.pages

textToSpeak = ""
for page in pages:
   textToSpeak += page.extract_text()
print(textToSpeak)

urlPiper = "http://localhost:5000"
outputFilename = "output.wav"

payload = {'text': textToSpeak}

r = requests.get(urlPiper,params=payload)

with open(outputFilename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)