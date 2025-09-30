from  fastapi import FastAPI
from models import booking_models as structure
import sqlalchemy
import psycopg2
import requests 
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/{param_a}")
def main_get(param_a):

    if param_a == 'guest':
        return 'get guest here'

    if param_a == 'booking':
        return 'get booking here'

    if param_a == 'invoice':
        return 'get invoice here'

    if param_b == 'quick-booking':
        return 'get quick booking here'


@app.post("/{param_a}")
def main_post(param_a):

    if param_a == 'guest':
        return 'post guest here'

    if param_a == 'booking':
        return 'post booking here'

    if param_a == 'invoice':
        return 'post invoice here'


@app.delete("/{param_a}")
def main_delete(param_a):

    if param_a == 'guest':
        return 'delete guest here'

    if param_a == 'booking':
        return 'delete booking here'

    if param_a == 'invoice':
        return 'delete invoice here'












