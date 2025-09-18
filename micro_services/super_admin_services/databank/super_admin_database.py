from sqlalchemy import create_engine, Integer, String, Boolean, ForeignKey, Table, Float, Column
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped
from sqlalchemy.orm import mapped_column, sessionmaker
from typing import List

###############################################################################

DATABASE_URL = "postgresql+psycopg2://invinsible:$omniman#@localhost:9030/super_admin_bank"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


###############################################################################

class Base(DeclarativeBase):
    pass

###############################################################################

########################  INTERMEDIATE TABLES  #################################

Tenant_Super_Admin_Association = Table (
    'tenant_super_admin_association',
    Base.metadata,
    Column('tenant_id', ForeignKey('tenant_object.tenant_id'), primary_key=True),
    Column('super_admin_id', ForeignKey('super_admin_object.super_admin_id'), primary_key=True),
)


###############################################################################

########################## TABLE INITIALIZATION ###########################


class Tenant_Object(Base):
    __tablename__ = 'tenant_object'

    tenant_id: Mapped[str] = mapped_column(String, primary_key=True)
    tenant_name: Mapped[str] = mapped_column(String)
    subscription_plan: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)

    super_admins: Mapped[List['Super_Admin_Object']] = relationship(
        secondary=Tenant_Super_Admin_Association,
        back_populates='tenants'
    )


class Super_Admin_Object(Base):
    __tablename__ = 'super_admin_object'

    super_admin_id: Mapped[str] = mapped_column(String, primary_key=True)
    user_id: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(String)
    last_login_at: Mapped[str] = mapped_column(String)

    super_admin_billing_wormhole: Mapped['Billing_Info_Object'] = relationship(back_populates='billing_super_admin_wormhole')

    tenants: Mapped[List['Tenant_Object']] = relationship(
        secondary=Tenant_Super_Admin_Association,
        back_populates='super_admins'
    )


class Billing_Info_Object(Base):
    __tablename__ = 'billing_info_object'

    billing_info_id: Mapped[str] = mapped_column(String, primary_key=True)
    next_payment_in_days: Mapped[int] = mapped_column(Integer)
    total_amount: Mapped[float] = mapped_column(Float)
    payment_transaction_id: Mapped[str] = mapped_column(String)

    super_admin_id: Mapped[str] = mapped_column(ForeignKey('super_admin_object.super_admin_id'))
    tenant_id: Mapped[str] = mapped_column(ForeignKey('tenant_object.tenant_id'))

    billing_super_admin_wormhole: Mapped['Super_Admin_Object'] = relationship(back_populates='super_admin_billing_wormhole')




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

tenant_one = Tenant_Object(
    tenant_id = '#8555',
    tenant_name = 'Neptune_Global',
    subscription_plan = 'dhdg',
    status = 'operational',
    created_at = '7thDay'
)

super_admin_one = Super_Admin_Object(
    super_admin_id = '5452d4',
    user_id = '3dfgh',
    created_at = 'Sept',
    last_login_at = '5452d4',
)

billing_info_one = Billing_Info_Object(
    billing_info_id= 'billing01',
    tenant_id = tenant_one.tenant_id,
    super_admin_id= super_admin_one.super_admin_id,
    next_payment_in_days= 23,
    total_amount= 568.35,
    payment_transaction_id= 'yrt0023'
)

super_admin_one.tenants.append(tenant_one)


#############################################################################

############################ TESTING FUNCTIONS ##############################


create_rows(session, [super_admin_one, tenant_one, billing_info_one])
#read_row(session, 12 , "policy_object", "policy_id")


#contents = session.query(Policy_Object).all()
#
#for item in contents:
#    print(item.policy_id)
#    print(item.policy_name)
#    for entity in item.roles:
#        print(entity.role_id, entity.role_name)




