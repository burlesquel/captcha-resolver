from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
# if cairo dll file error throws, install pipwin with pip, and install cairocffi via pipwin: pip install pipwin, pipwin install cairocffi
from svgtopng import svg2img
from predict import predict
import cv2 as cv
import random
import string


def randomString(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.post("/captcha")
async def resolveCaptcha(svg:str = Body(..., embed=True), letter:str = Body(..., embed=True)):
    try:
        result = predict(svg)
        for i,letter in enumerate(result):
            result[i] = letter.replace('_', '')
        print(result)
        return {"message": "success", "result":result}
    except Exception as err:
        print(err)
        return {"message": "error"}

@app.get("/health")
async def healthCheck():
    return {"message": "success"}