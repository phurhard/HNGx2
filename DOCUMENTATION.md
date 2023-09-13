# API performing CRUD operations on persons resource

## Setting up locally
Ensure you have python installed on your system, run
    
    
    apt upgrade
    apt update
    
 clone this repo
    
    git clone https://github.com/phurhard/HNGx2.git
    
cd into the repo
    
    cd HNGx2/
    
run
    
    pip -r install requirements.txt
    
to install required files/libraries
Great you're all set up, you can now run the flask server.
    
    python -m api.app
    
This will start the flask server amd create a database on your local machine.

## Standard formats
    The server/endpoints can be commumicated with by either using curl or any other known requests library.
    The following is the standars format for requests and the formats for the expected response.

    - POST *using curl
    *request
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "phurhard"}' http://localhost:5000/api
    ```
    *response
    ```bash
    {
         "id": "d5b5ee71-c9e0-4d55-a35d-aa88b42a6119",
         "name": "phurhard"
    }
    ```
    - **PUT *using curl
    *request
    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"name": "faster"}' http://127.0.0.1:5000/api/d5b5ee71-c9e0-4d55-a35d-aa88b42a6119
    ```
    *response
    ```bash
    {
      "id": "d5b5ee71-c9e0-4d55-a35d-aa88b42a6119",
      "name": "faster"
    }
    ```
    - **GET
    *request
    ```bash
    curl http://127.0.0.1:5000/api/d5b5ee71-c9e0-4d55-a35d-aa88b42a6119
    ```
    *response
    ```bash
    {
         "id": "d5b5ee71-c9e0-4d55-a35d-aa88b42a6119",                   "name": "New_name"                                         }
    ```
    - DELETE
    *request
    ```bash
    curl -X DELETE http://127.0.0.1:5000/api/d5b5ee71-c9e0-4d55-a35d-aa88b42a6119
    ```
    *response
    ```bash
    {}
    ```
## Sample usage
    The standard format[#standard_format] can also be used to view how the api emdpoints work.
    * Creating a user
    ```bash                                                         curl -X POST -H "Content-Type: application/json" -d '{"name": "phurhard"}' http://localhost:5000/api                            ```

