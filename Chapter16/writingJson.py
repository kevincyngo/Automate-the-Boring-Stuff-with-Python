import json

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

#Dumps translates Python value into a string of JSON-formatted data
stringOfJsonData = json.dumps(pythonValue)
