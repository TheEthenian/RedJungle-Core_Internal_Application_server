from  fastapi import FastAPI
from models import payment_gateway_models as structure
import sqlalchemy
import psycopg2
import requests 
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/{param_a}")
def main_get(param_a):

    if param_a == 'transaction':
        return 'get transaction'

    if param_a == 'payment-method':
        return 'get payment-method'



@app.post("/{param_a}")
def main_post(param_a):

    if param_a == 'transaction':
        return 'post transaction'

    if param_a == 'payment-method':
        return 'post payment-method'



@app.put("/payment-method}")
def main_put():
    return 'put payment-method'



@app.delete("/{param_a}")
def main_delete(param_a):

    if param_a == 'transaction':
        return 'delete transaction'

    if param_a == 'payment-method':
        return 'delete payment-method'












