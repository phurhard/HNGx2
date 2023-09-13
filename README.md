# HNG STAGE 2 TASK BACKEND
* API capable of performing CRUD operations on a person resource.
## Introduction
     This is a simple API with endpoints for CRUD operations on a person resource.
     run this (test.py)[file] to test the Endpoints.
     <fil
     
### How to run.
     Ensure you have python downloaded on your system, you can download python at (www.python.org) or run
     ```bash
     sudo apt install python.python3
     ```
     this will install python on your system, the run
     ```bash
     pip -r install requirements.txt
     ```
     this will install all neccessary libraries 

     type
    ```bash
    python -m api.app
    ```
    from the root directory i.e HNGx/
    ```bash
    python app.py
    ``` from the folder directory i.e ../api/

### How to use
The endpoints can be accessed by making API calls to the endpoints and working with the data recieved,
in order to work with this endppint, its required that the data to be sent by payload is of json format/ python dictionary.
The response is always in json. e.g>
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
    'id': "e36fec46-42d5-4284-8040-3cd23845ce62"
    }
```
the id returned from the post call is used to make all other requests. using /api/user_id

