
# Upgrade pip
`pip install -U pip`
or if "pip is undefined"
`python3 -m pip install -U pip`

# Install virtualenv
`pip install virtualenv`

# Create virtualenv
`virtualenv venv`

# Activate virtualenv
`source venv/bin/activate`

# Install requirements
`pip install -r requirements.txt`

# Tests
https://docs.djangoproject.com/en/2.2/intro/tutorial05/

# Django-Rest-Framework?
https://www.django-rest-framework.org
https://www.youtube.com/watch?v=TEOoxcASn1k

# CORS for development
https://www.youtube.com/watch?v=TEOoxcASn1k

# Angular integration
https://devarea.com/building-a-web-app-with-angular-django-and-django-rest/#.XYsK5y-HLUI

# Add to requirements
IMPORTANT WE DONT WANT REQUIREMENTS TO OUR REQUIREMENTS
`pip freeze > requirements.txt`


# Production
In settings fix following:\
`SECRET_KEY = 'ft*c^gqzv==7c17a_18ltje&^0vf)0=l&-t0wp-8x_6y4*g6jz'`\
Turn debug off: \
`DEBUG = True` to `DEBUG = False`\
Remove CORS:\
`CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
)`
