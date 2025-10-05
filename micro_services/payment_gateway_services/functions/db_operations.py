from sqlalchemy import update, delete
from databank.payment_gateway_db_initialization import get_session

from databank.payment_gateway_db_initialization import Transaction_Object
from databank.payment_gateway_db_initialization import Bank_Object


###################################################################
session = get_session()

###################################################################

def create_transaction(user_id_input,tenant_id_input,amount_input,status_input,bank_id_input,card_brand_input,card_last_four_digits_input,created_at_input):
    generated_transaction_id = '#67'

    transaction_item = Transaction_Object(
        transaction_id= generated_transaction_id,
        user_id= user_id_input,
        tenant_id= tenant_id_input,
        amount= amount_input,
        status= status_input,
        bank_id= bank_id_input,
        card_brand= card_brand_input,
        card_last_four_digits= card_last_four_digits_input,
        created_at= created_at_input
        )
    session.add(transaction_item)
    session.commit()
    session.close()

    return transaction_item

############################################################################

def create_bank(user_id_input,card_brand_input,card_number_input,card_expiration_date_input,account_balance_input,updated_at_input):
    generated_bank_id = 'bank#5'

    bank_item = Bank_Object(
        bank_id= generated_bank_id,
        user_id= user_id_input,
        card_brand= card_brand_input,
        card_number= card_number_input,
        card_expiration_date= card_expiration_date_input,
        account_balance= account_balance_input,
        updated_at= updated_at_input
        )
    session.add(bank_item)
    session.commit()
    session.close()

    return bank_item

############################################################################

def read_data(db_session,target_model_class,column_name,row_identifier):

    if target_model_class == 'transaction':
        column = getattr(Transaction_Object,column_name)
        target_item = db_session.query(Transaction_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'bank':
        column = getattr(Bank_Object,column_name)
        target_item = db_session.query(Bank_Object).filter(column == f'{row_identifier}').first()
        return target_item

############################################################################

def update_data(db_session,target_model_class,identifying_column_name,identifying_row_entity,target_column_to_change,new_value_of_cell):

    if target_model_class == 'transaction':

        identify_column = getattr(Transaction_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Transaction_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


    if target_model_class == 'bank':

        identify_column = getattr(Bank_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Bank_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


############################################################################

def delete_data(db_session,main_id,target_model_class):

    if target_model_class == 'transaction':
        target_item = db_session.query(Transaction_Object).filter(Transaction_Object.transaction_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

    if target_model_class == 'bank':
        target_item = db_session.query(Bank_Object).filter(Bank_Object.bank_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

############################################################################

def read_all_data(db_session,table_name):

    if table_name == 'transaction':
        res_data = db_session.query(Transaction_Object).all()
        return res_data

    if table_name == 'bank':
        res_data = db_session.query(Bank_Object).all()
        return res_data

############################################################################

def delete_all_data(table_name):

    if table_name == 'transaction':
        all_rows = delete(Transaction_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'bank':
        all_rows = delete(Bank_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

############################################################################


#create_bank('user2','mastercard',451745174517,'Tuesday5thNever',58500.25,'4THnow')
#create_transaction('user45','tenanat001',457.05,'successful','bank#5','visa',5782,'2ndYear')






