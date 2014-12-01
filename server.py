import os
<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('landing-page.html')
    # return 'Hello World!'

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5000,debug=True)
=======
from flask import Flask

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route("/")
def hello():
    return "Hello from Python!"

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
>>>>>>> 4c4322e1db1d6a433e9e792205f474cbb28b7e8d
