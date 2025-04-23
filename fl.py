from flask import Flask, render_template
import random

app = Flask("__name__")

@app.route("/")
def home():
    rnum = random.randint(100, 1000)
    return render_template("index.html", rnum = rnum)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)





