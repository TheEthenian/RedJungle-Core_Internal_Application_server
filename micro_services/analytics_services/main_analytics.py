from  fastapi import FastAPI
from models.analytics_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.get("/analytic/{param_a}")
def main_get(param_a,data: Incoming_Data):
    if param_a == 'event-log':
        respond = {
            "endpoint_echo":"get event log",
            "data": data
        }
        return respond

    if param_a == 'metric':
        respond = {
            "endpoint_echo":"get metric",
            "data": data
        }
        return respond


@app.post("/analytic/event-log")
def main_post(data: Incoming_Data):
    respond = {
        "endpoint_echo":"post event log",
        "data": data
    }
    return respond


@app.put("/analytic/metric")
def main_put(data: Incoming_Data):
    respond = {
        "endpoint_echo":"put metric",
        "data": data
    }
    return respond


@app.delete("/analytic/{param_a}")
def main_delete(param_a,data: Incoming_Data):
    if param_a == 'event-log':
        respond = {
            "endpoint_echo":"delete event log",
            "data": data
        }
        return respond

    if param_a == 'metric':
        respond = {
            "endpoint_echo":"delete metric",
            "data": data
        }
        return respond





