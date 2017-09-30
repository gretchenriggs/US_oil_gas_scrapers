from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date, Float, Boolean, ForeignKey
from geoalchemy2 import Geometry
import settings

DeclarativeBase = declarative_base()

#Simple find between function for strings
#Needed for the well details parser
def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

def replace_blanks_clean(dictionary):
    for key in dictionary:
        text = dictionary[key].strip()
        if text == "":
            dictionary[key] = None
        else:
            dictionary[key] = text

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_well_details(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class WellDetails(DeclarativeBase):
    """Sqlalchemy well details model"""
    __tablename__ = "well_details"
    __table_args__ = {'schema':'import'}

    id = Column(Integer, primary_key = True)
    well_id = Column('well_id', Integer)
    api_number = Column('api_number', String)
    well_no = Column('well_no', String, nullable = True)
    property_name = Column('property_name', String, nullable = True)
    property_number = Column('property_number', Integer, nullable = True)
    operator_name = Column('operator_name', String, nullable = True)
    operator_number = Column('operator_number', Integer, nullable = True)
    status =  Column('status', String, nullable = True)
    well_type =  Column('well_type', String, nullable = True)
    work_type =  Column('work_type', String, nullable = True)
    direction =  Column('direction', String, nullable = True)
    multi_lateral =  Column('multi_lateral', String, nullable = True)
    mineral_owner =  Column('mineral_owner', String, nullable = True)
    surface_owner =  Column('surface_owner', String, nullable = True)
    surface_location =  Column('surface_location', String, nullable = True)
    latitude =  Column('latitude', Float(50), nullable = True)
    longitude =  Column('longitude', Float(50), nullable = True)
    coord_sys =  Column('coord_sys', String, nullable = True)
    gl_elevation =  Column('gl_elevation', String, nullable = True)
    kb_elevation =  Column('kb_elevation', String, nullable = True)
    df_elevation =  Column('df_elevation', String, nullable = True)
    sing_mult_completion =  Column('sing_mult_completion', String, nullable = True)
    potash_waiver =  Column('potash_waiver', Boolean, nullable = True)
    prop_form =  Column('prop_form', String, nullable = True)
    prop_depth =  Column('prop_depth', Integer, nullable = True)
    tvd =  Column('tvd', Integer, nullable = True)
    mvd =  Column('mvd', Integer, nullable = True)
    pbd =  Column('pbd', Integer, nullable = True)
    init_apd_apprv =  Column('init_apd_apprv', Date, nullable = True)
    apd_eff =  Column('apd_eff', Date, nullable = True)
    apd_exp =  Column('apd_exp', Date, nullable = True)
    apd_cancel =  Column('apd_cancel', Date, nullable = True)
    apd_ext =  Column('apd_ext', Date, nullable = True)
    spud =  Column('spud', Date, nullable = True)
    ta_date =  Column('ta_date', Date, nullable = True)
    ta_exp =  Column('ta_exp', Date, nullable = True)
    shut_in =  Column('shut_in', Date, nullable = True)
    pa_intent =  Column('pa_intent', Date, nullable = True)
    pa_date =  Column('pa_date', Date, nullable = True)
    site_release =  Column('site_release', Date, nullable = True)
    last_insp =  Column('last_insp', Date, nullable = True)
    gas_cap_plan =  Column('gas_cap_plan', Date, nullable = True)
    ta_exp =  Column('ta_exp', Date, nullable = True)
    pnr_exp =  Column('pnr_exp', Date, nullable = True)
    last_mit_bht =  Column('last_mit_bht', Date, nullable = True)
