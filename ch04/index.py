from flask import Flask, request, render_template, jsonify
import RPi.GPIO as GPIO
from time import sleep
import pymysql
import atexit

app = Flask(__name__)
PIN = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

servo = GPIO.PWM(PIN, 50)
servo.start(0)

@atexit.register
def cleanup():
    servo.stop()
    GPIO.cleanup()

def set_angle(angle):
    duty = 2.5 + 10 * angle / 180
    servo.ChangeDutyCycle(duty)
    sleep(0.5)
    servo.ChangeDutyCycle(0)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/rotate", methods=["POST"])
def rotate():
    try:
        data = request.get_json()
        angle = int(data.get("angle", 0))
        if not (0 <= angle <= 180):
            return jsonify({"status": "error", "msg": "각도는 0~180 사이여야 합니다."}), 400

        set_angle(angle)
        return jsonify({"status": "ok", "angle": angle})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500

@app.route("/send", methods=["POST"])
def send_route():
    data = request.get_json()
    try:
        conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study')
        cur = conn.cursor()
        cur.execute("INSERT INTO numcount(num) VALUES (%s)", (data.get("value"),))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
