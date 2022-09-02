First, create the virtual environment by the given command: 
`virtualenv -p python3 <envname>`, 

After creating the virtual environment activate it by the given command:
`source <envname>/bin/activate`

Then install the required libraries available in the requirements.txt file. 
Command to install requirements.txt file is given below. 
`pip install -r requirements.txt`

Now run migrations. 
`python manage.py migrate`

run django server by using command below: 
`python manage.py runserver`,
Then go to the server url.

If you want to check data in the admin panel run the command given below.
`python manage.py createsuperuser`
Provide username email and password. By using this creadentials you can login in admin panel.
you can open admin page on the url given below:
`http://127.0.0.1:8001/admin`

Note:Use Postman for hitting the url

Register a user by hitting the url given below: 
`http://127.0.0.1:8001/user/register/`

After Registering the user hit the below url to generate the Authentication token:
`http://127.0.0.1:8001/api/token/`
Note:-please provide username and password in the body.

To retrieve, update and delete use the url given below:
`http://127.0.0.1:8001/user/retrieve_update_destroy/<user_id>/`

eg:`http://127.0.0.1:8001/user/retrieve_update_destroy/1/`
Note:-please use methods accordingly.


For creating the new Project hit url given below:
`http://127.0.0.1:8000/project/`
Note:-please provide title and description in the body and token in Authorization with method POST.

For list all the Projects hit url given below:
`http://127.0.0.1:8000/project/`
Note:-please use GET method.

To get, update and delete the Projects hit url given below:
`http://127.0.0.1:8000/project/<porject_id>/`

eg:`http://127.0.0.1:8000/project/1/`
Note:-please use methods accordingly.

To create the new Timelog hit url given below:
`http://127.0.0.1:8000/timelog/`
Note:-please provide project, date, status, hours and description in the body and token in Authorization with method POST.

To list all the Timelog hit url given below:
`http://127.0.0.1:8000/timelog/`
Note:-please use GET method.

To get, update and delete the Timelog hit url given below:
`http://127.0.0.1:8000/timelog/timelog_id>/`

eg:`http://127.0.0.1:8000/timelog/1/`
Note:-please use methods accordingly.

To run the testcases run the below command in the terminal:
`python manage.py test`