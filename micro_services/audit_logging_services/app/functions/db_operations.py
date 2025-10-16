from sqlalchemy import update, delete
import uuid
import datetime

from databank.audit_logging_db_initialization import get_session
from databank.audit_logging_db_initialization import Log_Object
from databank.audit_logging_db_initialization import Detail_Object


###################################################################
session = get_session()

###################################################################
def get_uuid4():
    random_uuid = uuid.uuid4()
    return random_uuid

def get_timestamp():
    unsanitized_datetime = datetime.datetime.now()
    no_microseconds_datetime = unsanitized_datetime.replace(microsecond=0)
    return no_microseconds_datetime

###################################################################

def create_log(source_service_input,service_uri_input,action_crud_input,user_id_input,tenant_id_input):

    log_item = Log_Object(
        log_id= get_uuid4(),
        source_service= source_service_input,
        service_uri= source_service_input,
        action_crud= action_crud_input,
        user_id= user_id_input,
        tenant_id= tenant_id_input,
        created_at= get_timestamp()
        )
    session.add(log_item)
    session.commit()
    session.close()

    return log_item

############################################################################

def create_detail(detail_name_input,detail_description_input):

    detail_item = Detail_Object(
        detail_id= get_uuid4(),
        detail_name= detail_name_input,
        detail_description= detail_description_input
        )
    session.add(detail_item)
    session.commit()
    session.close()

    return detail_item

###################################################################

def create_link_btwn_user_profile(db_session,detail_column_name,detail_row_identifier,log_column_name,log_row_identifier):

    target_log = read_data(db_session,'log',log_column_name,log_row_identifier)
    target_detail = read_data(db_session,'detail',detail_column_name,detail_row_identifier)

    target_log.details.append(target_detail)

    db_session.commit()
    db_session.close()
    return

############################################################################

def read_data(db_session,target_model_class,column_name,row_identifier):

    if target_model_class == 'log':
        column = getattr(Log_Object,column_name)
        target_item = db_session.query(Log_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'detail':
        column = getattr(Detail_Object,column_name)
        target_item = db_session.query(Detail_Object).filter(column == f'{row_identifier}').first()
        return target_item

############################################################################

def update_data(db_session,target_model_class,identifying_column_name,identifying_row_entity,target_column_to_change,new_value_of_cell):

    if target_model_class == 'log':

        identify_column = getattr(Log_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Log_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'detail':

        identify_column = getattr(Detail_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Detail_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


############################################################################

def delete_data(db_session,main_id,target_model_class):

    if target_model_class == 'log':
        target_item = db_session.query(Log_Object).filter(Log_Object.log_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 


    if target_model_class == 'detail':
        target_item = db_session.query(Detail_Object).filter(Detail_Object.detail_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

############################################################################

def read_all_data(db_session,table_name):

    if table_name == 'log':
        res_data = db_session.query(Log_Object).all()
        return res_data

    if table_name == 'detail':
        res_data = db_session.query(Detail_Object).all()
        return res_data


############################################################################

def delete_all_data(table_name):

    if table_name == 'log':
        all_rows = delete(Log_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'detail':
        all_rows = delete(Detail_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

############################################################################


#create_log('tenant_endpoint','/tenant','post','user75','tenant241','75thMoth')
#create_detail('create_tenant','tenant was created successfully')
#create_link_btwn_user_profile(session,'detail_name','create_tenant','source_service','tenant_endpoint')

#data_one = read_all_data(session,'log')
#
#for entry in data_one:
#    print(entry.log_id,entry.source_service,entry.service_uri,entry.action_crud)
#    for dt in entry.details:
#        print(dt.detail_name,dt.detail_description)
#
#session.close()


