from  fastapi import FastAPI
from models.audit_logging_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/audit")
def main_get(data: Incoming_Data):
    respond = {
        "endpoint": 'get audit logging',
        "echo_data": data
    }
    return  respond


@app.post("/audit")
def main_post(data: Incoming_Data):
    respond = {
        "endpoint": 'post audit logging',
        "echo_data": data
    }
    return  respond


@app.delete("/audit")
def main_delete(data: Incoming_Data):
    respond = {
        "endpoint": 'delete audit logging',
        "echo_data": data
    }
    return  respond










