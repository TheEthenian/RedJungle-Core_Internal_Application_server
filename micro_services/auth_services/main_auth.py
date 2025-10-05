from  fastapi import FastAPI
from models.auth_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/auth")
def main_get(data: Incoming_Data):
    return 'get auth'


@app.post("/auth")
def main_post(data: Incoming_Data):
    return 'post auth'


@app.put("/auth")
def main_put(data: Incoming_Data):
    return 'put auth'


@app.delete("/auth")
def main_delete(data: Incoming_Data):
    return 'delete auth'








