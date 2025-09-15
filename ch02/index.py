from flask import Flask, render_template, redirect, url_for,request
import pymysql
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/junsong",methods=["POST"])
def send():
    data=request.get_json()
    print(data.get("value"))
    conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study')
    cur = conn.cursor()
    cur.execute(f"insert into numcount(num) VALUES ({data.get("value")})")
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
