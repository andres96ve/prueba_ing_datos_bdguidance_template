import pandas as pd
from sqlalchemy import create_engine
import cargar_tablas as ct
import creacion_fact as cf
import dwh



def insert_data():

    db_name = 'dw_dvdrental'
    db_user='postgres'
    db_host='localhost'
    db_password='12345'
    db_port='5431'
    db_url = 'postgresql://postgres:12345@localhost:5431/dw_dvdrental'

    dwh.create_dwh(db_name, db_user, db_password, db_host, db_port)
    print('tablas creadas')
    dataframes=ct.read_tables_from_database()
    fact_df=cf.fact_table_create()
    dataframes['payment']=fact_df

    # Conecta a la base de datos PostgreSQL
    engine = create_engine(db_url)
    table_name=['Dim_Country', 'Dim_Film', 'Dim_Customer','Fct_Payment']

    
    # Itera sobre cada DataFrame y tabla correspondiente
    dataframes_items = dataframes.items()

    # Iterar sobre las listas paralelas (tuplas) usando zip()
    for (table_name, dataframe), table_name in zip(dataframes_items, table_name):
        # Insertar el DataFrame en la tabla correspondiente
        dataframe.to_sql(table_name, engine, if_exists='append', index=False)

insert_data()    