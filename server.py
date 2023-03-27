from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
# if cairo dll file error throws, install pipwin with pip, and install cairocffi via pipwin: pip install pipwin, pipwin install cairocffi
from svgtopng import svg2img
from main import predict
import cv2 as cv
import random
import string
from extractletters import extract_letters
from svgtopng import svg2img
import os
from uvicorn import run
import base64
import numpy as np

def randomString(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


dataset_dir = 'dataset'

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers
)


@app.post("/svg")
async def resolveCaptchaFromSvg(svg: str = Body(..., embed=True)):
    try:
        img = svg2img(svg)
        return {"status": True, "message": "success", "data": predict(img)}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=502, detail='An exception has ocurred.')
    
@app.post("/img")
async def resolveCaptchaFromImg(img: str = Body(..., embed=True)):
    try:
        encoded_image = img.split(',')[1]
        decoded_image = base64.b64decode(encoded_image)
        np_data = np.fromstring(decoded_image,np.uint8)
        image = cv.imdecode(np_data, cv.IMREAD_GRAYSCALE)
        return {"status": True, "message": "success", "data": predict(image)}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=502, detail='An exception has ocurred.')

@app.post("/dataset")
async def resolveCaptcha(svg: str = Body(..., embed=True), text = Body(..., embed=True)):
    if not os.path.exists('dataset'):
        os.mkdir('dataset')
    img = svg2img(svg)
    letters = extract_letters(img)
    for i, letter in enumerate(letters):
        label = text[i]
        randLetter = ''.join(random.choice(string.ascii_letters) for y in range(5))
        if not os.path.exists('dataset/'+label):
            os.mkdir('dataset/' + label)
        cv.imwrite('dataset/' + label + '/'+randLetter + '.png', letter)


@app.post("/svg2png")
async def convert(svg: str = Body(..., embed=True)):
    img = svg2img(svg)
    cv.imwrite('captchas/captcha.png', img)


@app.get("/health")
async def healthCheck():
    return {"message": "success"}

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    run(app, host="0.0.0.0", port=port)
