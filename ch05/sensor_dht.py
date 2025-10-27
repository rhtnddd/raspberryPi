import adafruit_dht
import board

def get_now():
    sensor = adafruit_dht.DHT11(board.D14)
    try:
        temp = sensor.temperature
        hum = sensor.humidity
        sensor.exit()
        return [temp, hum]
    except RuntimeError as e:
        print(f"센서 읽기 오류: {e}")
        return [0, 0]