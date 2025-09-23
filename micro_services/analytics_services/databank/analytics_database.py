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
session = Session()


###############################################################################


class Base(DeclarativeBase):
    pass


###############################################################################

########################  INTERMEDIATE TABLES  #################################



###############################################################################

########################## TABLE INITIALIZATION ###########################




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




#############################################################################

############################ TESTING FUNCTIONS ##############################


#create_rows(session, [policy_one, policy_two,role_item,decision_log_item])
#read_row(session, 12 , "policy_object", "policy_id")


#contents = session.query(Policy_Object).all()
#
#for item in contents:
#    print(item.policy_id)
#    print(item.policy_name)
#    for entity in item.roles:
#        print(entity.role_id, entity.role_name)




