from sqlalchemy import create_engine, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from functions.main_function import load_yaml_config
from typing import List


###############################################################################

config_data = load_yaml_config('../config_database.yaml')

db_username = config_data['analytics_microservice']['database']['db_username']
db_passcode = config_data['analytics_microservice']['database']['db_passcode']
db_url = config_data['analytics_microservice']['database']['db_url']
db_port = config_data['analytics_microservice']['database']['db_port']
db_name = config_data['analytics_microservice']['database']['db_name']


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




########################## TABLE INITIALIZATION ###########################




Base.metadata.create_all(engine)

#############################################################################





