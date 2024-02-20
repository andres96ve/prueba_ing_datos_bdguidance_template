import psycopg2
import pandas as pd

def fact_table_create():
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='12345',
            database='dvdrental'
        )

        print('Conexión exitosa')

        # Ejecutar una consulta SQL
        cursor = connection.cursor()
        query = """CREATE TEMPORARY TABLE temp_table as
                SELECT t1.payment_id,t1.amount,t1.payment_date,t5.country_id,t8.film_id,t9.customer_id
                FROM payment as t1
                JOIN staff as t2
                ON t1.staff_id=t2.staff_id
                JOIN address as t3
                ON t2.address_id=t3.address_id
                JOIN city as t4
                ON t3.city_id=t4.city_id
                JOIN country as t5
                ON t4.country_id=t5.country_id
                JOIN rental as t6
                ON t1.rental_id=t6.rental_id
                JOIN inventory as t7
                ON t6.inventory_id=t7.inventory_id
                JOIN film as t8
                ON t7.film_id=t8.film_id
                JOIN customer as t9
                ON t1.customer_id=t9.customer_id;"""
        cursor.execute(query)

        # Obtener los datos de la tabla temporal en un DataFrame
        cursor.execute("SELECT * FROM temp_table;")
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=column_names)

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()


        return df
    


    except psycopg2.Error as e:
        print('Error al conectarse a la base de datos:', e)
        return None
    
fact_table_create()

