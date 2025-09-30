from  fastapi import FastAPI
from models import admin_models as structure
import sqlalchemy
import psycopg2
import requests 
import json

#####################################################################

app = FastAPI()

#####################################################################


#####################################################################


@app.get("/{param_a}")
def main_get(param_a):
    
    if param_a == 'hotel':
        return 'get hotel'

    if param_a == 'hotel-service':
        return 'get hotel service'

    if param_a == 'staff':
        return 'get staff'

    if param_a == 'admin':
        return 'get admin'


@app.post("/{param_a}")
def main_post(param_a):
    
    if param_a == 'hotel':
        return 'post hotel'

    if param_a == 'hotel-service':
        return 'post hotel service'

    if param_a == 'staff':
        return 'post staff'

    if param_a == 'admin':
        return 'post admin'



@app.put("/{param_a}")
def main_put(param_a):
    
    if param_a == 'hotel':
        return 'put hotel'

    if param_a == 'hotel-service':
        return 'put hotel service'

    if param_a == 'staff':
        return 'put staff'

    if param_a == 'admin':
        return 'put admin'



@app.delete("/{param_a}")
def main_delete(param_a):
    
    if param_a == 'hotel':
        return 'delete hotel'

    if param_a == 'hotel-service':
        return 'delete hotel service'

    if param_a == 'staff':
        return 'delete staff'

    if param_a == 'admin':
        return 'delete admin'













