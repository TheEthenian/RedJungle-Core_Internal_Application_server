from sqlalchemy import create_engine, Integer, String, ForeignKey, Column, Table
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from functions.main_function import load_yaml_config
from typing import List


###############################################################################

config_data = load_yaml_config('../config_database.yaml')

db_username = config_data['user_info_microservice']['database']['db_username']
db_passcode = config_data['user_info_microservice']['database']['db_passcode']
db_url = config_data['user_info_microservice']['database']['db_url']
db_port = config_data['user_info_microservice']['database']['db_port']
db_name = config_data['user_info_microservice']['database']['db_name']


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


User_Profile_Association = Table (
    'user_profile_association',
    Base.metadata,
    Column('user_id', ForeignKey('user_object.user_id'), primary_key=True),
    Column('profile_id', ForeignKey('profile_object.profile_id'), primary_key=True)
)

###############################################################################

########################## TABLE INITIALIZATION ###########################

class User_Object(Base):
    __tablename__ = 'user_object'

    user_id: Mapped[str] = mapped_column(String, primary_key=True)
    tenant_id: Mapped[str] = mapped_column(String)
    role_id: Mapped[str]= mapped_column(String, default='no role')
    created_at: Mapped[str] = mapped_column(String, default='timenow')
    updated_at: Mapped[str] = mapped_column(String, default='updated_date')

    profiles: Mapped[List['Profile_Object']] = relationship(
        secondary= User_Profile_Association,
        back_populates= 'users'
    )

class Profile_Object(Base):
    __tablename__ = 'profile_object'

    profile_id: Mapped[str] = mapped_column(String, primary_key=True)
    profile_picture_url: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String, default=None)
    email: Mapped[str] = mapped_column(String, default=None)
    phone_number: Mapped[int] = mapped_column(Integer, default=None)

    users: Mapped[List['User_Object']] = relationship(
        secondary= User_Profile_Association,
        back_populates= 'profiles'
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


profile_one = Profile_Object(
    profile_id= '5sdfsdsd8f',
    profile_picture_url= '78sdfsfs78',
    first_name= 'Some',
    last_name= 'Individual',
    email= 'Some@company.org',
    phone_number= 25486
)


user_one = User_Object(
    user_id= '005',
    tenant_id= '#7854'
)


user_one.profiles.append(profile_one)

#############################################################################

############################ TESTING FUNCTIONS ##############################


#create_rows(session, [profile_one, user_one])
#read_row(session, 12 , "policy_object", "policy_id")


contents = session.query(User_Object).all()
#
for item in contents:
    print(item.user_id)
    print(item.role_id)
    for entity in item.profiles:
        print(entity.first_name, entity.email, entity.phone_number)





