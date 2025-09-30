from  fastapi import FastAPI
from models import audit_logging_models as structure
import sqlalchemy
import psycopg2
import requests 
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/audit")
def main_get(something):
    return 'get audit logging'


@app.post("/audit")
def main_post(something):
    return 'post audit logging'


@app.delete("/audit")
def main_delete(something):
    return 'delete audit logging'










