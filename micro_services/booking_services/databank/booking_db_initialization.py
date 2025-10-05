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

def get_session():
    session = Session()
    return session
    

###############################################################################
class Base(DeclarativeBase):
    pass

########################  INTERMEDIATE TABLES  #################################

Guest_Booking_Association = Table (
    'guest_booking_association',
    Base.metadata,
    Column('guest_id', ForeignKey('guest_object.guest_id'), primary_key=True),
    Column('booking_id', ForeignKey('booking_object.booking_id'), primary_key=True)
)

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

    booking_invoice_wormhole: Mapped['Invoice_Object'] = relationship(back_populates='invoice_booking_wormhole')

    guests: Mapped[List['Guest_Object']] = relationship(
        secondary= Guest_Booking_Association,
        back_populates='bookings'
    )


class Guest_Object(Base):
    __tablename__ = 'guest_object'

    guest_id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)

    bookings: Mapped[List['Booking_Object']] = relationship(
        secondary= Guest_Booking_Association,
        back_populates='guests'
    )


class Invoice_Object(Base):
    __tablename__ = 'invoice_object'

    invoice_id: Mapped[str] = mapped_column(String, primary_key=True)
    invoice_number: Mapped[int] = mapped_column(Integer, unique=True)
    status: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)

    booking_id: Mapped[str] = mapped_column(String, ForeignKey('booking_object.booking_id'))
    invoice_booking_wormhole: Mapped['Booking_Object'] = relationship(back_populates='booking_invoice_wormhole')


Base.metadata.create_all(engine)

#############################################################################








