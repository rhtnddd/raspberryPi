from flask import Flask, request, render_template, jsonify
import db_model
import sensor_dht
app = Flask(__name__)
@app.route("/")
def home():
  return render_template("index.html")

@app.route('/api/now')
def insertdb():
    temp, hum = sensor_dht.get_now()
    result = db_model.add(temp, hum)
    return result

@app.route('/api/record')
def selectAll():
    result = db_model.find_all()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")