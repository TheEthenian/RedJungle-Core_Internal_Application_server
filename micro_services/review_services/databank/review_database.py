from sqlalchemy import create_engine, Integer, Boolean, ForeignKey, Table, String, Float, Column
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from typing import List

###############################################################################

DATABASE_URL = "postgresql+psycopg2://invinsible:$omniman#@localhost:9005/review_bank"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


###############################################################################


class Base(DeclarativeBase):
    pass


###############################################################################

########################  INTERMEDIATE TABLES  #################################

Review_Picture_Association = Table (
    'review_picture_association',
    Base.metadata,
    Column('review_id', ForeignKey('review_object.review_id'), primary_key=True),
    Column('picture_id', ForeignKey('picture_object.picture_id'), primary_key=True)
)

Review_Message_Association = Table (
    'review_message_association',
    Base.metadata,
    Column('review_id', ForeignKey('review_object.review_id'), primary_key=True),
    Column('message_id', ForeignKey('message_object.message_id'), primary_key=True),
)


###############################################################################

########################## TABLE INITIALIZATION ###########################

class Review_Object(Base):
    __tablename__ = 'review_object'

    review_id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(String)
    tenant_id: Mapped[str] = mapped_column(String)
    date_created: Mapped[str] = mapped_column(String)
    date_updated: Mapped[str] = mapped_column(String)

    pictures: Mapped[List['Picture_Object']] = relationship(
        secondary= Review_Picture_Association,
        back_populates= 'reviews'
    )

    messages: Mapped[List['Message_Object']] = relationship(
        secondary= Review_Message_Association,
        back_populates= 'reviews'
    )



class Picture_Object(Base):
    __tablename__ = 'picture_object'

    picture_id: Mapped[str] = mapped_column(String, primary_key=True)
    picture_url: Mapped[str] = mapped_column(String)
    date_created: Mapped[str] = mapped_column(String)

    reviews: Mapped[List['Review_Object']] = relationship(
        secondary= Review_Picture_Association,
        back_populates= 'pictures'
    )



class Message_Object(Base):
    __tablename__ = 'message_object'

    message_id: Mapped[str] = mapped_column(String, primary_key=True)
    message_text: Mapped[str] = mapped_column(String)
    date_created: Mapped[str] = mapped_column(String)
    date_updated: Mapped[str] = mapped_column(String)

    reviews: Mapped[List['Review_Object']] = relationship(
        secondary= Review_Message_Association,
        back_populates= 'messages'
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


review_one = Review_Object(
    review_id= 'review1',
    user_id= 'qqq',
    tenant_id= '#534',
    date_created= '12thDec',
    date_updated= '25thJan'
)

picture_one = Picture_Object(
    picture_id= 'ghl', 
    picture_url= 'url/some/me',
    date_created= '14thDec'
)

message_one = Message_Object(
    message_id= 'rrrr',
    message_text= 'This is the review message',
    date_created= 'yyyyy',
    date_updated= '1stMonthYear'
)


review_one.pictures.append(picture_one)
review_one.messages.append(message_one)

#############################################################################

############################ TESTING FUNCTIONS ##############################


#create_rows(session, [picture_one, message_one, review_one])
#read_row(session, 12 , "policy_object", "policy_id")


contents = session.query(Review_Object).all()
#
for item in contents:
    print(item.user_id)
    print(item.tenant_id)
    for entity in item.messages:
        print('Messages')
        print(entity.message_id, entity.message_text)
    for entity in item.pictures:
        print('Pictures')
        print(entity.picture_id, entity.picture_url)







