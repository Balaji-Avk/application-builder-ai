import google.generativeai as genai
import textwrap
import json
from filehandler import createFile
from zipit import zipFile
import time

print("Welcome to AI project builder , This script uses Gemini API to build applications for you. \n")

time.sleep(2)

key = input("Please enter your Gemini AI API key : ")

time.sleep(2)

genai.configure(api_key= key )

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

description = input("\nEnter what you want to build using Gemini AI : ")

time.sleep(2)

print('\nBuilding.... \n')

instruction = textwrap.dedent("""
    Please return JSON having file name as key and value as code from the description of the project use the following JSON schema as a reference:

    code = {"file_name": str , "code":str}

    return list[code]
                         
    Important: Only return a single piece of valid JSON.
                         
    Note : Structure the file as the requirements of the project

    Here is the Description:

    """)


#getting response from the model

try :
  response = model.generate_content(instruction + description)
except:
  print('Invalid API key')
  exit()

print('Build complete , Creating files.... \n')

try:
  jsonfor = json.loads(response.text[8:-3])

  jsonfor = list(jsonfor)
except:
  print("please rewrite the description and try again")
  exit()

for i in jsonfor :
  createFile(i['file_name'],i['code'])


print("creating zip file please wait \n")

zipFile()

print("Thank You for using it.")