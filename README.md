# Django Rest API
Technologies: Python, Django, GitHub Actions

#### 1) Making a CRUD REST API using the rest framework library

   The application must implement the API:
      
    GET /persons/{personId} – information about a person;
    GET /persons - information on all people;
    POST /persons - create a new record about a person;
    PATCH /persons/{personId} - update an existing person record;
    DELETE /persons/{personId} – deleting a person entry.

###### Read more: <https://rsoi-person-service.herokuapp.com/swagger-ui.html>
#### 2) Making a small CRUD page.
#### 3) Writing 5 unit tests for implemented functions
#### 4) GitHub Actions is used for testing and deployment
## Read more
##### API
1) Requests/responses in JSON format
2) If the record by id is not found, then HTTP status 404 Not Found is returned
3) When creating a new person record (POST /person method), HTTP status 201 Created is returned with an empty body and Header "Location: https://rsoi-person-service.herokuapp.com/persons/{personId}", where personId – id of the created entry.
##### GitHub Actions
1) Deploy to Heroku
2) Full automation of the testing and deployment process
