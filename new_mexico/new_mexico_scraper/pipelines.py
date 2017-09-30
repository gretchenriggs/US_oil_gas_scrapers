from sqlalchemy.orm import sessionmaker
from models import WellDetails, db_connect, create_well_details
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewMexicoScraperPipeline(object):
    """Pipeline for storing scraped items from the New Mexico webpage in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_well_details(engine)
        self.Session= sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """ Save well details into the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        #Set search path to import
        session.execute("set search_path to import")
        well_detail = WellDetails(**item)        
        try:
            session.add(well_detail)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
