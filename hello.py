from flask import Flask, render_template,url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('home.html')
@app.route('/fillthevoid')
def fillthevoid():
    return render_template('fillthevoid.html',)
@app.route('/drift')
def drift():
    # return render_template('templates.html')
    image_file = url_for('static', filename='DRIFT.jpg')
    return render_template("drift.html", title="DRIFT",image_file=image_file)
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html',)