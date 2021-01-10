from flask import Flask
from flask import request, jsonify
from PIL import Image
import io

import numpy
import requests
import time
import json
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def hello_World():
	return jsonify(isError="false",
				message= "Hello spam logo detector",
				statusCode= 200), 200


@app.route('/images',methods=['GET','POST','DELETE','PATCH'])
def show_user_profile():
	if request.method == 'GET':
		data = "getting info"
		return jsonify(isError= False,
					message= "Success",
					data=data,
					statusCode= 200), 200
	
	if request.method == 'POST':
		if ("imagecapture" in request.files):
			image = Image.open(request.files["imagecapture"])
			print(image.format)
			if (image.format == "JPEG"):
				
				captureRes = {'isErrorCapture':'false',
					  'messageCapture':'Success capture detection',
					  'dataCapture':'ok image was taken',
					  'detected_logo': 'logo',					  
					  'reslogoCapture':{'good_maches': 1356,
                                    'match': 87.20257234726688},
					  'statusCodeCapture':200}

			else:
				captureRes = {'isErrorCapture':'true',
					  'messageCapture':'requered jpg image',					  
					  'statusCodeCapture':400}
		else:
			captureRes = {'isErrorCapture':'true',
					  'messageCapture':'An image input is required',					  
					  'statusCodeCapture':400}

	

	data = {'capturepred':captureRes}
	return json.dumps(data), 200


if __name__ == '__main__':
    app.run()