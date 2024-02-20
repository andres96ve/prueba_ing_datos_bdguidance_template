import psycopg2
import pandas as pd

def read_tables_from_database():
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='12345',
            database='dvdrental'
        )

        print('Conexión exitosa')

        # Lista de tablas
        #tables = ['payment', 'staff', 'store', 'address', 'city', 'country', 'rental', 'inventory', 'film', 'customer']
        tables = ['country', 'film', 'customer']

        # Diccionario para almacenar los DataFrames
        dfs = {}

        # Iterar sobre las tablas y leer cada una
        for table in tables:
            query = f"SELECT * FROM {table}"
            dfs[table] = pd.read_sql_query(query, connection)
        print(dfs['film'])
        connection.close()
        return dfs
        

    except psycopg2.Error as e:
        print('Error al conectarse a la base de datos:', e)
        return None


