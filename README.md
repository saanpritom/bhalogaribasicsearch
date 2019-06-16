Requirements for this project to run:
1. Python Version -> 3.6 or higher
2. Django Framework -> 2
3. Django Rest Framework
4. SQLite as the Database

Rest of the package requirements will be found on requirements.txt file

Instruction to setup and run the project
1. Create a python virtual environment with the mentioned python version or above
2. Activate the Virtual environment
3. Install or update the pip to the latest one
4. run the following command to install all the dependencies 'pip install -r requirements.txt'
5. If your django deployment is running on the 'http//:127.0.0.1:8000' url then you do not need to configure anything. Otherwise just
   change the base_url on apps/searchapp/configs.py file
6. Now run the following command 'python manage.py runserver'
7. You will see the project on your default django deployment

Instruction to operate the project:
1. The application is decoupled. Means there are particularly two apps. One app called the 'searchapp' is responsible for the
   REST API Endpoints Generation and the other app called the 'apiconsumer' is responsible for consuming and showing the results
2. You will find all the links of the client app on 'Application Links' dropdown
3. All the APIs are Browsable so you may browse them on 'Browsable API' dropdown
4. All datas are dummy and inserted using a Python Library called Faker.
