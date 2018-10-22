# Alexa's Domains [The top 50 on the web](https://www.alexa.com/topsites)


Small application that return the top 50 site on the web that works  extracting data from Alexa.com and show it. 

Basic application who works with Django and BeautifulSoup.

## Requirements 
Python >= 3.4.3
PostgreSQL
Pip

## Setup environment

1. Create vitualenv and activate it
	```
	$ virtualenv -p python3 env
	$ source env/bin/activate 
	```

2. Install requirements
	```
	(env) Alexa$ pip install -r requirements.txt
	```


## Setup database:

1. Create 'alexa' database
	```
	$ sudo su - postgres
	postgres$ psql
	> CREATE DATABASE alexa;
	```

2. Create 'sirius' user with password 'alexa' and configure with djangs settings
	```
	> CREATE USER alexa WITH PASSWORD 'alexa';
	> ALTER USER alexa CREATEDB;
	```
	
3. Grant privileges to this user in the db
	```
	> GRANT ALL PRIVILEGES ON DATABASE alexa TO alexa;
	\q
	postgres$ exit
	```

## Database

```
	$ (env) cd Alexa
	$ (env) python manage.py migrate
```
## Run server
	```
	(env) Alexa$  python3 manage.py runserver
	```

## Run tests

Selenium test and unit test

Run in console, inside the Alexa carpet:
	 ```
	 (env) Alexa$ python manage.py test alexaDomain
	 ```

## Tips

1. When you run the app first you need to register
2. Then you can take any url that have a table un Alexa.com/topsites/ and put in the inpu url and then 'click ger information'
3. You will see in the right side all de pages and domain that has the url. 
4. You can click on details and you will see a modal with information
5. You can make click on the domain on the table of a row and you will go to the page. 
