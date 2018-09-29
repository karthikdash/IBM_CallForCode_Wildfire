from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
serviceUsername = "ac99bfe8-c64e-48a5-9f62-e3b7c44ba586-bluemix"
servicePassword = "c3809deee19c50d976b3c0536508a1762322d6f903cc6d4369a6ed4a53a9e475"
serviceURL = "https://ac99bfe8-c64e-48a5-9f62-e3b7c44ba586-bluemix:c3809deee19c50d976b3c0536508a1762322d6f903cc6d4369a6ed4a53a9e475@ac99bfe8-c64e-48a5-9f62-e3b7c44ba586-bluemix.cloudant.com"
client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()
databaseName = "databasedemo"
myDatabaseDemo = client.create_database(databaseName)
if myDatabaseDemo.exists():
        print "'{0}' successfully created.\n".format(databaseName)
# Create documents using the sample data.
# Go through each row in the array
sampleData = [
    [1, "one", "boiling", 100],
    [2, "two", "hot", 40],
    [3, "three", "warm", 20],
    [4, "four", "cold", 10],
    [5, "five", "freezing", 0]
]
# Create documents using the sample data.
# Go through each row in the array
for document in sampleData:
    # Retrieve the fields in each row.
    number = document[0]
    name = document[1]
    description = document[2]
    temperature = document[3]

    # Create a JSON document that represents
    # all the data in the row.
    jsonDocument = {
        "numberField": number,
        "nameField": name,
        "descriptionField": description,
        "temperatureField": temperature
    }

    # Create a document using the Database API.
    newDocument = myDatabaseDemo.create_document(jsonDocument)

    # Check that the document exists in the database.
    if newDocument.exists():
        print "Document '{0}' successfully created.".format(number)
