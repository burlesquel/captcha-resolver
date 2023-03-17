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


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


@app.post("/captcha")
async def resolveCaptcha(svg: str = Body(..., embed=True)):
    try:
        result = predict(svg)
        print(result)
        return {"message": "success", "result": result}
    except Exception as err:
        print(err)
        return {"message": "error"}


@app.post("/dataset")
async def resolveCaptcha(svg: str = Body(..., embed=True), captcha_type: str = Body(..., embed=True), character: str = Body(..., embed=True)):
    if not os.path.exists('dataset'):
        os.mkdir('dataset')
    img = svg2img(svg)
    result = extract_letters(img, type=captcha_type, dataset_mode=True)
    if captcha_type == "math":
        randLetter = ''.join(random.choice(string.ascii_letters) for i in range(5))
        if not os.path.exists('dataset/'+'+'):
            os.mkdir('dataset/+')
        cv.imwrite('dataset/+/'+randLetter + '.png', result)
    elif captcha_type == "normal":
        for letter in result:
            if not os.path.exists('dataset/'+character):
                os.mkdir('dataset/'+character)
            randLetter = ''.join(random.choice(string.ascii_letters) for i in range(5))
            cv.imwrite('dataset/'+ character +'/'+randLetter + '.png', letter)


@app.get("/health")
async def healthCheck():
    return {"message": "success"}
