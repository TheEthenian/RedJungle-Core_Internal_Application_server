from sqlalchemy import create_engine, Integer, String, Boolean, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from functions.main_function import load_yaml_config
from typing import List


###############################################################################

config_data = load_yaml_config('../config_database.yaml')

db_username = config_data['orchestration_microservice']['database']['db_username']
db_passcode = config_data['orchestration_microservice']['database']['db_passcode']
db_url = config_data['orchestration_microservice']['database']['db_url']
db_port = config_data['orchestration_microservice']['database']['db_port']
db_name = config_data['orchestration_microservice']['database']['db_name']


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


Workflow_Step_Association = Table (
    "workflow_step_association",
    Base.metadata,
    Column('workflow_id', ForeignKey('workflow_object.workflow_id'), primary_key=True),
    Column('step_id', ForeignKey('step_object.step_id'), primary_key=True)
)

Service_Step_Association = Table (
    "service_step_association",
    Base.metadata,
    Column('service_id', ForeignKey('service_object.service_id'), primary_key=True),
    Column('step_id', ForeignKey('step_object.step_id'), primary_key=True)
)

Sub_Workflow_Workflow_Association = Table (
    "sub_workflow_workflow_association",
    Base.metadata,
    Column('sub_workflow_id', ForeignKey('sub_workflow_object.sub_workflow_id'), primary_key=True),
    Column('workflow_id', ForeignKey('workflow_object.workflow_id'), primary_key=True)
)


###############################################################################

########################## TABLE INITIALIZATION ###########################

class Workflow_Object(Base):
    __tablename__ = 'workflow_object'

    workflow_id: Mapped[str] = mapped_column(String, primary_key=True)
    workflow_name: Mapped[str] = mapped_column(String)

    workflow_progress_wormhole: Mapped['Progress_Object'] = relationship(back_populates='progress_workflow_wormhole')
    workflow_step_wormhole: Mapped['Step_Object'] = relationship(back_populates='step_workflow_wormhole')
    workflow_sub_workflow_wormhole: Mapped['Sub_Workflow_Object'] = relationship(back_populates='sub_workflow_workflow_wormhole')

    steps: Mapped[List['Step_Object']] = relationship(
        secondary=Workflow_Step_Association,
        back_populates='workflows'
        )

    sub_workflows: Mapped[List['Sub_Workflow_Object']] = relationship(
        secondary=Sub_Workflow_Workflow_Association,
        back_populates='workflows'
        )



class Step_Object(Base):
    __tablename__ = 'step_object'

    step_id: Mapped[str] = mapped_column(String, primary_key=True)
    relative_url: Mapped[str] = mapped_column(String)
    execution_order: Mapped[int] = mapped_column(Integer)

    service_id: Mapped[str] = mapped_column(ForeignKey('service_object.service_id'))
    workflow_id: Mapped[str] = mapped_column(ForeignKey('workflow_object.workflow_id'))
    step_workflow_wormhole: Mapped['Workflow_Object'] = relationship(back_populates='workflow_step_wormhole')

    workflows: Mapped[List['Workflow_Object']] = relationship(
        secondary=Workflow_Step_Association,
        back_populates='steps'
        )

    services: Mapped[List['Service_Object']] = relationship(
        secondary=Service_Step_Association,
        back_populates='steps'
        )



class Service_Object(Base):
    __tablename__ = 'service_object'

    service_id: Mapped[str] = mapped_column(String, primary_key=True)
    service_name: Mapped[str] = mapped_column(String)
    endpoint: Mapped[str] = mapped_column(String)

    steps: Mapped[List['Step_Object']] = relationship(
        secondary=Service_Step_Association,
        back_populates='services'
        )



class Sub_Workflow_Object(Base):
    __tablename__ = 'sub_workflow_object'

    sub_workflow_id: Mapped[str] = mapped_column(String, primary_key=True)
    execution_order: Mapped[int] = mapped_column(Integer)
    
    assistance_workflow_id: Mapped[str] = mapped_column(ForeignKey('workflow_object.workflow_id'))

    sub_workflow_workflow_wormhole: Mapped['Workflow_Object'] = relationship(back_populates='workflow_sub_workflow_wormhole')

    workflows: Mapped[List['Workflow_Object']] = relationship(
        secondary= Sub_Workflow_Workflow_Association,
        back_populates='sub_workflows'
        )



