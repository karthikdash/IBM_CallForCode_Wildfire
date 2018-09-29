import flask
from flask import request, jsonify
import serial
import RPi.GPIO as GPIO
import time
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

app = flask.Flask(__name__)



#1 Create some test data for our catalog in the form of a list of dictionaries.
books = [
            {'id': 0,
                     'latitude': '42.445278',
                          'longtitude': '-76.481651',
                               'color': '#e67e22',
                                    'Safe': 'false'},
                {'id': 1,
                         'latitude': '42.445518',
                              'longtitude': '-76.479830',
                                   'color': '#c0392b',
                                        'Safe': 'false'},
]

l1 = {'id': 0,
                     'latitude': '42.445278',
                          'longtitude': '-76.481651',
                               'color': '#e67e22',
                                    'Safe': 'false'}
l2 = {'id': 0,
                     'latitude': '42.445518',
                          'longtitude': '-76.479830',
                               'color': '#e67e22',
                                    'Safe': 'false'}


@app.route('/', methods=['GET'])
def home():
	

	return '''<h1>Distant Reading Archive</h1>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
	ser = serial.Serial("/dev/ttyACM0", 9600)
	ser.baudrate = 9600
	temp1 = ser.readline()
	# temp1 = 20
	ser = serial.Serial("/dev/ttyACM1", 9600)
	ser.baudrate = 9600
	temp2 = ser.readline()
	# temp2 = 20
	print temp1, temp2
	if int(temp1[0:2]) < 35:
	# if temp1 < 35: 

		books[0]['color'] = "#2ecc71"
		books[0]['Safe'] = "true"
	else:
		books[0]['color'] = "#c0392b"
		books[0]['Safe'] = "false"
	# if temp2 < 35: 
	if int(temp2[0:2]) < 35: 
		books[1]['color'] = "#2ecc71"
		books[1]['Safe'] = "true"
	else:
		books[1]['color'] = "#c0392b"
		books[1]['Safe'] = "false"

	return jsonify(books)
def looping():
	while  True:
		time.sleep(5)
		ser = serial.Serial("/dev/ttyACM0", 9600)
		ser.baudrate = 9600
		temp1 = ser.readline()
		# temp1 = 20
		ser = serial.Serial("/dev/ttyACM1", 9600)
		ser.baudrate = 9600
		temp2 = ser.readline()
		# temp2 = 20
		print temp1, temp2
		if int(temp1[0:2]) < 35:
		# if temp1 < 35: 

			l1['color'] = "#2ecc71"
			l1['Safe'] = "true"
		else:
			l1['color'] = "#c0392b"
			l1['Safe'] = "false"
		# if temp2 < 35: 
		if int(temp2[0:2]) < 35: 
			l2['color'] = "#2ecc71"
			l2['Safe'] = "true"
		else:
			l2['color'] = "#c0392b"
			l2['Safe'] = "false"
		serviceUsername = "ac99bfe8-c64e-48a5-9f62-e3b7c44ba586-bluemix"
		servicePassword = "c3809deee19c50d976b3c0536508a1762322d6f903cc6d4369a6ed4a53a9e475"
		serviceURL = "https://ac99bfe8-c64e-48a5-9f62-e3b7c44ba586-bluemix:c3809deee19c50d976b3c0536508a1762322d6f903cc6d4369a6ed4a53a9e475@ac99bfe8-c64e-48a5-9f62-e3b7c44ba586-bluemix.cloudant.com"
		client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
		client.connect()
		databaseName = "sensordbs"
		try :
			client.delete_database(databaseName)
		except CloudantException:
			print "There was a problem deleting '{0}'.\n".format(databaseName)
		else:
			print "'{0}' successfully deleted.\n".format(databaseName)  
		myDatabaseDemo = client.create_database(databaseName)
		if myDatabaseDemo.exists():
			print "'{0}' successfully created.\n".format(databaseName)
		newDocument = myDatabaseDemo.create_document(l1)
		newDocument = myDatabaseDemo.create_document(l2)

		# Check that the document exists in the database.
		if newDocument.exists():
			print "Document"
if __name__ == '__main__':
	looping()
	app.run(host='192.168.43.233')

