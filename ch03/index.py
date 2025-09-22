import LED
from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/on")
def led_on():
    try:
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(LED, GPIO.HIGH)
        return "ok"
    except:
        GPIO.output(LED, GPIO.LOW)
        return "fail"

@app.route("/off")
def led_off():
    try:
        GPIO.output(8, GPIO.LOW)
        return "ok"
    except:
        return "fail"

if __name__ == "__main__":
    app.run(host="0.0.0.0")