from flask import Flask, request, render_template
import RPi.GPIO as GPIO
from servo import add_status

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
servo = GPIO.PWM(8, 50)
servo.start(0)


def setAngle(angle):
    duty = 2.5 + 10 * int(angle) / 180
    print(f"degree : {angle} to {duty}(duty)")
    servo.ChangeDutyCycle(duty)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def led_y_on():
    try:
        setAngle(request.get_json())
        add_status(request.get_json())
        print("ok")

        return "ok"
    except:
        print("fail")
        return "fail"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)