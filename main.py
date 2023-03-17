from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
# if cairo dll file error throws, install pipwin with pip, and install cairocffi via pipwin: pip install pipwin, pipwin install cairocffi
from svgtopng import svg2img
from predict import predict
import cv2 as cv
import random
import string
from extractletters import extract_letters
from svgtopng import svg2img
import os

def randomString(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

dataset_dir = 'dataset'

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)

@app.post("/captcha")
async def resolveCaptcha(svg: str = Body(..., embed=True)):
    try:
        result = predict(svg, type='math')
        if result[1] == "+": #If the second character of the result is +, this is the math captcha.
            return {"message": "success", "result": result}
        else:
            result = predict(svg)
            print(result)
            return {"message": "success", "result": result}
    except Exception as err:
        print(err)
        return {"message": "error"}


@app.post("/dataset")
async def resolveCaptcha(svg: str = Body(..., embed=True), captcha_type: str = Body(..., embed=True), text: str = Body(..., embed=True)):
    if not os.path.exists('dataset2'):
        os.mkdir('dataset2')
    img = svg2img(svg)
    result = extract_letters(img, type=captcha_type, dataset_mode=True)
    if captcha_type == "math":
        for i, char in enumerate(result):
            label = text[i]
            randLetter = ''.join(random.choice(string.ascii_letters) for i in range(5))
            if not os.path.exists('dataset2/'+label):
                os.mkdir('dataset2/' + label)
            cv.imwrite('dataset2/'+ label +'/'+randLetter + '.png', char)
    elif captcha_type == "normal":
        for letter in result:
            if not os.path.exists('dataset2/'+text):
                os.mkdir('dataset2/'+text)
            randLetter = ''.join(random.choice(string.ascii_letters) for i in range(5))
            cv.imwrite('dataset2/'+ text +'/'+randLetter + '.png', letter)


@app.get("/health")
async def healthCheck():
    return {"message": "success"}

