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
`http://127.0.0.1:8000/jstaus/<busID>`<br>
	<b>Example</b>
	`http://127.0.0.1:8000/123`

3. PUT request 
	view name: test
	`url : http://127.0.0.1:8000/test/<bus_id>`

## Application 
1. Search Functionality
	`127.0.0.1:8000/search/`
2. Then follow the flow of application.

## Seat Structure changes
1. Models.py change in line #21 -- values are stored in CSV format
2. Views.py changes in function booking -- starting line# 61
3. To book enter seats in CSV format in `booking/<busid>` url

## Delete Reserved seats 
1. PUT request
2. URL format `127.0.0.1:8000/delete/<busid>`
3. Data format <br>
`
{
	'bus_id': 123
	'seats': '1,2,3,4'
}`
4. Function will return seat updated seat stucture

