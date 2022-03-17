import urllib.request,json
from .models import Weather
from urllib import response


# Getting api key
api_key = None

# Getting the blog base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MAIL_SENDGRID_API_KEY']
    base_url = app.config['MAIL_DEFAULT_SENDER']
