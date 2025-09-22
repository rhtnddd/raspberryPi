from flask import Flask, request, render_template, jsonify
import random
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

led_pins = [8, 10, 12]
GPIO.setmode(GPIO.BOARD)
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

game_results = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random_leds():
    sequence = [1, 2, 3]
    random.shuffle(sequence)

    for num in sequence:
        pin = led_pins[num - 1]
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.5)

    return render_template("index.html", sequence=sequence)


@app.route("/submit_sequence", methods=['POST'])
def submit_sequence():
    try:
        data = request.get_json()
        sequence = data.get('sequence', [])

        color_to_num = {'red': 1, 'yellow': 2, 'green': 3}
        sequence_nums = [color_to_num.get(color, 0) for color in sequence]

        for num in sequence_nums:
            if num > 0:
                pin = led_pins[num - 1]
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(pin, GPIO.LOW)
                time.sleep(0.3)

        game_result = {
            'sequence': sequence,
            'sequence_nums': sequence_nums,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        game_results.append(game_result)

        return jsonify({
            'success': True,
            'message': f'입력된 순서: {" → ".join(sequence)}',
            'received_sequence': sequence
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'message': '처리 중 오류가 발생했습니다.'
        }), 500


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", debug=True)
    finally:
        GPIO.cleanup()