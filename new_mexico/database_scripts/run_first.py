from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date, Float, Boolean
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry
import settings
import pudb

#This script connects to the database and creates a new table ScrapeChecklists
#We populate well_id, api_number, and url from the Wells table

engine = create_engine(URL(**settings.DATABASE))
Base = declarative_base(engine)
DeclarativeBase = declarative_base()
def create_scrape_checklist(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

def loadSession():
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session=Session()
    return session

class Wells(Base):
    """Sqlalchemy well model (this table imported initially from shapefile)"""
    __tablename__ = "wells"
    __table_args__= {'autoload':True, 
                     'schema': 'import'}


class ScrapeChecklists(DeclarativeBase):
    """Sqlalchemy well details model"""
    __tablename__ = "scrape_checklists"
    __table_args__ = {'schema':'import'}

    id = Column(Integer, primary_key = True)
    well_id = Column('well_id', Integer)
    api_number = Column('api_number', String)
    url = Column('url', String)
    well_info_2017 = Column('well_info_2017', Boolean, nullable = False, default = False)
    wi_updated_2017 = Column('wi_updated_2017', Date)
    const_2017 = Column('const_2017', Boolean, nullable = False, default = False)
    con_updated_2017 = Column('con_updated_2017', Date)
    comp_2017 = Column('comp_2017', Boolean, nullable = False, default = False)
    cmp_updated_2017 = Column('cmp_updated_2017', Date)
    inc_2017 = Column('inc_2017', Boolean, nullable = False, default = False)
    inc_updated_2017 = Column('inc_updated_2017', Date)


if __name__ == "__main__":
    session = loadSession()
    create_scrape_checklist(engine)
    pu.db

    res = session.query(Wells).all()

    
