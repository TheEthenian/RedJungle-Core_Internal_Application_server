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
    return 'get audit logging'


@app.post("/audit")
def main_post(data: Incoming_Data):
    return 'post audit logging'


@app.delete("/audit")
def main_delete(data: Incoming_Data):
    return 'delete audit logging'










