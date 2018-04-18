# Bus_BTP
Backend for Bus booking system in Django

## Installation
1. clone the project 
`git clone https://github.com/aarushverma96/Bus_BTP.git`
2. cd to the project directory 
`cd Bus_BTP` and create virtual environment 
`virtualenv venv`
3. activate virtual environment 
`. venv/bin/activate`
 `cd btp`
4. `pip install -r requirements.txt`
5. `python manage.py makemigrations`
6. `python manage.py migrate`
7. `python manage.py runserver`
8. To use admin create super user 
`python manage.py createsuperuser`

## REST API
1. Accessing Bus Information 
`127.0.0.1:8000/jbuses/<source>/<destination>`<br>
	<b>Examples</b>
	`http://127.0.0.1:8000/JP/DLE`

2. Acessing status information
`http://127.0.0.1:8000/jstsus/<busID>`<br>
	<b>Example</b>
	`http://127.0.0.1:8000/123`

## Application 
1. Search Functionality
	`127.0.0.1:8000/search/`
2. Then follow the flow of application.