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
async def resolveCaptchaFromSvg(svg: str = Body(..., embed=True), mode: str = Body(None, embed=True)):
    try:
        img = svg2img(svg)
        return {"status": True, "message": "success", "data": predict(img, mode)}
    except Exception as err:
        raise HTTPException(status_code=501, detail='An exception has ocurred.')

@app.post("/dataset")
async def resolveCaptcha(svg: str = Body(..., embed=True), captcha_type: str = Body(..., embed=True), text: str = Body(..., embed=True)):
    if not os.path.exists('dataset2'):
        os.mkdir('dataset2')
    img = svg2img(svg)
    result = extract_letters(img, type=captcha_type, dataset_mode=True)
    if captcha_type == "math":
        for i, char in enumerate(result):
            label = text[i]
            randLetter = ''.join(random.choice(string.ascii_letters)
                                 for i in range(5))
            if not os.path.exists('dataset2/'+label):
                os.mkdir('dataset2/' + label)
            cv.imwrite('dataset2/' + label + '/'+randLetter + '.png', char)
    elif captcha_type == "normal":
        for letter in result:
            if not os.path.exists('dataset2/'+text):
                os.mkdir('dataset2/'+text)
            randLetter = ''.join(random.choice(string.ascii_letters)
                                 for i in range(5))
            cv.imwrite('dataset2/' + text + '/'+randLetter + '.png', letter)


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
