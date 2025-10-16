from sqlalchemy import update, delete
import uuid
import datetime

from databank.booking_db_initialization import get_session
from databank.booking_db_initialization import Invoice_Object
from databank.booking_db_initialization import Guest_Object
from databank.booking_db_initialization import Booking_Object


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

def create_invoice(booking_id_input,invoice_number_input,status_input):

    invoice_item = Invoice_Object(
        invoice_id= get_uuid4(), 
        booking_id=booking_id_input,
        invoice_number=invoice_number_input,
        status=status_input,
        created_at=get_timestamp()
        )
    session.add(invoice_item)
    session.commit()
    session.close()

    return invoice_item

############################################################################

def create_guest(user_id_input,email_input):

    guest_item = Guest_Object(
        guest_id= get_uuid4(),
        user_id= user_id_input,
        email= email_input,
        created_at= get_timestamp()
        )
    session.add(guest_item)
    session.commit()
    session.close()

    return guest_item

###################################################################

def create_booking(tenant_id_input,hotel_id_input,room_id_input,check_in_date_input,
    check_out_date_input,status_input,total_price_input,payment_transaction_id_input):

    booking_item = Booking_Object(
        booking_id= get_uuid4(),
        tenant_id= tenant_id_input,
        hotel_id= hotel_id_input,
        room_id= room_id_input,
        check_in_date= check_in_date_input,
        check_out_date= check_out_date_input,
        status= status_input,
        total_price= total_price_input,
        payment_transaction_id= payment_transaction_id_input,
        created_at= get_timestamp()
        )
    session.add(booking_item)
    session.commit()
    session.close()

    return booking_item

###################################################################

def create_link_btwn_booking_guest(db_session,guest_column_name,guest_row_identifier,booking_column_name,booking_row_identifier):

    target_booking = read_data(db_session,'booking',booking_column_name,booking_row_identifier)
    target_guest = read_data(db_session,'guest',guest_column_name,guest_row_identifier)

    target_booking.guests.append(target_guest)

    db_session.commit()
    db_session.close()
    return

############################################################################

def read_data(db_session,target_model_class,column_name,row_identifier):

    if target_model_class == 'invoice':
        column = getattr(Invoice_Object,column_name)
        target_item = db_session.query(Invoice_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'booking':
        column = getattr(Booking_Object,column_name)
        target_item = db_session.query(Booking_Object).filter(column == f'{row_identifier}').first()
        return target_item

    if target_model_class == 'guest':
        column = getattr(Guest_Object,column_name)
        target_item = db_session.query(Guest_Object).filter(column == f'{row_identifier}').first()
        return target_item

############################################################################

def update_data(db_session,target_model_class,identifying_column_name,identifying_row_entity,target_column_to_change,new_value_of_cell):

    if target_model_class == 'guest':

        identify_column = getattr(Guest_Object, identifying_column_name)
        update_data_column_with_value = {
            target_column_to_change : new_value_of_cell
        }

        with db_session:
            entity = (
                update(Guest_Object)
                .where(identify_column == identifying_row_entity)
                .values(**update_data_column_with_value)
            )
            result = db_session.execute(entity)
            db_session.commit()

        db_session.close()
        return 


############################################################################

def delete_data(db_session,main_id,target_model_class):

    if target_model_class == 'invoice':
        target_item = db_session.query(Invoice_Object).filter(Invoice_Object.invoice_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 


    if target_model_class == 'guest':
        target_item = db_session.query(Guest_Object).filter(Guest_Object.guest_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

    if target_model_class == 'booking':
        target_item = db_session.query(Booking_Object).filter(Booking_Object.booking_id == f'{main_id}').first()
        db_session.delete(target_item)
        db_session.commit()
        db_session.close()

        return 

############################################################################

def read_all_data(db_session,table_name):

    if table_name == 'invoice':
        res_data = db_session.query(Invoice_Object).all()
        return res_data

    if table_name == 'guest':
        res_data = db_session.query(Guest_Object).all()
        return res_data

    if table_name == 'booking':
        res_data = db_session.query(Booking_Object).all()
        return res_data


############################################################################

def delete_all_data(table_name):

    if table_name == 'invoice':
        all_rows = delete(Invoice_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'guest':
        all_rows = delete(Guest_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

    if table_name == 'booking':
        all_rows = delete(Booking_Object)
        session.execute(all_rows)

        session.commit()
        session.close()
        return 

############################################################################

#create_guest('user758','758@company.internet','Day7Month48')
#create_booking('tenant875','hotel#b23','room$ty','7thSep','21stOct','unoccupied today',8465.00,'payment#548','1stSolarMonth')
#create_invoice('&SD',25462,'fully paid','TodayMonthYear45')

#create_link_btwn_booking_guest(session,'user_id','user758','hotel_id','hotel#b23')

#data_one = read_all_data(session,'booking')
#for data in data_one:
#    for entity in data.guests:
#        print(entity.user_id,entity.email)
#
#session.close()



