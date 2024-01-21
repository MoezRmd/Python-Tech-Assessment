import databases
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, exc, inspect


class SqlConnector:
    def __init__(self, database_url):

        try:
            self.engine = create_engine(database_url, connect_args={'check_same_thread': False})
            self.connection = self.engine.connect()
            print("Connection established successfully.")
        except exc.SQLAlchemyError as e:
            print(f"Error establishing connection: {e}")

    def create_table(self, df, table_name):
        inspector = inspect(self.engine)
        if inspector.has_table(table_name):
            print(f"Table {table_name} exists")
        else:

            df.to_sql(table_name, self.engine, if_exists='replace', index=False)

    def insert_dataframe(self, df, table_name):
        df.to_sql(table_name, self.engine, if_exists='append', index=False)

    def read_data(self, table_name):
        try:
            query = f"SELECT * FROM {table_name}"
            result = pd.read_sql(query, self.connection)
            return result
        except exc.SQLAlchemyError as e:
            print(f"Error reading data from {table_name}: {e}")
            return None