class Progress_Object(Base):
    __tablename__ = 'progress_object'

    progress_id: Mapped[str] = mapped_column(String, primary_key=True)
    workflow_id: Mapped[str] = mapped_column(ForeignKey('workflow_object.workflow_id'))
    current_service_id: Mapped[str] = mapped_column(String)
    progress_status: Mapped[str] = mapped_column(String)
    complete_status: Mapped[str] = mapped_column(String)

    progress_workflow_wormhole: Mapped['Workflow_Object'] = relationship(back_populates='workflow_progress_wormhole')



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


workflow_one = Workflow_Object(
    workflow_id= 'w1',
    workflow_name= 'w_name1'
)
workflow_three = Workflow_Object(
    workflow_id= 'w2',
    workflow_name= 'w_name2'
)
workflow_two = Workflow_Object(
    workflow_id= 'w3',
    workflow_name= 'w_name3'
)

#############################################################################

service_three = Service_Object(
    service_id= 's1',
    service_name= 's_name3',
    endpoint= '/s'
)
service_two = Service_Object(
    service_id= 's2',
    service_name= 's_name2',
    endpoint= '/r'
)
service_one = Service_Object(
    service_id= 's3',
    service_name= 's_name1',
    endpoint= '/v'
)

#############################################################################

step_two = Step_Object(
    step_id= 'st_1',
    workflow_id= workflow_two.workflow_id,
    service_id= service_one.service_id,
    relative_url= '/mrkrabs',
    execution_order= 4
)
step_one = Step_Object(
    step_id= 'st_2',
    workflow_id= workflow_one.workflow_id,
    service_id= service_three.service_id,
    relative_url= '/joker',
    execution_order= 7
)
step_four = Step_Object(
    step_id= 'st_4',
    workflow_id= workflow_two.workflow_id,
    service_id= service_one.service_id,
    relative_url= '/spongebob',
    execution_order= 9
)
step_three = Step_Object(
    step_id= 'st_3',
    workflow_id= workflow_one.workflow_id,
    service_id= service_two.service_id,
    relative_url= '/squidward',
    execution_order= 2
)
step_five = Step_Object(
    step_id= 'st_5',
    workflow_id= workflow_three.workflow_id,
    service_id= service_three.service_id,
    relative_url= '/lobster',
    execution_order= 1
)

#############################################################################

sub_workflow_one = Sub_Workflow_Object(
    sub_workflow_id= 'bigle',
    assistance_workflow_id= workflow_two.workflow_id,
    execution_order= 4
)
sub_workflow_two = Sub_Workflow_Object(
    sub_workflow_id= 'dart',
    assistance_workflow_id= workflow_three.workflow_id,
    execution_order= 4
)

#############################################################################

progress_one = Progress_Object(
    progress_id= '#452',
    workflow_id= workflow_one.workflow_id,
    current_service_id= 'something_pasted',
    progress_status= 'done',
    complete_status= 'inprogress'
)

#############################################################################

workflow_one.steps.append(step_one)
workflow_one.steps.append(step_three)
workflow_two.steps.append(step_two)
workflow_two.steps.append(step_four)
workflow_three.steps.append(step_five)

step_one.services.append(service_one)
step_one.services.append(service_three)
step_two.services.append(service_two)
step_three.services.append(service_one)
step_three.services.append(service_two)
step_four.services.append(service_one)
step_four.services.append(service_three)
step_four.services.append(service_two)
step_five.services.append(service_two)

workflow_one.sub_workflows.append(sub_workflow_one)
workflow_three.sub_workflows.append(sub_workflow_two)

#############################################################################

############################ TESTING FUNCTIONS ##############################


#create_rows(session, [
#    workflow_one,workflow_two,workflow_three,service_one,
#    service_two,service_three,step_one,step_two,step_three,
#    step_four,step_five,sub_workflow_one,sub_workflow_two,
#    progress_one
#    ])


#read_row(session, 12 , "policy_object", "policy_id")


#contents = session.query(Workflow_Object).all()
##
#for workflow_item in contents:
#    print('root workflow name: ', workflow_item.workflow_name)
#    print('root workflow id: ', workflow_item.workflow_id)
#    for sub_workflow_item in workflow_item.sub_workflows:
#        print('sub_workflow_id: ', sub_workflow_item.sub_workflow_id)
#        print('sub_workflow_execution_order: ', sub_workflow_item.execution_order)
#        print('assistance_workflow_id: ', sub_workflow_item.assistance_workflow_id)
#        for workflow_instance in contents:
#            if workflow_instance.workflow_id == sub_workflow_item.assistance_workflow_id:
#                print('This is the assistance workflow info')
#                print('workflow name: ', workflow_instance.workflow_name)
#                print('workflow id: ', workflow_instance.workflow_id)
                













