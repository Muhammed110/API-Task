import requests

BASE_URL = "https://reqres.in/"  # This is the base URL used for all requests
HEADERS = {  # Used to inform what type of data is expected
    'accept': 'application/json',
    'Content-Type': 'application/json',
}


#Question 1
def successful_login(user_email, user_password):
    """
          Documentation: This function uses the provided user user_email and user_password to login
          using python's requests library (POST method). It sends email, password credentials.This function
          returns the response data (login token, response status code) from the request in tuple format.

          parameters:
            user_email: The user email for login
            user_password: The user password for login

          returns:
            response_token: The response token from login request.
            response_status_code: Response status code from registration request.
    """
    relative_url = "api/login"
    url = BASE_URL + relative_url
    data = {'email': user_email, 'password': user_password}
    response = requests.request("POST", url, headers=HEADERS, json=data)
    response_token = response.json()['token']
    return response_token, response.status_code

#Question 2
def create_user(user_name, user_job):
    """
          Documentation: This function uses the provided user_name and user_job to post a request
          using python's requests library (POST request). It Creates a new user with the given
          parameters.This function only returns the data with the given path you provide in (tuple format).

          parameters:
            user_name:  The new user name to create for a user
            user_job:   The new job to create for a user

          returns:
            created_name: The received name from the response after posting the request.
            created_job: The received job from the response after posting the request.
            response_status_code: Response status code from the request.
    """
    relative_url = "api/users"
    url = BASE_URL + relative_url
    data = {'name': user_name, 'job': user_job}
    response = requests.request("POST", url, json=data, headers=HEADERS)
    created_name = response.json()['name']
    created_job = response.json()['job']
    response_status = response.status_code
    return created_name, created_job, response_status
#Question 3
def update_user(ID, user_name, user_job):
    """
          Documentation: This function uses the provided user ID to update a specific user
          using python's requests library (PUT method). The user's credentials are updated with
          the given parameters (user_name, user_job). This function returns the response data
          (name, job) from the request in tuple format.

          parameters:
            ID:  The specific user id to updates his data
            user_name:  The new user name to create for a user
            user_job:   The new job to create for a user

          returns:
            updated_name: The updated name from the response after posting the request.
            updated_job: The updated job from the response after posting the request.
            response_status_code: Response status code from the request.
    """
    relative_url = "api/users/"
    url = BASE_URL + relative_url + str(ID)
    data = {'name': user_name, 'job': user_job}
    response = requests.request("PUT", url, headers=HEADERS, json=data)
    updated_name = response.json()['name']
    updated_job = response.json()['job']
    response_status = response.status_code
    return updated_name, updated_job, response_status

#Question 4
def delete_user(Id):
    """
          Documentation: This function uses the provided user ID to delete a specific user
          using python's requests library (DELETE method). This function returns the response
          status code.

          parameters:
            ID:  The specific user id to delete.

          returns:
            response_status_code: Response status code from the request.
    """
    relative_url = "api/users/"
    url = BASE_URL + relative_url + str(Id)
    response = requests.request("DELETE", url, headers=HEADERS)
    return response.status_code
