from flask import Flask, render_template, url_for
import os

app = Flask(__name__)


@app.route('/')
def main():
	return render_template('home.html')

@app.route('/webgazer.html')
def webgazer():
    return render_template('webgazer.html')

@app.route('/gazerecorder.html')
def gazerecorder():
    return render_template('gazerecorder.html')

if __name__ == "__main__":
    app.run(ssl_context='adhoc')
