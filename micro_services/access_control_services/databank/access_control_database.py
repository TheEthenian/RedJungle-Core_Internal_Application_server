from sqlalchemy import create_engine, Integer, String, Boolean, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from functions.main_function import load_yaml_config
from typing import List


###############################################################################


config_data = load_yaml_config('../config_database.yaml')

db_username = config_data['access_control_microservice']['database']['db_username']
db_passcode = config_data['access_control_microservice']['database']['db_passcode']
db_url = config_data['access_control_microservice']['database']['db_url']
db_port = config_data['access_control_microservice']['database']['db_port']
db_name = config_data['access_control_microservice']['database']['db_name']


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


Role_Policy_Association = Table(
    "role_policy_association",
    Base.metadata,
    Column("role_id", ForeignKey("role_object.role_id"), primary_key=True),
    Column("policy_id", ForeignKey("policy_object.policy_id"), primary_key=True)
)


###############################################################################

########################## TABLE INITIALIZATION ###########################


class Policy_Object(Base):
    __tablename__ = 'policy_object'

    policy_id: Mapped[str] = mapped_column(String, primary_key=True)
    policy_name: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str] = mapped_column(String, unique=True)

    roles: Mapped[List['Role_Object']] = relationship(
        secondary=Role_Policy_Association,
        back_populates='policies'
        )


class Role_Object(Base):
    __tablename__ = 'role_object'

    role_id: Mapped[str] = mapped_column(String, primary_key=True)
    role_name: Mapped[str] = mapped_column(String, unique=True)

    policies: Mapped[List['Policy_Object']] = relationship(
        secondary=Role_Policy_Association,
        back_populates='roles'
        )


class Decision_Log_Object(Base):
    __tablename__ = 'decision_log_object'

    decision_id: Mapped[str] = mapped_column(String, primary_key=True)
    service_id: Mapped[str] = mapped_column(String)
    user_id: Mapped[str] = mapped_column(String)
    tenant_id: Mapped[str] = mapped_column(String)
    resource_targeted: Mapped[str] = mapped_column(String)
    action_crud: Mapped[str] = mapped_column(String)
    allowed: Mapped[bool] = mapped_column(Boolean, default=False)
    policy_based_reason: Mapped[str] = mapped_column(String)
    timestamp: Mapped[str] = mapped_column(String)


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


policy_one = Policy_Object(
    policy_id= '12',
    policy_name= 'erase', 
    description= 'scotch earth'
)
policy_two = Policy_Object(
    policy_id= '255sssd45',
    policy_name= 'geek', 
    description= 'dont talk about fignt club'
)


role_item = Role_Object(
    role_id= '5sdfsdsd8f',
    role_name= 'Techlead'
)


decision_log_item = Decision_Log_Object(
    decision_id= '005',
    service_id= '1sfsd',
    tenant_id= '#845',
    user_id= '177',
    resource_targeted= '78',
    action_crud= 'Create',
    allowed= True,
    policy_based_reason= 'Good policy pass',
    timestamp= 'today_timed'
)

role_item.policies.append(policy_one)
role_item.policies.append(policy_two)



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








