from sqlalchemy import create_engine, Integer, String, Float, Boolean, ForeignKey, Table, Column
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
session = Session()

###############################################################################

class Base(DeclarativeBase):
    pass

###############################################################################

########################  INTERMEDIATE TABLES  #################################

Transaction_Payment_Object = Table (
    'transaction_payment_object',
    Base.metadata,
    Column('transaction_id', ForeignKey('transaction_object.transaction_id'), primary_key=True),
    Column('payment_method_id', ForeignKey('payment_method_object.payment_method_id'), primary_key=True)
)


###############################################################################

########################## TABLE INITIALIZATION ###########################


class Transaction_Object(Base):
    __tablename__ = 'transaction_object'

    transaction_id: Mapped[str]= mapped_column(String, primary_key=True)
    user_id: Mapped[str]= mapped_column(String)
    tenant_id: Mapped[str]= mapped_column(String)
    amount: Mapped[float]= mapped_column(Float)
    status: Mapped[str]= mapped_column(String)
    created_at: Mapped[str]= mapped_column(String)

    payment_methods: Mapped[List['Payment_Method_Object']] = relationship(
        secondary= Transaction_Payment_Object,
        back_populates= 'transactions'
    )


class Payment_Method_Object(Base):
    __tablename__ = 'payment_method_object'

    payment_method_id: Mapped[str] = mapped_column(String, primary_key=True)
    gateway_token: Mapped[str] = mapped_column(String)
    card_brand: Mapped[str] = mapped_column(String)
    last_four_digits: Mapped[int] = mapped_column(Integer)
    card_expiration_date: Mapped[str] = mapped_column(String)
    is_default: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)

    transactions: Mapped[List['Transaction_Object']] = relationship(
        secondary= Transaction_Payment_Object,
        back_populates= 'payment_methods'
    )


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


transaction_one = Transaction_Object (
    transaction_id = 'qwqwqqww',
    user_id= 'tytytytyty',
    tenant_id = 'bnbnbnbn',
    amount = 758.35,
    status = 'onway',
    created_at = '45thMonth'
)

payment_one = Payment_Method_Object(
    payment_method_id= 'hghghghg',
    gateway_token= 'nmnmnm',
    card_brand= 'visa',
    last_four_digits= 4526,
    card_expiration_date= '8/33',
    is_default= 'cash',
    created_at= '7thMonthYear'
)


payment_one.transactions.append(transaction_one)

#############################################################################

############################ TESTING FUNCTIONS ##############################


#create_rows(session, [transaction_one,payment_one])
#read_row(session, 12 , "policy_object", "policy_id")


#contents = session.query(Transaction_Object).all()
#
#for item in contents:
#    print(item.transaction_id)
#    print(item.amount)
#    for entity in item.payment_methods:
#        print(entity.card_brand, entity.last_four_digits)




