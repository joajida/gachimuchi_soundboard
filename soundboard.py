import pygame
import glob
from flask import Flask
import os
path=os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

pygame.mixer.init()

filenames=glob.glob(path+'/*.mp3')
print(filenames)
page=""
for name in filenames:
	relative=name.split('\\')[-1]
	page= page + "<a href='/play/%s'>%s</a><br>" % (relative,relative)
print(page)


@app.route("/")
def index():
	return page

@app.route("/play/<name>")
def play(name):
	pygame.mixer.music.load(name)
	pygame.mixer.music.play()
	return page



if __name__ == '__main__':
	app.debug = True
	app.run()