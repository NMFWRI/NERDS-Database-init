import pandas as pd

from func.functions import create_url
from func.alchemy import generate_sqlalchemy_models
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
import os
import configparser
import sys


class CollectionDB:
    """
    Class to collect database/server information in table manipulations.
    This functionality is specific to just Riparian or Uplands databases created for NMFWRI.
    Some of this will need to be manually changed in the config files, including defining tables in a well-formatted
    Excel workbook/.xlsx file type and the database config .ini file for database server connections.
    """

    def __init__(self, config_file, param_name):
        self.name = param_name
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.params = self.config[self.name]
        self.url = create_url(**self.params)
        self.engine = create_engine(self.url)
        self.base = None

        if 'Uplands' in param_name:
            self.base = UplandsBase
        elif 'Riparian' in param_name:
            self.base = RiparianBase

    def create_tables(self):

        """
        Creates tables for a database as defined in the models file. Code is very easy to read.
        """

        print(f"Creating tables for {self.name}")
        self.base.metadata.create_all(self.engine)

    def clear_tables(self):

        """For use in resetting a database if tables need to be changed at all. Code is self-explanatory."""

        server_meta = MetaData()
        server_meta.reflect(self.engine)

        print(f"Dropping all tables for {self.name}")

        server_meta.drop_all(self.engine)

    def insert_codes(self):
        """
        This will insert the data for damage codes, damage severity, and species saved as .csv in the program directory
        :return: static method
        """

        for table in ['LUDamageCodes', 'LUDamageSev', 'LUSpecies']:
            csv_file = table + '.csv'
            csv_path = os.path.join('tables', csv_file)

            df = pd.read_csv(csv_path, encoding='latin')
            with Session(self.engine) as conn:
                try:
                    df.to_sql(table, conn.bind, if_exists='replace', index=False)
                except Exception as e:
                    conn.rollback()
                    print(e)

    def clear_and_create(self):
        """
        Drops all the tables from the current database and creates new ones
        """

        self.clear_tables()
        self.create_tables()
        self.insert_codes()


if __name__ == '__main__':

    """
    To use this, call from the terminal the following:
    
    py create_tables.py [Uplands[Access | MSSQL] | Riparian[Access | MSSQL]] [Field Mapping path] [SQLAlchemy model path]
    
    Choice 1 dictates whether the the tables are for the Uplands protocols or Riparian protocols.
    
    Choice 2 is the path to the field mapping Excel workbook. This is a document that provides table definitions for 
    the tables used for each of these protocols defined in an Excel workbook. Each sheet in the workbook contains the 
    definition for a table. The sheet contains table name, corresponding table in FFI database (used by another script),
    primary or foreign key designation, data type, field length, decimal places if applicable, default value, null
    capabilities, corresponding foreign table, and corresponding foreign key column. Workbooks are stored in the tables 
    subfolder in the project directory.
    
    Choice 3 is the location of the SQLAlchemy model generated in the process. Models are stored in the models/ 
    directory.
    """

    if len(sys.argv) == 4:
        config_set = sys.argv[1]
        def_file = f"{sys.argv[2]}.csv"
        model_file = f"{sys.argv[3]}.py"

        generate_sqlalchemy_models(def_file, model_file)

        from models.riparian_models import *
        from models.uplands_models import *

        db = CollectionDB('config/servers.ini', config_set)
        db.clear_and_create()

    else:
        print('Please provide a database config selection.')
