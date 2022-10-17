## Python Flask Backend for Notes App / SQLite Database server


Instructions for Mac

Open VS Code
New folder <flask directory name>
New file “app.py”
Open terminal
$ pipenv shell
$ pipenv install flask flask_sqlalchemy flask_marshmallow 
$ python3
>>> from app import db
>>> from app import app
>>> with app.app_context():
>>>     db.create_all()
(NOTE: be sure to indent step 12 and hit enter more than once to get code to execute)

CTRL^ + Z to exit shell
$ python3 app.py

Default server at: http://127.0.0.1:5000

Test the routes w/ Postman


