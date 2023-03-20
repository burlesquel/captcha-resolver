from svgtopng import svg2img
import cv2 as cv

img = svg2img('<svg xmlns="http://www.w3.org/2000/svg" width="250" height="150" viewBox="0,0,250,150"><rect width="100%" height="100%" fill="rgb(255,200,150)"/><path d="M10 116 C125 47,107 95,240 68" stroke="#6cdd42" fill="none"/><path fill="#e368ac" d="M62.95 77.30L62.91 77.25L63.01 77.35Q63.80 77.28 65.30 77.12L65.25 77.06L65.31 77.12Q65.23 77.78 65.23 78.48L65.39 78.63L65.20 79.80L65.27 79.86Q64.39 79.88 63.50 79.96L63.47 79.93L63.56 80.03Q62.70 80.10 61.80 80.06L61.68 79.94L61.79 80.06Q58.73 86.66 55.06 91.59L54.94 91.47L54.99 91.52Q52.37 92.29 50.98 92.94L50.86 92.82L51.00 92.96Q55.37 86.81 58.64 80.08L58.60 80.04L55.83 80.09L55.84 80.09Q55.69 78.52 55.57 77.09L55.67 77.20L55.63 77.16Q57.63 77.28 59.84 77.28L59.88 77.33L61.86 73.31L61.87 73.32Q62.99 71.34 64.30 69.63L64.28 69.61L64.38 69.71Q62.63 69.80 60.92 69.80L60.89 69.77L60.97 69.85Q54.46 69.86 50.42 67.50L50.34 67.42L49.67 65.60L49.66 65.59Q49.33 64.74 48.93 63.80L48.78 63.65L48.92 63.79Q53.61 66.65 59.73 66.90L59.56 66.73L59.59 66.76Q65.18 67.09 70.69 64.97L70.68 64.96L70.59 64.87Q70.52 65.45 69.99 66.39L69.83 66.23L69.97 66.37Q66.12 71.49 63.06 77.40ZM71.71 67.86L71.68 67.83L72.63 65.56L72.75 65.69Q71.57 66.05 69.78 66.83L69.79 66.84L70.13 66.65L70.07 66.59Q70.26 66.50 70.38 66.37L70.41 66.40L70.41 66.40Q70.76 65.61 71.53 64.18L71.41 64.05L71.44 64.09Q65.89 66.69 59.73 66.45L59.70 66.42L59.58 66.30Q53.15 66.03 48.05 62.85L48.11 62.90L48.17 62.96Q49.24 64.93 50.14 67.79L50.08 67.73L50.13 67.78Q51.26 68.42 52.11 68.74L52.20 68.83L52.21 68.84Q52.25 69.08 52.74 71.08L52.73 71.07L52.87 71.21Q56.26 72.57 62.18 72.40L62.12 72.35L62.16 72.38Q61.73 72.90 59.61 76.94L59.62 76.95L59.64 76.97Q57.38 76.91 55.26 76.70L55.36 76.80L55.32 76.76Q55.40 77.66 55.40 78.60L55.41 78.61L55.45 80.49L57.25 80.49L57.24 81.99L57.12 81.86Q52.96 89.82 49.98 93.65L49.91 93.59L49.97 93.64Q51.67 92.82 53.43 92.29L53.40 92.26L53.49 92.35Q52.69 93.26 51.22 95.10L51.19 95.07L51.28 95.16Q54.63 93.94 57.24 93.70L57.29 93.74L57.26 93.71Q60.40 89.68 63.75 82.42L63.72 82.39L67.33 82.53L67.33 82.54Q67.42 81.73 67.42 80.75L67.27 80.59L67.26 78.67L67.34 78.75Q67.00 78.69 66.41 78.73L66.45 78.78L66.48 78.81Q65.80 78.76 65.52 78.76L65.61 78.86L65.57 78.81Q65.50 78.63 65.54 78.46L65.68 78.59L65.62 78.26L65.63 78.26Q68.30 72.74 71.61 67.76Z"/><path fill="#79e169" d="M122.34 90.41L122.50 90.57L122.49 90.56Q121.67 90.43 120.93 90.47L120.91 90.45L120.99 90.53Q120.19 90.58 119.45 90.58L119.50 90.62L119.49 90.62Q119.89 86.86 119.89 83.19L119.98 83.27L119.97 83.27Q118.01 83.31 117.03 83.31L117.05 83.33L116.93 83.21Q116.13 83.31 114.18 83.23L114.19 83.23L114.21 83.26Q114.09 82.81 113.89 80.16L113.91 80.19L113.93 80.21Q116.63 80.74 119.81 80.74L119.77 80.70L119.78 80.71Q119.57 76.06 119.12 73.28L119.11 73.27L119.24 73.40Q120.04 73.47 120.90 73.47L120.90 73.47L122.73 73.55L122.63 73.45Q122.39 78.02 122.39 80.80L122.40 80.80L122.34 80.74Q124.73 80.80 128.15 80.44L128.19 80.47L128.20 80.49Q128.02 81.85 128.02 83.16L128.00 83.14L128.07 83.21Q127.68 83.10 126.82 83.14L126.96 83.29L126.83 83.15Q125.88 83.26 125.22 83.30L125.07 83.14L125.16 83.24Q125.09 83.17 122.24 83.17L122.28 83.21L122.33 86.93L122.39 87.00Q122.30 88.66 122.42 90.49ZM128.59 79.90L128.51 79.82L128.59 79.89Q126.59 80.27 124.59 80.35L124.55 80.30L124.47 80.22Q124.86 76.98 125.31 74.98L125.37 75.04L125.34 75.01Q124.59 75.08 123.08 75.24L123.02 75.18L123.30 73.06L123.23 72.98Q120.37 72.94 118.57 72.81L118.61 72.85L118.69 72.94Q119.26 76.24 119.47 80.40L119.52 80.45L119.54 80.47Q117.41 80.18 113.45 79.53L113.45 79.52L113.57 79.64Q113.91 80.96 113.91 83.78L113.84 83.71L115.38 83.61L115.38 83.61Q115.36 84.37 115.20 85.88L115.25 85.93L119.45 85.61L119.59 85.74Q119.27 89.05 118.94 91.01L119.04 91.11L118.92 90.99Q119.72 90.98 121.23 90.85L121.20 90.82L121.39 91.01Q121.29 91.64 121.25 93.07L121.18 93.00L121.29 93.11Q121.90 93.15 125.77 93.31L125.77 93.31L125.71 93.25Q124.76 89.97 124.51 85.73L124.42 85.64L124.55 85.77Q127.96 85.71 130.20 86.12L130.19 86.11L130.28 86.19Q130.03 85.13 130.03 84.11L130.14 84.22L130.05 82.09L130.11 82.15Q129.76 82.05 129.19 82.09L129.30 82.20L128.40 82.15L128.46 82.21Q128.55 81.45 128.67 79.98Z"/><path fill="#c17ee2" d="M178.71 83.56L178.72 83.57L178.68 83.53Q182.04 83.17 185.46 83.29L185.43 83.27L185.35 83.18Q185.32 80.45 185.32 77.88L185.41 77.98L185.30 77.87Q185.28 75.19 185.48 72.46L185.62 72.60L185.56 72.54Q184.24 74.36 178.65 83.50ZM189.19 91.31L189.19 91.30L189.23 91.35Q187.49 91.07 185.57 90.99L185.63 91.05L185.62 91.04Q185.39 88.48 185.27 85.83L185.29 85.85L185.16 85.73Q179.54 85.61 174.48 87.12L174.49 87.13L174.40 87.04Q174.63 86.62 174.84 85.56L174.86 85.58L174.74 85.46Q176.65 82.07 180.48 75.34L180.54 75.39L180.63 75.49Q183.75 70.29 187.43 66.13L187.36 66.06L187.24 65.94Q188.29 65.85 190.09 65.57L189.97 65.44L190.14 65.62Q188.01 72.42 188.01 79.96L188.03 79.99L188.04 79.99Q188.06 81.61 188.14 83.20L188.19 83.25L189.57 83.36L189.52 83.32Q190.10 83.28 190.75 83.40L190.84 83.49L190.85 83.50Q190.95 84.54 191.23 86.62L191.17 86.56L191.26 86.64Q189.85 86.25 188.26 86.05L188.28 86.07L188.33 86.12Q188.49 88.19 189.22 91.33ZM191.06 83.02L191.17 83.12L191.01 82.97Q190.93 83.01 190.73 83.01L190.58 82.86L190.18 82.87L190.32 83.01Q190.18 81.40 190.18 79.89L190.08 79.79L190.06 79.77Q190.17 73.03 192.37 66.59L192.33 66.55L192.28 66.49Q191.62 66.93 190.07 67.34L190.05 67.32L190.03 67.31Q190.19 66.40 190.68 64.89L190.80 65.01L190.77 64.98Q189.29 65.30 187.08 65.54L187.10 65.56L187.04 65.50Q182.93 70.24 177.35 80.27L177.26 80.19L179.64 76.41L179.63 76.40Q179.10 77.42 178.81 78.03L178.92 78.14L174.12 87.78L174.04 87.70Q174.67 87.47 175.89 87.06L175.96 87.13L175.81 87.39L175.76 87.34Q175.67 88.10 175.34 89.45L175.41 89.52L175.37 89.47Q179.68 87.96 184.86 88.16L184.87 88.17L184.97 88.27Q185.05 89.33 185.25 91.45L185.12 91.32L185.11 91.30Q186.42 91.47 187.56 91.59L187.47 91.50L187.52 91.55Q187.69 92.29 187.97 93.76L187.88 93.67L187.89 93.67Q189.97 93.96 193.20 94.94L193.14 94.89L193.12 94.87Q192.17 92.70 191.20 89.19L191.11 89.10L192.62 89.55L192.66 89.60Q193.35 89.80 194.09 90.16L194.11 90.18L194.12 90.20Q193.32 87.56 193.16 85.77L193.16 85.77L193.07 85.68Q192.61 85.67 191.39 85.42L191.26 85.30L191.33 85.37Q191.15 84.05 191.15 83.11ZM182.53 82.89L182.50 82.86L182.61 82.97Q183.31 81.47 184.99 78.74L184.90 78.66L185.03 78.78Q185.04 79.81 185.00 80.83L185.05 80.88L185.01 80.85Q184.99 81.89 185.04 82.91L185.02 82.89L185.02 82.89Q184.37 82.81 183.76 82.81L183.77 82.82L183.87 82.92Q183.18 82.88 182.52 82.88Z"/></svg>')

cv.imwrite('fourcaptcha.png', img)
