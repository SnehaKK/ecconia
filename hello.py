import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')
    # return 'Hello World!'
@app.route('/about')
def aboutUs():
	return render_template('about.html')

@app.route('/services')
def services():
	return render_template('services.html')

@app.route('/details')
def details():
	return render_template('portfolio-item.html')

@app.route('/generalChart')
def genCharts():
	return render_template('chartGeneral.html')

@app.route('/heatmaps')
def heatMaps():
	return render_template('heatmaps.html')

@app.route('/highChart')
def highCharts():
	return render_template('highChart.html')

@app.route('/charts')
def charts():
	return render_template('charts.html')

@app.route('/kmeans')
def kmeans():
	return render_template('kmeansOutput.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')


if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5000,debug=True)