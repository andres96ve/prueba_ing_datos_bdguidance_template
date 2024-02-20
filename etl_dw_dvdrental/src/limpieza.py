import cargar_tablas as ct  

def clean_dataframes():
    dataframes = ct.read_tables_from_database() 

    for df_name, dataframe in dataframes.items():
        #Covertir listas que estan contenidas en columnas
        def convert_to_text(value):
            
            if isinstance(value, list):
                # Separar por ',' donde haya listas
                return ', '.join(map(str, value))
            else:
                return str(value)
        
        for column in dataframe.columns:
            # Observar si hay una lista en la columna
            if dataframe[column].apply(lambda x: isinstance(x, list)).any():
                # Si hay una lista convertirla en string
                dataframe[column] = dataframe[column].apply(convert_to_text)
        
        #Remover duplicados, nulos y convertir en minusculas
        dataframes[df_name] = dataframe.dropna().drop_duplicates().apply(lambda x: x.astype(str).str.lower())

    return dataframes

clean_dataframes()

