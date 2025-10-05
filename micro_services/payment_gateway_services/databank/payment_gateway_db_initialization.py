from sqlalchemy import create_engine, Integer,BigInteger, String, Float, Boolean, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from functions.main_function import load_yaml_config
from typing import List


###############################################################################

config_data = load_yaml_config('../config_database.yaml')

db_username = config_data['payment_gateway_microservice']['database']['db_username']
db_passcode = config_data['payment_gateway_microservice']['database']['db_passcode']
db_url = config_data['payment_gateway_microservice']['database']['db_url']
db_port = config_data['payment_gateway_microservice']['database']['db_port']
db_name = config_data['payment_gateway_microservice']['database']['db_name']

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

########################## TABLE INITIALIZATION ###########################

class Transaction_Object(Base):
    __tablename__ = 'transaction_object'

    transaction_id: Mapped[str]= mapped_column(String, primary_key=True)
    user_id: Mapped[str]= mapped_column(String)
    tenant_id: Mapped[str]= mapped_column(String)
    amount: Mapped[float]= mapped_column(Float)
    status: Mapped[str]= mapped_column(String)
    bank_id: Mapped[str]= mapped_column(ForeignKey('bank_object.bank_id'))
    card_brand: Mapped[str]= mapped_column(String)
    card_last_four_digits: Mapped[str]= mapped_column(Integer)
    created_at: Mapped[str]= mapped_column(String)

    transaction_bank_wormhole: Mapped['Bank_Object'] = relationship(back_populates='bank_transaction_wormhole')


class Bank_Object(Base):
    __tablename__ = 'bank_object'

    bank_id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(String)
    card_brand: Mapped[str] = mapped_column(String)
    card_number: Mapped[str] = mapped_column(BigInteger)
    card_expiration_date: Mapped[str] = mapped_column(String)
    account_balance: Mapped[str] = mapped_column(Float)
    updated_at: Mapped[str] = mapped_column(String)

    bank_transaction_wormhole: Mapped['Transaction_Object'] = relationship(back_populates='transaction_bank_wormhole')


Base.metadata.create_all(engine)

#############################################################################








