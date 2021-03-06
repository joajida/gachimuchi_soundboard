import glob
from flask import Flask, request, render_template
import os
assets=os.path.dirname(os.path.abspath(__file__))+'/static/music/'

app = Flask(__name__)

@app.route("/")
def index():
	dirs=[d for d in os.listdir(assets)]
	files=[(fold,f) for fold in dirs for f in os.listdir(assets+fold)]
	files.sort(key=lambda x:"".join(x).lower())
	length=len(files)
	return render_template('index.html',
		title='List',
		length=length,
		files=files,
		assets=assets)

if __name__ == '__main__':
	app.debug = True
	app.run()
