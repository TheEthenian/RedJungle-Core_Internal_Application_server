from sqlalchemy import create_engine, Integer, Boolean, ForeignKey, Table, String, Float, Column
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from functions.main_function import load_yaml_config
from typing import List


###############################################################################

config_data = load_yaml_config('../config_database.yaml')

db_username = config_data['hotel_management_microservice']['database']['db_username']
db_passcode = config_data['hotel_management_microservice']['database']['db_passcode']
db_url = config_data['hotel_management_microservice']['database']['db_url']
db_port = config_data['hotel_management_microservice']['database']['db_port']
db_name = config_data['hotel_management_microservice']['database']['db_name']


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

Room_Amenity_Association = Table (
    'room_amenity_association',
    Base.metadata,
    Column('room_id', ForeignKey('room_object.room_id'), primary_key=True),
    Column('amenity_id', ForeignKey('room_amenity_object.amenity_id'), primary_key=True)
)

Room_Picture_Association = Table (
    'room_picture_association',
    Base.metadata,
    Column('room_id', ForeignKey('room_object.room_id'), primary_key=True),
    Column('picture_id', ForeignKey('room_picture_object.picture_id'), primary_key=True),
)


###############################################################################

########################## TABLE INITIALIZATION ###########################


class Room_Object(Base):
    __tablename__ = 'room_object'

    room_id: Mapped[str] = mapped_column(String, primary_key=True)
    room_no: Mapped[int] = mapped_column(Integer)
    hotel_id: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)


    room_maintenance_wormhole: Mapped['Maintenance_Request_Object'] = relationship(back_populates='maintenance_room_wormhole')
    room_picture_wormhole: Mapped['Room_Picture_Object'] = relationship(back_populates="picture_room_wormhole")


    amenities: Mapped[List['Room_Amenity_Object']] = relationship(
        secondary= Room_Amenity_Association,
        back_populates= 'rooms'
    )

    pictures: Mapped[List['Room_Picture_Object']] = relationship(
        secondary= Room_Picture_Association,
        back_populates= 'rooms'
    )


class Room_Amenity_Object(Base):
    __tablename__ = 'room_amenity_object'

    amenity_id: Mapped[str] = mapped_column(String, primary_key=True)
    amenity_name: Mapped[str] = mapped_column(String)
    amenity_description: Mapped[str] = mapped_column(String)
    max_occupancy: Mapped[int] = mapped_column(Integer)
    

    rooms: Mapped[List['Room_Object']] = relationship(
        secondary= Room_Amenity_Association,
        back_populates= 'amenities'
    )


class Room_Picture_Object(Base):
    __tablename__ = 'room_picture_object'

    picture_id: Mapped[str] = mapped_column(String, primary_key=True)
    picture_url: Mapped[str] = mapped_column(String)
    date_created: Mapped[str] = mapped_column(String)

    room_id: Mapped[str] = mapped_column(ForeignKey('room_object.room_id'), default='')

    picture_room_wormhole: Mapped['Room_Object'] = relationship(back_populates='room_picture_wormhole')

    rooms: Mapped[List['Room_Object']] = relationship(
        secondary= Room_Picture_Association,
        back_populates= 'pictures'
    )


class Maintenance_Request_Object(Base):
    __tablename__ = 'maintenance_request_object'
    
    request_id: Mapped[str] = mapped_column(String, primary_key=True)
    maintenance_description: Mapped[str] = mapped_column(String)
    hotel_id: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    reported_by_staff_id: Mapped[str] = mapped_column(String)

    room_id: Mapped[str] = mapped_column(ForeignKey('room_object.room_id'), default='')

    maintenance_room_wormhole: Mapped['Room_Object'] = relationship(back_populates='room_maintenance_wormhole')
    


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


amenity_one = Room_Amenity_Object(
    amenity_id= 'qqq',
    amenity_name= 'amenity1',
    amenity_description= 'amenity description one',
    max_occupancy= 5,
)

room_one = Room_Object(
    room_id= 'aaa',
    room_no= 7,
    hotel_id= 'llllll', 
    status= 'open24hrs',
    price= 547.00
)

maintenance_one = Maintenance_Request_Object(
    request_id= 'ggggg',
    hotel_id= 'llllll', 
    room_id= room_one.room_id,
    maintenance_description= 'something with ecosystem synchronization',
    reported_by_staff_id= '#45d',
    status = 'ongoing',
)

picture_one = Room_Picture_Object(
    picture_id= 'rrrr',
    room_id= room_one.room_id,
    picture_url= 'yyyyy',
    date_created= '1stMonthYear'
)


room_one.pictures.append(picture_one)
room_one.amenities.append(amenity_one)


#############################################################################

############################ TESTING FUNCTIONS ##############################


#create_rows(session, [amenity_one, room_one, maintenance_one, picture_one])
#read_row(session, 12 , "policy_object", "policy_id")


#contents = session.query(Room_Object).all()
#
#for item in contents:
#    print(item.room_no)
#    print(item.price)
#    for entity in item.pictures:
#        print(entity.picture_url, entity.date_created)
#        for pic in entity.rooms:
#            print(pic.room_no)
#            print(pic.price)
#            print(pic.room_id)
#



