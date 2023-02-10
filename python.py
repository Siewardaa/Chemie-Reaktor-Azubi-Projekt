from flask import Flask
from flask import render_template
#import RPi.GPIO as rpi
import time

app= Flask(__name__)


#rpi.setwarnings(False)

print("Done")

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route('/B1')
def Rot():
    print("B1")
    return render_template('webpage.html')

@app.route('/B2')
def Gelb():
    print("B2")
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
    app.run(debug=True) #,host='192.168.4.1')
