from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import pymysql

app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

conn = pymysql.connect(host='localhost', user='mingyu', password='q1w2e3', db='study_db')
cur = conn.cursor() #SQL 문을 실행하거나 실행된 결과를 돌려받는 통로


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/on")
def led_on():
    try:
        GPIO.output(8, GPIO.HIGH)
        cur.execute("insert into record_led(status) values('{0}')".format("on"))
        conn.commit()
        return "ok"
    except:
        GPIO.output(LED, GPIO.LOW)
        return "fail"

@app.route("/off")
def led_off():
    try:
        GPIO.output(8, GPIO.LOW)
        cur.execute("insert into record_led(status) values('{0}')".format("off"))
        conn.commit()

        return "ok"
    except:
        return "fail"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
