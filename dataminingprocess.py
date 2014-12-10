import os, json
from flask import Flask, render_template, request, make_response
from werkzeug import secure_filename
import csv
import sys
import glob

@app.route('/')
def index():
	return "Hello World!"

def words(stringIterable):
    #upcast the argument to an iterator, if it's an iterator already, it stays the same
    lineStream = iter(stringIterable)
    for line in lineStream: #enumerate the lines
        for word in line.split(): #further break them down
            yield word

@app.route('/generateDatabase')
def generateDatabase():
	dataFile = open("datafile.csv", "w")
	for filename in glob.iglob(os.path.join('refinedData', '*', '*.txt')):
		with open(filename) as txtfile:
			for line in txtfile:
				# print line,
				for word in line.split():
					print word
					dataFile.write( word + "," )
		dataFile.write("\n")
	return "Created dataFile!!"


if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5200,debug=True)