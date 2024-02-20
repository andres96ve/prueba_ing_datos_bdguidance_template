import pandas as pd
import psycopg2
import traceback



# Function to create the Data Warehouse and save it in the DB folder
def create_dwh(db_name, db_user, db_password, db_host, db_port):
    try:
        # Create connection to PostgreSQL
        conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = conn.cursor()

        
        cursor.execute("""CREATE TABLE IF NOT EXISTS Dim_Country(
            country_id INTEGER PRIMARY KEY,
            country CHARACTER VARYING(50) NOT NULL,
            last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL);""")
        

        cursor.execute("""CREATE TABLE IF NOT EXISTS Dim_Film(
            film_id integer PRIMARY KEY,
            title character varying(255) NOT NULL,
            description text,
            release_year date,
            language_id smallint NOT NULL,
            rental_duration smallint NOT NULL DEFAULT 3,
            rental_rate numeric(4,2) NOT NULL DEFAULT 4.99,
            length smallint,
            replacement_cost numeric(5,2) NOT NULL DEFAULT 19.99,
            rating CHAR(5) DEFAULT 'G',
            last_update timestamp without time zone NOT NULL,
            special_features text[],
            fulltext tsvector NOT NULL);""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS Dim_Customer(
            customer_id integer PRIMARY KEY,
            store_id smallint NOT NULL,
            first_name character varying(45) NOT NULL,
            last_name character varying(45) NOT NULL,
            email character varying(50),
            address_id smallint NOT NULL,
            activebool boolean NOT NULL,
            create_date date NOT NULL,
            last_update timestamp without time zone,
            active integer);""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS Fct_Payment(
            payment_id  smallint PRIMARY KEY,
            customer_id  smallint NOT NULL,
            country_id  smallint NOT NULL,
            film_id  smallint NOT NULL,   
            amount numeric(5,2) NOT NULL,
            payment_date timestamp without time zone NOT NULL,                     
            FOREIGN KEY (customer_id) REFERENCES Dim_Customer(customer_id),
            FOREIGN KEY (country_id) REFERENCES Dim_Country(country_id),        
            FOREIGN KEY (film_id) REFERENCES Dim_Film(film_id))""")
        # Close connection
        conn.commit()
        conn.close()
    except Exception as e:
        print('Error: ', e)
        print(traceback.format_exc())
    return None