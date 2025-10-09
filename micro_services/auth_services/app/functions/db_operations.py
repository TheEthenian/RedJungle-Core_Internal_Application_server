from sqlalchemy import update, delete
from databank.auth_db_initialization import get_session

from databank.auth_db_initialization import Password_Reset_Token_Object
from databank.auth_db_initialization import Session_Object
from databank.auth_db_initialization import Credential_Object


###################################################################
session = get_session()

###################################################################

def create_password_reset_token(token_input,expires_at_input,is_used_input):
    generated_token_id = '#67'

    password_reset_token_item = Password_Reset_Token_Object(
        token_id= generated_token_id,
        token= token_input,
        expires_at= expires_at_input,
        is_used= is_used_input,
        )
    session.add(password_reset_token_item)
    session.commit()
    session.close()

    return password_reset_token_item

############################################################################

def create_session(credential_id_input,token_hash_input,expires_at_input,ip_address_input):
    generated_session_id = '$F45'

    session_item = Session_Object(
        session_id= generated_session_id,
        credential_id= credential_id_input,
        token_hash= token_hash_input,
        expires_at= expires_at_input,
        ip_address= ip_address_input
        )
    session.add(session_item)
    session.commit()
    session.close()

    return session_item

###################################################################

def create_credential(user_id_input,email_input,hashed_password_input,salt_input,mfa_secret_input,last_login_at_input,failed_login_attempts_input):
    generated_credential_id = '4&5'

    credential_item = Credential_Object(
        credential_id= generated_credential_id,
        user_id= user_id_input,
        email= email_input,
        hashed_password= hashed_password_input,
        salt= salt_input,
        mfa_secret= mfa_secret_input,
        last_login_at= last_login_at_input,
        failed_login_attempts= failed_login_attempts_input
        )
    session.add(credential_item)
    session.commit()
    session.close()

    return credential_item

###################################################################

def create_link_btwn_credential_reset_token(db_session,credential_column_name,credential_row_identifier,reset_token_column_name,reset_token_row_identifier):

    target_credential = read_data(db_session,'credential',credential_column_name,credential_row_identifier)
    target_reset_token = read_data(db_session,'reset_token',reset_token_column_name,reset_token_row_identifier)

    target_credential.reset_tokens.append(target_reset_token)

    db_session.commit()
    db_session.close()
    return


############################################################################

def read_data(db_session,target_model_class,column_name,row_identifier):

    if target_model_class == 'reset_token':
        column = getattr(Password_Reset_Token_Object,column_name)
        target_item = db_session.query(Password_Reset_Token_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'credential':
        column = getattr(Credential_Object,column_name)
        target_item = db_session.query(Credential_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'session':
        column = getattr(Session_Object,column_name)
        target_item = db_session.query(Session_Object).filter(column == f'{row_identifier}').first()
        return target_item

############################################################################

def update_data(db_session,target_model_class,identifying_column_name,identifying_row_entity,target_column_to_change,new_value_of_cell):

    if target_model_class == 'credential':

        identify_column = getattr(Credential_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Credential_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


############################################################################

def delete_data(main_id,target_model_class):

    if target_model_class == 'reset_token':
        target_item = session.query(Password_Reset_Token_Object).filter(Password_Reset_Token_Object.token_id == f'{main_id}').first()
        session.delete(target_item)
        session.commit()
        session.close()

        return 


    if target_model_class == 'session':
        target_item = session.query(Session_Object).filter(Session_Object.session_id == f'{main_id}').first()
        session.delete(target_item)
        session.commit()
        session.close()

        return 

    if target_model_class == 'credential':
        target_item = session.query(Credential_Object).filter(Credential_Object.credential_id == f'{main_id}').first()
        session.delete(target_item)
        session.commit()
        session.close()

        return 

############################################################################

def read_all_data(db_session,table_name):

    if table_name == 'reset_token':
        res_data = session.query(Password_Reset_Token_Object).all()
        return res_data

    if table_name == 'session':
        res_data = session.query(Session_Object).all()
        return res_data

    if table_name == 'credential':
        res_data = session.query(Credential_Object).all()
        return res_data


############################################################################

def delete_all_data(table_name):

    if table_name == 'reset_token':
        all_rows = delete(Password_Reset_Token_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'session':
        all_rows = delete(Session_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'credential':
        all_rows = delete(Credential_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

############################################################################


#create_credential('th445','email@company.com','Thk4532l','im batman','batcave','75thDay',8)
#create_password_reset_token('DHALDADSFH','12October',False)
#create_session('4&5','AHD87DADF','1985','182.148.124.781')


#create_link_btwn_credential_reset_token(session,'user_id','th445','expires_at','12October')

#delete_all_data('session')
#delete_all_data('credential')
#delete_all_data('reset_token')

data_one = read_all_data(session,'credential')


for data in data_one:
    for entity in data.reset_tokens:
        print(entity.token, entity.is_used)
session.close()









