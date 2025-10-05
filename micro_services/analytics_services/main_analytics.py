from  fastapi import FastAPI
from models.analytics_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/analytic")
def main_get(data: Incoming_Data):
    return 'get analytic'


@app.post("/analytic")
def main_post(data: Incoming_Data):
    return 'post analytic'


@app.delete("/analytic")
def main_delete(data: Incoming_Data):
    return 'delete analytic'






