from sqlalchemy import create_engine, Integer, String, Boolean, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from functions.main_function import load_yaml_config
from typing import List


###############################################################################

config_data = load_yaml_config('../config_database.yaml')

db_username = config_data['auth_microservice']['database']['db_username']
db_passcode = config_data['auth_microservice']['database']['db_passcode']
db_url = config_data['auth_microservice']['database']['db_url']
db_port = config_data['auth_microservice']['database']['db_port']
db_name = config_data['auth_microservice']['database']['db_name']


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


Reset_Credential_Association = Table (
    'reset_credential_association',
    Base.metadata,
    Column('password_reset_token', ForeignKey('password_reset_token.token'), primary_key=True),
    Column('credential_id', ForeignKey('credential_object.credential_id'), primary_key=True)
)


###############################################################################

########################## TABLE INITIALIZATION ###########################

class Credential_Object(Base):
    __tablename__ = 'credential_object'

    credential_id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    hashed_password: Mapped[str] = mapped_column(String)
    salt: Mapped[str] = mapped_column(String)
    mfa_secret: Mapped[str] = mapped_column(String)
    last_login_at: Mapped[str] = mapped_column(String)
    failed_login_attempts: Mapped[int] = mapped_column(Integer)

    credential_session_wormhole: Mapped['Session_Object'] = relationship(back_populates='session_credential_wormhole')

    reset_tokens: Mapped[List['Password_Reset_Token']] = relationship(
        secondary= Reset_Credential_Association,
        back_populates= 'credentials'
    )


class Session_Object(Base):
    __tablename__ = 'session_objects'

    session_id: Mapped[str] = mapped_column(String, primary_key=True)
    token_hash: Mapped[str] = mapped_column(String)
    expires_at: Mapped[str] = mapped_column(String)
    ip_address: Mapped[str] = mapped_column(String)

    credential_id: Mapped[str] = mapped_column(ForeignKey('credential_object.credential_id'))

    session_credential_wormhole: Mapped['Credential_Object'] = relationship(back_populates='credential_session_wormhole')



class Password_Reset_Token(Base):
    __tablename__ = 'password_reset_token' 

    token: Mapped[str] = mapped_column(String, primary_key=True)
    expires_at: Mapped[str] = mapped_column(String)
    is_used: Mapped[bool] = mapped_column(Boolean)

    credentials: Mapped[List['Credential_Object']] = relationship(
        secondary= Reset_Credential_Association,
        back_populates= 'reset_tokens'
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


credential_one = Credential_Object(
    credential_id= 'ewewewew',
    user_id= 'yjyjyjyj',
    email= 'wewew@company.local',
    hashed_password= 'hashed stuff',
    salt= 'some barbeque salt',
    mfa_secret= 'secret club two',
    last_login_at= '18thSep',
    failed_login_attempts= 5

)

session_one = Session_Object(
    session_id= '5%5%5%43',
    credential_id= credential_one.credential_id,
    token_hash= 'shsshshshhs',
    expires_at= '#4343rfsdsd',
    ip_address= '10.17.7.57:9080'

)

reset_one = Password_Reset_Token(
    token = '@#hhhhhhhh$#',
    expires_at = '1995Jan40th',
    is_used = False

)

credential_one.reset_tokens.append(reset_one)



#############################################################################

############################ TESTING FUNCTIONS ##############################


#create_rows(session, [credential_one, session_one, reset_one])
#read_row(session, 12 , "policy_object", "policy_id")


contents = session.query(Credential_Object).all()
#
for item in contents:
    print(item.user_id)
    print(item.email)
    print(item.last_login_at)
    for entity in item.reset_tokens:
        print(entity.is_used,entity.token, entity.expires_at)




