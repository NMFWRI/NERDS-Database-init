import sys
import json
import pandas as pd


def create_url(**kwargs):
    """
    create a SQLAlchemy URL out of a config file parameters
    The config.ini file is excluded from the git repository for security purposes; you'll have to create your own for
    your own s

    """
    driver = kwargs['driver']
    if 'user' in kwargs:
        user = kwargs.get('user')
    if 'password' in kwargs:
        pwd = kwargs.get('password')
    if 'server' in kwargs:
        server = kwargs.get('server')
    database = kwargs['database']

    if 'postgresql' in kwargs['type'].lower():
        conn_str = f"{driver}://{user}:{pwd}@{server}/{database}"

    elif 'mssql' in kwargs['type'].lower():
        conn_str = f"{driver}://{user}:{pwd}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

    elif 'access' in kwargs['type'].lower():
        conn_str = f"{driver}:///?odbc_connect=Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={database}"

    else:
        return ""

    return conn_str


def excel_to_json(input_file):
    # Read the .xlsx file into a pandas DataFrame
    df = pd.read_excel(input_file)

    # Convert the DataFrame to a dictionary with column values mapped to each other
    mapping_dict = df.set_index('Column1')['Column2'].to_dict()

    # Write the dictionary to a JSON file
    with open('output_file.json', 'w') as json_file:
        json.dump(mapping_dict, json_file)

    print('Conversion completed. JSON file created.')
