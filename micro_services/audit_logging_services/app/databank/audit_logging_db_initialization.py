from sqlalchemy import create_engine, Integer, String, Boolean,Column, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from functions.main_function import load_yaml_config
from typing import List


###############################################################################

config_data = load_yaml_config('../config_database.yaml')

db_username = config_data['audit_logging_microservice']['database']['db_username']
db_passcode = config_data['audit_logging_microservice']['database']['db_passcode']
db_url = config_data['audit_logging_microservice']['database']['db_url']
db_port = config_data['audit_logging_microservice']['database']['db_port']
db_name = config_data['audit_logging_microservice']['database']['db_name']


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

Log_Detail_Association = Table (
    'log_detail_association',
    Base.metadata,
    Column('log_id', ForeignKey('log_object.log_id'), primary_key=True),
    Column('detail_id', ForeignKey('detail_object.detail_id'), primary_key=True)
)

########################## TABLE INITIALIZATION ###########################

class Log_Object(Base):
    __tablename__ = 'log_object'

    log_id: Mapped[str] = mapped_column(String, primary_key=True)
    source_service: Mapped[str] = mapped_column(String)
    service_uri: Mapped[str] = mapped_column(String)
    action_crud: Mapped[str]= mapped_column(String)
    user_id: Mapped[str] = mapped_column(String)
    tenant_id: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)

    details: Mapped[List['Detail_Object']] = relationship(
        secondary= Log_Detail_Association,
        back_populates= 'logs'
    )

class Detail_Object(Base):
    __tablename__ = 'detail_object'

    detail_id: Mapped[str] = mapped_column(String, primary_key=True)
    detail_name: Mapped[str] = mapped_column(String)
    detail_description: Mapped[str] = mapped_column(String)

    logs: Mapped[List['Log_Object']] = relationship(
        secondary= Log_Detail_Association,
        back_populates= 'details'
    )




Base.metadata.create_all(engine)

#############################################################################




