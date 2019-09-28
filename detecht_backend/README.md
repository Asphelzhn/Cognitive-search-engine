# Welcome to Detecht Backend
Here we will be using DJANGO to develop the frontend. 

### OBS
Everything that is going to be written in the terminal should be done inside the folder: \
`the-detecht-cognitive-search-engine/detecht_backend/`


## Getting started

### Install and update Python 3
To get started check if you have python3 installed on your computer, in terminal write
`python3`\
The version should be at least
`Python 3.4.0`\
If you dont have python3 or an older python3 installed please go to python.org and download the latest version. \

### Update pip
To update pip, in terminal write
`pip install -U pip`
or if "pip is undefined"
`python3 -m pip install -U pip`.\
If you get an error you may need to add the --user flag
`pip install -U pip -class` or `python3 -m pip install -U pip --user`

### Install and create virtualenv
#### Install virtualenv
In terminal write
`pip install virtualenv`

#### Create virtualenv
In terminal write
`virtualenv venv`

#### Activate virtualenv
In terminal write
`source venv/bin/activate`\
Or if you are on a windows computer
`venv\Scripts\activate`

### Install requirements
In project go to requrements.txt and press install\
Or in terminal write
`pip install -r requirements.txt`

### Check all is done correctly
In terminal write 
`git status`,
the last row should be \
`nothing to commit, working tree clean` \
If you do not have a clean working tree, please go directly to your teamleader before continue! \
\
Press the green play button and see that the sever is running and that you can access the website. 
Or write in terminal `python manage.py renserver 8000` to start the server on port 8000

## Code Standard

### Indentation style
All code shall be indented according to PyCharm standard. 

### Names
The name should be a clear description of what the component does, this should be done by 1-2 words.


## Workflow
See notes on drive about workflow.
For different cli commands see further down 

### Activate virtualenv
In terminal write
`source venv/bin/activate`\
Or if you are on a windows computer
`venv\Scripts\activate`

### Deactivate virtualenv
In terminal write
`deactivate`

### To serve the application 
Write in terminal
`ng serve`. 
Or press the green play button in the top right corner of WebStorm

#### To stop serve the application
In the terminal serving the application press Ctrl + C
Or press the red square up in the top right corner of WebStorm where the play-button were


## To install a module / library / package / etc. 
### Talk to your teamleader first
##### IMPORTANT WE DONT WANT REQUIREMENTS TO OUR REQUIREMENTS
In terminal write \
`pip install module-name`\
Look in requirements what the current requirements are, then write in terminal\
`pip freeze > requirements.txt`\
Look in requirements what the new requirements are, remove all new requirements that was made to the file except
the requirement that was just installed.

## Any questions?
Talk to your teamleader, who will gladly help or get help from others! :)


# Production
In settings fix following:\
`SECRET_KEY = 'ft*c^gqzv==7c17a_18ltje&^0vf)0=l&-t0wp-8x_6y4*g6jz'`\
Turn debug off: \
`DEBUG = True` to `DEBUG = False`\
Remove CORS:\
`CORS_ORIGIN_ALLOW_ALL = Falsegt
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
)`


# Test in DJANGO
https://docs.djangoproject.com/en/2.2/intro/tutorial05/

# Django-Rest-Framework
https://www.django-rest-framework.org
https://www.youtube.com/watch?v=TEOoxcASn1k

# CORS for development
https://www.youtube.com/watch?v=TEOoxcASn1k

# Angular integration
https://devarea.com/building-a-web-app-with-angular-django-and-django-rest/#.XYsK5y-HLUI



