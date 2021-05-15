from flask import Flask, render_template, url_for
import os

app = Flask(__name__)


@app.route('/')
def main():
	return render_template('home.html')
