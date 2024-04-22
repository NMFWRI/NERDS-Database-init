import pandas as pd


def strip_value(x: str):
    if type(x) == str:
        return x.strip()
    else:
        return x


def generate_sqlalchemy_models(file_path, output_file):

    """
    This will read in the table definitions from file_path and generate a SQLAlchemy model .py file
    :param file_path: name of file containing table attribute definitions
    :param output_file: where .py file will be written
    """

    # Read the Excel file
    excel_file = "tables/" + file_path

    with open("models/" + output_file, 'w') as f:

        name_split = output_file.split('_')
        model_split = name_split[0]
        model_name = model_split.title()

        f.write("from sqlalchemy import Column, Integer, String, "
                "Float, Boolean, DateTime, ForeignKey, Text, Double, LargeBinary\n")
        f.write("from sqlalchemy.ext.declarative import declarative_base\n\n")
        f.write(f"{model_name}Base = declarative_base()\n\n")

        #### New code
        detail_df = pd.read_csv(excel_file)
        detail_df = detail_df.applymap(strip_value)
        tables = detail_df['TableName'].unique()
        ####

        for table_name in tables:
            # table_df = pd.read_excel(df, table_name)
            table_df = detail_df.loc[detail_df['TableName'] == table_name]

            # if table_name == 'Event':
            #     print("debug")

            if len(table_df) > 0:  # we need to make sure this is a table that's actually spec'd out
                has_pk = True in list(table_df['PK'])

                f.write(f"\nclass {table_name}({model_name}Base):\n")
                f.write(f"\t__tablename__ = '{table_name}'\n")

                if not has_pk:  # use AutoNumber as PK if not provided (rare)
                    f.write("\n\tID = Column(Integer, primary_key=True, autoincrement=True)")

                for _, row in table_df.iterrows():
                    # generate SQLAlchemy  field for each attribute in table
                    column_name = row['ColumnName']
                    column_type = row['DataType']
                    column_length = row['Length']
                    column_description = row['Description']
                    column_default = str(row['DefaultValue'])
                    # column_decimal_places = row['Decimals']
                    column_key = row['PK']
                    column_null = row['Nullable']
                    col_fk_table = row['ForeignTable']
                    col_fk_col = row['ForeignCol']

                    print(table_name + "." + column_name)

                    f.write(f"\n\t{column_name} = Column(\n\t\t")

                    # Select correct data type
                    if not pd.isna(column_type):
                        if column_type.title() == 'Integer' \
                                or column_type.title() == 'Single' \
                                or column_type == 'AutoNumber':
                            f.write("Integer")
                        elif column_type.title() == 'Float' or column_type.title() == 'Double':
                            if not pd.isna(column_length):
                                f.write(f"Double({int(column_length)})")
                            else:
                                f.write("Double()")
                        elif column_type.title() == 'String' \
                                or column_type.title() == 'Text' \
                                or column_type.title() == 'Complex Text':
                            if not pd.isna(column_length):
                                f.write(f"String({int(column_length)})")
                            else:
                                f.write("String()")
                        elif column_type.title() == 'Memo':  # a bit confusing, but necessary
                            f.write(f"Text")
                        elif column_type.title() == 'Boolean' or column_type == 'Yes/No':
                            f.write("Boolean")
                        elif column_type.title() == 'Datetime'\
                                or column_type.title() == 'Date'\
                                or column_type == 'Date/Time':
                            f.write("DateTime")
                        elif column_type.title() == 'Attachment':
                            f.write("LargeBinary")

                    # Declare foreign key if needed
                    if not pd.isna(col_fk_table) and not pd.isna(col_fk_col):
                        f.write(f",\n\t\tForeignKey('{col_fk_table}.{col_fk_col}')")

                    # Appropriately mark the primary key
                    if column_key:
                        f.write(f",\n\t\tprimary_key=True")

                    if column_type == 'AutoNumber':
                        f.write(f",\n\t\tautoincrement=True")

                    # Handle default value based on data type
                    if len(column_default) > 0:
                        if column_default.lower().strip('=') != 'null' and \
                                column_default.lower() != 'nan':
                            if column_type.title() == 'String' \
                                    or column_type.title() == 'Text' \
                                    or column_type.title() == 'Memo':
                                column_default = column_default.strip("\"")
                                f.write(f',\n\t\tdefault="""{column_default}"""')

                            elif column_type.title() == 'Boolean' or column_type.title() == 'Yes/No':
                                if column_default.lower() == 'yes' or column_default.lower() == '1':
                                    f.write(',\n\t\tdefault=True')
                                elif column_default.lower() == 'no' or column_default.lower() == '0':
                                    f.write(',\n\t\tdefault=False')
                            else:
                                f.write(f",\n\t\tdefault={column_default}")

                    # SQLAlchemy 'comment' field holds the descriptions
                    if not pd.isna(column_description):
                        f.write(f',\n\t\tcomment="""{column_description}"""')

                    # Is Nullable
                    if not pd.isna(column_null):
                        if type(column_null) == float:
                            if column_null < 1:
                                f.write(f",\n\t\tnullable=False")
                        elif type(column_null) == bool:
                            if not column_null:
                                f.write(f",\n\t\tnullable=False")
                        else:
                            f.write(f",\n\t\tnullable={column_null.title()}")

                    f.write("\n\t\t)")

                f.write("\n\n")

    print(f'Successfully generated SQLAlchemy models. Saved in {output_file}')