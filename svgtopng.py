# if cairo dll file error throws, install pipwin with pip, and install cairocffi via pipwin: pip install pipwin, pipwin install cairocffi
from cairosvg import svg2png
from PIL import Image
from io import BytesIO
import numpy as np 

# Abstraction of svg2png library.

def svg2img(svg):
    img_bytes = svg2png(bytestring=svg, scale=1.0)
    return np.array(Image.open(BytesIO(img_bytes)).convert('RGBA'))