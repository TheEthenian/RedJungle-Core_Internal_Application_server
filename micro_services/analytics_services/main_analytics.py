from  fastapi import FastAPI
from models import analytics_models as structure
import sqlalchemy
import psycopg2
import requests 
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/analytic")
def main_get(something):
    return 'get analytic'


@app.post("/analytic")
def main_post(something):
    return 'post analytic'


@app.delete("/analytic")
def main_delete(something):
    return 'delete analytic'






