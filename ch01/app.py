from flask import Flask, request

app=Flask(__name__)

@app.route('/')
def hi():
    a1=request.args.get('name')
    a2=request.args.get('age')
    return a1+a2+'world'
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001)
