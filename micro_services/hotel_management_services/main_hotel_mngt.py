from  fastapi import FastAPI
from models.hotel_mgnt_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/room")
def main_get(data: Incoming_Data):
    return 'get room info'


@app.post("/room")
def main_post(data: Incoming_Data):
    return 'create room'


@app.put("/room")
def main_post(data: Incoming_Data):
    return 'put room'


@app.delete("/room")
def main_post(data: Incoming_Data):
    return 'delete room'














