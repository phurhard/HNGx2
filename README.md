# HNG STAGE 2 TASK BACKEND
* API capable of performing CRUD operations on a person resource.
## Introduction
This is a simple API with endpoints for CRUD operations on a person resource.
run this [test.py](test.py) to test the Endpoints.
     
     
### How to run.
Ensure you have python downloaded on your system, you can download python at (www.python.org) or run
     
     
     sudo apt install python.python3
     
this will install python on your system, the run
     
     
     pip -r install requirements.txt
     
this will install all neccessary libraries 

type


    python -m api.app


from the root directory i.e HNGx/ to start the server

run the [test.py](test.py) file to get a feel of the API

### How to use
The endpoints can be accessed by making API calls to the endpoints and working with the data recieved,
in order to work with this endppint, its required that the data to be sent by payload is of json format/ python dictionary.
The response is always in json. e.g

```
>> import requests
>> data = {
            'name': 'phurhard'
            }
>> r = requests.post('https:url.com/api', json=data)
>> r.status_code
.. 201
>> r.json()
.. {
    'name': 'phurhard',
    'id': "e36fec46-42d5-4284-8040-3cd23845ce62",
    'created': "2023-09-13 18:32:40.097312"
    }
```
the name of the user can used for all other CRUD operations.

