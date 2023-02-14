
from flask import Flask
from flask import render_template
import RPi.GPIO as GPIO
import time


app= Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.OUT)

GPIO.setwarnings(False)

print("Done")

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route('/B1')
def Rot():
    print("B1")
    GPIO.output(35,True)
    return render_template('loadingsite.html')

@app.route('/B2')
def Gelb():
    print("B2")
    GPIO.output(35,False)
    return render_template('webpage.html')

@app.route('/B3')
def Gruen():
    print("B3")
    return render_template('webpage.html')

@app.route('/B4')
def Blau():
    print("B4")
    return render_template('webpage.html')

if __name__=="__main__":
    print("Start")
    app.run(debug=True) ,host='192.168.4.1')
