from functions.db_operations import create_transaction
from functions.db_operations import create_bank
from functions.db_operations import create_bank_customer
from functions.db_operations import create_link_btwn_customer_bank

from functions.db_operations import read_data
from functions.db_operations import read_all_data
from functions.db_operations import update_data
from functions.db_operations import delete_data
from functions.db_operations import delete_all_data
from databank.payment_gateway_db_initialization import get_session

import httpx
import json
from datetime import datetime

################## GLOBAL VARIABLES ##################################

session = get_session()

base_url = "http://redjungle-00.lab:7060"

bank_url = f"{base_url}/bank"
transaction_url = f"{base_url}/transaction"
bank_customer_url = f"{base_url}/bank-customer"

def get_current_year():
    current_date = datetime.now()
    year = current_date.year
    return year

##########################################################################3

def transaction_function(payload):

    if  payload.payload['action'] == 'create':
        pass

    if  payload.payload['action'] == 'get':
        pass

    if  payload.payload['action'] == 'delete':
        pass


def bank_function(payload):

    bank_name = payload.payload['details']['bank_name']

    if  payload.payload['action'] == 'create':
        check_bank_existance_payload = input_data_structure_conversion(action='get',parameter_nested_list=[['description','existance']['bank_name',bank_name]])
        check_bank_existance = httpx.post(bank_url,json=check_bank_existance_payload)

        if check_bank_existance.json() == 'found':
            new_bank = create_bank(bank_name_input=bank_name)
            return f'new bank has been made and has id = {new_bank['bank_id']}'

        if check_bank_existance.json() == 'not_found':
            return f'bank of name = {bank_name} already exists'

    if  payload.payload['action'] == 'get':
        if payload.payload['payload']['details']['description'] == 'existance':
            pass


    if  payload.payload['action'] == 'update':
        pass

    if  payload.payload['action'] == 'delete':
        pass


def bank_customer_function(payload):

    if  payload.payload['action'] == 'create':
        pass

    if  payload.payload['action'] == 'get':
        pass
    
    if  payload.payload['action'] == 'update':
        pass

    if  payload.payload['action'] == 'delete':
        pass



########################## MODULAR FUNCTIONS ##################################

def input_data_structure_conversion(action,parameter_nested_list):
    actual_dynamic_data = {}

    for item in parameter_nested_list:
        actual_dynamic_data[item[0]] = item[1]

    canonical_structure = {
        "server_authorization_token":"adasdfsd",
        "payload":{
            "action":action,
            "details":actual_dynamic_data
        }
    }
    return canonical_structure


def transform_list_string_bidirectional(change_direction,input_data_list,mediator_char):
    
    if change_direction == 'turn_to_list':
        list_converted = input_data_list[0].split(mediator_char)
        return list_converted

    if change_direction == 'turn_to_string':
        list_converted = mediator_char.join(input_data_list)
        return list_converted

    else:
        return 'change direction is invalid'




