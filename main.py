from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def main():
	return render_template('home.html')
