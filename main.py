from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
# if cairo dll file error throws, install pipwin with pip, and install cairocffi via pipwin: pip install pipwin, pipwin install cairocffi
from svgtopng import svg2img
from predict import predict
import cv2 as cv
import random
import string
import os

def randomString(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.post("/captcha/")
async def resolveCaptcha(svg:str = Body(..., embed=True), letter:str = Body(..., embed=True)):
    try:
        img = svg2img(svg)
        img = cv.cvtColor(img, cv.COLOR_RGBA2BGRA)
        result = predict(img)
        for i,letter in enumerate(result):
            result[i] = letter.replace('_', '')
        print(result)
        cv.imshow('img', img)
        cv.waitKey(0)
        return {"message": "success", "result":result}
    except Exception as err:
        print(err)
        return {"message": "error"}