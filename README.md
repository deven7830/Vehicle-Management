# Vehicle-Management

1: Outside the root directory vehicle_management create a virtual environment.
2: Activate the Virtual Environment
3: cd vehicle_management, to go to the inner package directory where we have manage.py and requirements.txt files.
4: pip install -r requirements.txt
5: python manage.py makemigrations
6: python manage.py migrate
7: python manage.py runserver
8: Navigate to http://127.0.0.1:8000/

                      ## Existing Users In Database ##
                   Super_Admin = username:dev, password: qwerty@123
                   Admin = username:kajal, password: qwerty@123
                   User = username:kukku, password: qwerty@123


##For Testing##
python manage.py test

python manage.py test account
python manage.py test vehicle
