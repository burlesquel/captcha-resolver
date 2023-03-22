from seleniumwire import webdriver # Import seleniumwire
from selenium.webdriver.common.by import By
import requests
import time
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

API = "https://captcha-resolver-o28t.onrender.com/svg"

# Create the Chrome driver
driver = webdriver.Chrome()
 
# Go to the Github homepage
driver.get('http://localhost:3001')

svg = ""
 
# Access requests list via the `requests` attribute

trues = 0
falses = 0
x = 0
x_data, y_data = [], []

figure = pyplot.figure()
line, = pyplot.plot(x_data, y_data)

def update(frame):
    global falses
    global trues
    global x
    try:
        svg = ""
        driver.get('http://localhost:3001')
        for request in driver.requests:
            if request.response and "captcha" in request.url:
                svg = request.response.body.decode('utf-8')
        response = requests.post(API, json={"svg":svg})
        characters = "".join(response.json()['data'])
        input_element = driver.find_element(By.NAME, "captcha")
        button = driver.find_element(By.XPATH, "//input[@type='submit']")
        input_element.send_keys(characters)
        time.sleep(2)
        button.click()
        time.sleep(2)
        result = driver.find_element(By.TAG_NAME, 'p').get_attribute('innerText')
        if 'true' in result:
            trues = trues + 1
        else:
            falses = falses + 1
        success_rate = (trues/(trues+falses))*100
        print(f'trues: {trues} || falses: {falses} || success_rate: {success_rate}')
        x_data.append(x)
        y_data.append(success_rate)
        line.set_data(x_data, y_data)
        figure.gca().relim()
        figure.gca().autoscale_view()
        time.sleep(1)
        x = x + 1
        return line,
    except Exception as err:
        print(err)
    
# Draws success_rate graph.
animation = FuncAnimation(figure, update, interval=200)

pyplot.show()