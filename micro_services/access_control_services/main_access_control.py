from  fastapi import FastAPI
from models import access_control_models as structure
import sqlalchemy
import psycopg2
import requests 
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/{param_a}")
def main_get(param_a):

    if param_a == 'role':
        return 'get role'

    if param_a == 'policy':
        return 'get policy'


@app.post("/{param_a}")
def main_get(param_a):

    if param_a == 'role':
        return 'post role'

    if param_a == 'policy':
        return 'post policy'


@app.put("/{param_a}")
def main_get(param_a):

    if param_a == 'role':
        return 'put role'

    if param_a == 'policy':
        return 'put policy'


@app.delete("/{param_a}")
def main_get(param_a):

    if param_a == 'role':
        return 'delete role'

    if param_a == 'policy':
        return 'delete policy'



