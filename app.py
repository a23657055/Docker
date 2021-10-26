 # !/usr/bin/python
 # coding:utf-8
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """<h1>Hello Flask</h1>
<p>建立 Dockerfile 執行 Flask</p>
"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8888")