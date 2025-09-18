from sqlalchemy import create_engine, Integer, String, Float, Boolean, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from typing import List

###############################################################################

DATABASE_URL = "postgresql+psycopg2://invinsible:$omniman#@localhost:9060/payment_gateway_bank"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

###############################################################################

class Base(DeclarativeBase):
    pass

###############################################################################

########################  INTERMEDIATE TABLES  #################################



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

    payment_method_id: Mapped[str]= mapped_column(ForeignKey('payment_method_object.payment_method_id'))


class Paymenet_Method_Object(Base):
    __tablename__ = 'payment_method_object'

    payment_method_id: Mapped[str] = mapped_column(String, primary_key=True)
    gateway_token: Mapped[str] = mapped_column(String)
    card_brand: Mapped[str] = mapped_column(String)
    last_four_digits: Mapped[int] = mapped_column(Integer)
    card_expiration_date: Mapped[str] = mapped_column(String)
    is_default: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)



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


payment_one = Paymenet_Method_Object(
    payment_method_id= 'hghghghg',
    gateway_token= 'nmnmnm',
    card_brand= 'visa',
    last_four_digits= 4526,
    card_expiration_date= '8/33',
    is_default= 'cash',
    created_at= '7thMonthYear'
)

transaction_one = Transaction_Object (
    transaction_id = 'qwqwqqww',
    user_id= 'tytytytyty',
    tenant_id = 'bnbnbnbn',
    amount = 758.35,
    status = 'onway',
    payment_method_id = payment_one.payment_method_id,
    created_at = '45thMonth'
)


#############################################################################

############################ TESTING FUNCTIONS ##############################


#create_rows(session, [payment_one,transaction_one])
#read_row(session, 12 , "policy_object", "policy_id")


#contents = session.query(Policy_Object).all()
#
#for item in contents:
#    print(item.policy_id)
#    print(item.policy_name)
#    for entity in item.roles:
#        print(entity.role_id, entity.role_name)




