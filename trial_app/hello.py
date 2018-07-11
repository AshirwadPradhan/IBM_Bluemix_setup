from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
	return "<h1>Hello World using IBM Cloud</h1> <p> Team KitKat </p>"

port = os.getenv('VCAP_APP_PORT', '5000')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(port), debug=True)