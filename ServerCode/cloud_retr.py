from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
serviceUsername = "ac99bfe8-c64e-48a5-9f62-e3b7c44ba586-bluemix"
servicePassword = "c3809deee19c50d976b3c0536508a1762322d6f903cc6d4369a6ed4a53a9e475"
serviceURL = "https://ac99bfe8-c64e-48a5-9f62-e3b7c44ba586-bluemix:c3809deee19c50d976b3c0536508a1762322d6f903cc6d4369a6ed4a53a9e475@ac99bfe8-c64e-48a5-9f62-e3b7c44ba586-bluemix.cloudant.com"
client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()
databaseName = "sensordbs"
myDatabaseDemo = client.create_database(databaseName)
result_collection = Result(myDatabaseDemo.all_docs, include_docs=True)
# print len(result_collection)
print "Retrieved minimal document:\n{0}\n".format(result_collection[0])
print "Retrieved minimal document:\n{0}\n".format(result_collection[1])
print "Retrieved minimal document:\n{0}\n".format(result_collection[2])
print "Retrieved minimal document:\n{0}\n".format(result_collection[3])
