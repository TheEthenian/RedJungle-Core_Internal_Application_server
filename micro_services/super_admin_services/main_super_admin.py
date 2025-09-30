from  fastapi import FastAPI
from models import super_admin_models as structure
import sqlalchemy
import psycopg2
import requests 
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/{param_a}")
def main_get(param_a):

    if param_a == 'tenant':
        return 'get tenant'

    if param_a == 'super-admin':
        return 'get super-admin'

    if param_a == 'billing':
        return 'get billing'



@app.post("/{param_a}")
def main_post(param_a):

    if param_a == 'tenant':
        return 'post tenant'

    if param_a == 'super-admin':
        return 'post super-admin'

    if param_a == 'billing':
        return 'post billing'



@app.put("/{param_a}")
def main_put(param_a):

    if param_a == 'tenant':
        return 'put tenant'

    if param_a == 'super-admin':
        return 'put super-admin'

    if param_a == 'billing':
        return 'put billing'



@app.delete("/{param_a}")
def main_delete(param_a):

    if param_a == 'tenant':
        return 'delete tenant'

    if param_a == 'super-admin':
        return 'delete super-admin'

    if param_a == 'billing':
        return 'delete billing'











