# CoRider_CRUD

Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API. The REST API endpoints should be accessible via HTTP requests

---

## Endpoints
- GET /users - Returns a list of all users.
- GET /users/<id> - Returns the user with the specified ID.
- POST /users - Creates a new user with the specified data.
- PUT /users/<id> - Updates the user with the specified ID with the new data.
- DELETE /users/<id> - Deletes the user with the specified ID.

---
## Setting up the Project

### Using the Dockerfile

The pre-requisite is that Docker must be installed on the system.
In order to run the web application using docker image, run the following command on the terminal

```

docker build -t <app_name>
docker run -p 4000:5000 <app_name>

```

---

### Without using the Dockerfile

In order to set up the project and run on your local system, follow the following steps:
- Step 1: Installing the dependencies

Run the following command on the terminal to install the required libraries. The minimum pre-requisite is `Python 3.8 and above`

```
pip install -r requirements.txt.

```

- Step 2: Creating mongoDB login utilities

    - Create a database user credential for your mongoDB Atlas database.

    - Create a `.env` file and put these as new environment variables.

    - Update the enivronment variables in the `database.py` file.

    - Update the cluster, database and collection names accroding to your mongoDB database.
    
    



- Step 3: Launching the flask server

Run the following command on the terminal with desired `<port_number>`

```
flask run -p <port_number>

```
