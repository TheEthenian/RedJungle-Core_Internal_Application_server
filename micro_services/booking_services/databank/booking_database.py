from sqlalchemy import create_engine, Integer, String, Float, Boolean, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from functions.main_function import load_yaml_config
from typing import List


###############################################################################

config_data = load_yaml_config('../config_database.yaml')

db_username = config_data['booking_microservice']['database']['db_username']
db_passcode = config_data['booking_microservice']['database']['db_passcode']
db_url = config_data['booking_microservice']['database']['db_url']
db_port = config_data['booking_microservice']['database']['db_port']
db_name = config_data['booking_microservice']['database']['db_name']


###############################################################################

DATABASE_URL = f"postgresql+psycopg2://{db_username}:{db_passcode}@{db_url}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


###############################################################################


class Base(DeclarativeBase):
    pass


###############################################################################

########################  INTERMEDIATE TABLES  #################################

Guest_Booking_Association = Table (
    'guest_booking_association',
    Base.metadata,
    Column('guest_id', ForeignKey('guest_object.guest_id'), primary_key=True),
    Column('booking_id', ForeignKey('booking_object.booking_id'), primary_key=True)
)

###############################################################################

########################## TABLE INITIALIZATION ###########################

class Booking_Object(Base):
    __tablename__ = 'booking_object'

    booking_id: Mapped[str] = mapped_column(String, primary_key=True)
    tenant_id: Mapped[str] = mapped_column(String)
    hotel_id: Mapped[str] = mapped_column(String)
    room_id: Mapped[str] = mapped_column(String)
    check_in_date: Mapped[str] = mapped_column(String)
    check_out_date: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    total_price: Mapped[float] = mapped_column(Float)
    payment_transaction_id: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)

    guest_id: Mapped[str] = mapped_column(ForeignKey('guest_object.guest_id'))

    booking_invoice_wormhole: Mapped['Invoice_Object'] = relationship(back_populates='invoice_booking_wormhole')
    booking_guest_wormhole: Mapped['Guest_Object'] = relationship(back_populates='guest_booking_wormhole')

    guests: Mapped[List['Guest_Object']] = relationship(
        secondary= Guest_Booking_Association,
        back_populates='bookings'
    )


class Guest_Object(Base):
    __tablename__ = 'guest_object'

    guest_id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(String, default='')
    first_name: Mapped[str] = mapped_column(String, default='')
    last_name: Mapped[str] = mapped_column(String, default='')
    email: Mapped[str] = mapped_column(String, default='')
    phone_number: Mapped[int] = mapped_column(Integer, default='')
    created_at: Mapped[str] = mapped_column(String)

    guest_booking_wormhole: Mapped['Booking_Object'] = relationship(back_populates='booking_guest_wormhole')

    bookings: Mapped[List['Booking_Object']] = relationship(
        secondary= Guest_Booking_Association,
        back_populates='guests'
    )


class Invoice_Object(Base):
    __tablename__ = 'invoice_object'

    invoice_id: Mapped[str] = mapped_column(String, primary_key=True)
    invoice_number: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)

    booking_id: Mapped[str] = mapped_column(String, ForeignKey('booking_object.booking_id'))

    invoice_booking_wormhole: Mapped['Booking_Object'] = relationship(back_populates='booking_invoice_wormhole')


Base.metadata.create_all(engine)

#############################################################################

###############################  FUNCTIONS  #################################

def create_rows(db_session, list_rows):
    db_session.add_all(list_rows)
    db_session.commit()
    db_session.close()


def read_row(db_session, item_content, target_table, target_attribute):
    entity = db_session.query(target_table).filter(target_attribute == item_content).first()
    print(entity)


def update_row(db_session, item_id, target_view):
    pass 


def delete_row(db_session, list_rows):
    pass 



#############################################################################

########################## OBJECT INITIALIZATION ###########################

guest_one = Guest_Object(
    guest_id= 'thethethe', 
    user_id= 'rtrtrt', 
    first_name= 'someone', 
    last_name= 'lastone', 
    email= 'person@email.org', 
    phone_number= 548689,
    created_at= '4thTemberYear'
)

booking_one = Booking_Object(
    booking_id= 'tttttt',
    guest_id= guest_one.guest_id,
    tenant_id= 'rrrrrr',
    hotel_id= 'ssssss',
    room_id= 'vvvvvvvvv',
    check_in_date= '1stMonth',
    check_out_date= '5stMonth',
    status= 'ready for occupation',
    total_price= 2548.05,
    payment_transaction_id= 'cwcwcw',
    created_at= '24thDay'
)

invoice_one = Invoice_Object(
    invoice_id= 'hjkhjk',
    invoice_number= 8759426,
    booking_id= booking_one.booking_id,
    status= 'pending',
    created_at= '7thHourMInute'
)

guest_one.bookings.append(booking_one)



#############################################################################

############################ TESTING FUNCTIONS ##############################


#create_rows(session, [guest_one, booking_one,invoice_one])
#read_row(session, 12 , "policy_object", "policy_id")


contents = session.query(Guest_Object).all()
#
for item in contents:
    print(item.email)
    print(item.phone_number)
    for entity in item.bookings:
        print(entity.booking_id, entity.room_id, entity.status , entity.total_price)




