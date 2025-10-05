from  fastapi import FastAPI
from models.access_control_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/{param_a}")
def main_get(param_a, data: Incoming_Data):

    if param_a == 'role':
        return 'get role'

    if param_a == 'policy':
        return 'get policy'


@app.post("/{param_a}")
def main_get(param_a, data: Incoming_Data):

    if param_a == 'role':
        return 'post role'

    if param_a == 'policy':
        return 'post policy'


@app.put("/{param_a}")
def main_get(param_a, data: Incoming_Data):

    if param_a == 'role':
        return 'put role'

    if param_a == 'policy':
        return 'put policy'


@app.delete("/{param_a}")
def main_get(param_a, data: Incoming_Data):

    if param_a == 'role':
        return 'delete role'

    if param_a == 'policy':
        return 'delete policy'



