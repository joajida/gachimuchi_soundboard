import glob
from flask import Flask, request, render_template
import os
assets=os.path.dirname(os.path.abspath(__file__))+'/static/music/'

app = Flask(__name__)

@app.route("/")
def index():
	files=[f for f in os.listdir(assets)if f.endswith('mp3')]
	length=len(files)
	return render_template('index.html',
		title='List',
		length=length,
		files=files,
		assets=assets)
"""
@app.route("/<filename>")
def play(filename):
	return render_template('play.html',
		title=filename,
		file=filename)
"""


if __name__ == '__main__':
	app.debug = True
	app.run()