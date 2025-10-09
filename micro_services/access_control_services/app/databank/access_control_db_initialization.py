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


def get_session():
    session = Session()
    return session

###############################################################################
class Base(DeclarativeBase):
    pass

########################  INTERMEDIATE TABLES  #################################


Role_Policy_Association = Table(
    "role_policy_association",
    Base.metadata,
    Column("role_id", ForeignKey("role_object.role_id"), primary_key=True),
    Column("policy_id", ForeignKey("policy_object.policy_id"), primary_key=True)
)


########################## TABLE INITIALIZATION ###########################


class Policy_Object(Base):
    __tablename__ = 'policy_object'

    policy_id: Mapped[str] = mapped_column(String, primary_key=True)
    service_id: Mapped[str] = mapped_column(String)
    uri: Mapped[str] = mapped_column(String, unique=True)
    action: Mapped[str] = mapped_column(String)

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

#########################################################
