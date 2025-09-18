from sqlalchemy import create_engine, Integer, String, Boolean, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from typing import List

###############################################################################

DATABASE_URL = "postgresql+psycopg2://invinsible:$omniman#@localhost:9001/orchestration_bank"
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



###############################################################################

########################## TABLE INITIALIZATION ###########################

class Workflow_Object(Base):
    __tablename__ = 'workflow_object'

    workflow_id: Mapped[str] = mapped_column(String, primary_key=True)
    workflow_name: Mapped[str] = mapped_column(String)

    workflow_progress_wormhole: Mapped['Progress_Object'] = relationship(back_populates='progress_workflow_wormhole')
    workflow_step_wormhole: Mapped['Step_Object'] = relationship(back_populates='step_workflow_wormhole')

    steps: Mapped[List['Step_Object']] = relationship(
        secondary=Workflow_Step_Association,
        back_populates='workflows'
        )


class Step_Object(Base):
    __tablename__ = 'step_object'

    step_id: Mapped[str] = mapped_column(String, primary_key=True)
    service_id: Mapped[str] = mapped_column(ForeignKey('service_object.service_id'))
    workflow_id: Mapped[str] = mapped_column(ForeignKey('workflow_object.workflow_id'))
    step_execution_order: Mapped[int] = mapped_column(Integer)

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
    workflow_id= 'eeer',
    workflow_name= 'tututu'
)

service_one = Service_Object(
    service_id= 'cvcvcv',
    service_name= 'mkmkmkmk',
    endpoint= '/v3/something/here'
)

step_one = Step_Object(
    step_id= 'bnbnbn',
    workflow_id= workflow_one.workflow_id,
    service_id= service_one.service_id,
    step_execution_order= 4
)

progress_one = Progress_Object(
    progress_id= '#452',
    workflow_id= workflow_one.workflow_id,
    current_service_id= 'something_pasted',
    progress_status= 'done',
    complete_status= 'inprogress'
)

workflow_one.steps.append(step_one)
step_one.services.append(service_one)

#############################################################################

############################ TESTING FUNCTIONS ##############################


#create_rows(session, [workflow_one,service_one,step_one,progress_one])
#read_row(session, 12 , "policy_object", "policy_id")


#contents = session.query(Workflow_Object).all()
##
#for item in contents:
#    print(item.workflow_name)
#    for some in item.steps:
#        print(some.step_execution_order)
#        for serve in some.services:
#            print(serve.endpoint)




