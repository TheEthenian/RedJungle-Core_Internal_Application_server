from sqlalchemy import create_engine, Integer, String, Boolean, ForeignKey, Table, Column, Float
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from functions.main_function import load_yaml_config
from typing import List


###############################################################################

config_data = load_yaml_config('../config_database.yaml')

db_username = config_data['admin_microservice']['database']['db_username']
db_passcode = config_data['admin_microservice']['database']['db_passcode']
db_url = config_data['admin_microservice']['database']['db_url']
db_port = config_data['admin_microservice']['database']['db_port']
db_name = config_data['admin_microservice']['database']['db_name']

print(db_name)

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

Hotel_Config_Association = Table (
    "hotel_config_association",
    Base.metadata,
    Column('hotel_id', ForeignKey('hotel_object.hotel_id'), primary_key=True),
    Column('config_id', ForeignKey('hotel_configuration_object.config_id'), primary_key=True)
)


Hotel_Service_Association = Table (
    'hotel_service_association',
    Base.metadata,
    Column('hotel_id', ForeignKey('hotel_object.hotel_id'), primary_key=True),
    Column('service_id', ForeignKey('hotel_service_object.service_id'), primary_key=True),
)


Hotel_Staff_Association = Table (
    'hotel_staff_association',
    Base.metadata,
    Column('hotel_id', ForeignKey('hotel_object.hotel_id'), primary_key=True),
    Column('staff_id', ForeignKey('staff_user_object.staff_id'), primary_key=True),
)


###########################################################################

################################ TABLES INITIALIZATION ###################################


class Hotel_Object(Base):
    __tablename__ = 'hotel_object'

    hotel_id: Mapped[str] = mapped_column(String, primary_key=True)
    hotel_name: Mapped[str] = mapped_column(String)
    tenant_id: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    contact_number: Mapped[int] = mapped_column(Integer)

    hotel_admin_wormhole: Mapped['Admin_User_Object'] = relationship(back_populates='admin_hotel_wormhole')
    hotel_config_wormhole: Mapped['Hotel_Configuration_Object'] = relationship(back_populates='config_hotel_wormhole')
    hotel_service_wormhole: Mapped['Hotel_Service_Object'] = relationship(back_populates='service_hotel_wormhole')
    hotel_staff_wormhole: Mapped['Staff_User_Object'] = relationship(back_populates='staff_hotel_wormhole')

    configs: Mapped[List['Hotel_Configuration_Object']] = relationship(
        secondary=Hotel_Config_Association,
        back_populates='hotels'
        )

    services: Mapped[List['Hotel_Service_Object']] = relationship(
        secondary=Hotel_Service_Association,
        back_populates='hotels'
        )

    staff_persons: Mapped[List['Staff_User_Object']] = relationship(
        secondary=Hotel_Staff_Association,
        back_populates='hotels'
        )


class Hotel_Service_Object(Base):
    __tablename__ = 'hotel_service_object'

    service_id: Mapped[str] = mapped_column(String, primary_key=True)
    service_name: Mapped[str] = mapped_column(String)
    service_description: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    operation_schedule: Mapped[str] = mapped_column(String)

    hotel_id: Mapped[str] = mapped_column(ForeignKey('hotel_object.hotel_id'))

    service_hotel_wormhole: Mapped['Hotel_Object'] = relationship(back_populates='hotel_service_wormhole')

    hotels: Mapped[List['Hotel_Object']] = relationship(
        secondary=Hotel_Service_Association,
        back_populates='services'
        )


class Admin_User_Object(Base):
    __tablename__ = 'admin_user_object'

    admin_user_id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(String)
    tenant_id: Mapped[str] = mapped_column(String)
    role_id: Mapped[str] = mapped_column(String)

    hotel_id: Mapped[str] = mapped_column(ForeignKey('hotel_object.hotel_id'))

    admin_hotel_wormhole: Mapped['Hotel_Object'] = relationship(back_populates='hotel_admin_wormhole')


class Staff_User_Object(Base):
    __tablename__ = 'staff_user_object'

    staff_id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(String)
    role_id: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)

    hotel_id: Mapped[str] = mapped_column(ForeignKey('hotel_object.hotel_id'))

    staff_hotel_wormhole: Mapped['Hotel_Object'] = relationship(back_populates='hotel_staff_wormhole')

    hotels: Mapped[List['Hotel_Object']] = relationship(
        secondary=Hotel_Staff_Association,
        back_populates='staff_persons'
        )

class Hotel_Configuration_Object(Base):
    __tablename__ = 'hotel_configuration_object'

    config_id: Mapped[str] = mapped_column(String, primary_key=True)
    config_name: Mapped[str] = mapped_column(String)
    config_value: Mapped[str] = mapped_column(String)
    last_updated_timestamp: Mapped[str] = mapped_column(String)

    last_updated_admin_id: Mapped[str] = mapped_column(ForeignKey('admin_user_object.admin_user_id'))
    hotel_id: Mapped[str] = mapped_column(ForeignKey('hotel_object.hotel_id'))

    config_hotel_wormhole: Mapped['Hotel_Object'] = relationship(back_populates='hotel_config_wormhole')

    hotels: Mapped[List['Hotel_Object']] = relationship(
        secondary=Hotel_Config_Association,
        back_populates='configs'
        )



Base.metadata.create_all(engine)


###########################################################################

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


hotel_one = Hotel_Object(
    hotel_id= '7d8',
    hotel_name= 'somehotel',
    tenant_id= '78522',
    location= 'Offworld',
    contact_number = 845255
)

service_one = Hotel_Service_Object(
    service_id= 'wwww',
    hotel_id = hotel_one.hotel_id,
    service_name= 'service_one',
    service_description= 'service description words',
    price= 789.27,
    operation_schedule= 'Thursday'
)

admin_one = Admin_User_Object(
    admin_user_id= 'fadfa',
    user_id= 'idhere',
    hotel_id = hotel_one.hotel_id,
    tenant_id= '#783',
    role_id= '848349jf'
)

staff_one = Staff_User_Object(
    staff_id= 'bbbbb', 
    hotel_id= hotel_one.hotel_id, 
    user_id= 'ccccc', 
    role_id= 'eeeee', 
    status= 'clocked in'
)

config_one = Hotel_Configuration_Object(
    config_id= '87dadfa7',
    config_name= 'superior chijin ping',
    hotel_id= hotel_one.hotel_id,
    config_value= 'somevalue',
    last_updated_admin_id= admin_one.admin_user_id,
    last_updated_timestamp= '12thMonth8080'
)

hotel_one.configs.append(config_one)
hotel_one.services.append(service_one)
hotel_one.staff_persons.append(staff_one)


#############################################################################

############################ TESTING FUNCTIONS ##############################


#create_rows(session, [hotel_one, service_one, staff_one, config_one, admin_one])
#read_row(session, 12 , "policy_object", "policy_id")


contents = session.query(Hotel_Object).all()
#
for item in contents:
    print(item.hotel_name)
    print(item.location)
    for entity in item.services:
        print(entity.service_name, entity.price, entity.service_description)



