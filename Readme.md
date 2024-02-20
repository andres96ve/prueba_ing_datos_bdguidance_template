# Prueba tecnica ingeniero de datos BD Guidance.

## Propuesta para el data warehouse de dvdrental.

La propuesta del datawarehouse consiste en un modelo estrella que contiene la tabla de hechos llamada Fact_Payment y 3 tablas dimensionales_Dim_Country,Dim_Film y Dim_Customer.

![image.png](https://res.craft.do/user/full/439fe800-da20-b63d-fbda-2763e3c7128c/doc/2565ce43-8e51-e7df-0f7b-fa416f581e05/48ed30dc-f241-456a-980f-24e77ee2e14a)

## Construccion de los Dockers

A continuacion se establecen los pasos requeridos para construir y correr los dockers en los que se encuentra el codigo para crear la base de datos transaccional (base_datos_transaccional), la base de datos en la que se almacena el Data Warehouse propuesto (data_warehouse) y el contenedor en el que se ejecutan los ETLs (etl_dw_dvdrental)

1. Se debe crear en el docker un network para la conexion de los contenedores, el comando a usar es:

```other
docker network create dw_network
```

2. Para crear el contenedor con la base de datos transaccional "dvdrental" en Postgres se deben ejecutar los siguientes comandos:

```other
cd base_datos_transaccional
docker build -t imagen_postgres .
docker run -d --net dw_network -p 5432:5432 --name dvdrental_contenedor imagen_postgres
```

3. Para crear la el contenedor en el que se almacena la base de datos Postgres "dw_dvdrental" en la que se genera el almacen de datos se debe ejecutar el siguiente comando:

```other
cd data_warehouse
docker build -t imagen_dw_dvdrental .
docker run -d --net dw_network -p 5431:5432 --name dw_dvdrental_contenedor imagen_dw_dvdrental
```

## Data Warehouse obtenido

El datawarehouse obetenido consiste en el modelo estrella mencionado anteriormente.

![WhatsApp Image 2024-02-20 at 5.16.48 PM.jpeg](https://res.craft.do/user/full/439fe800-da20-b63d-fbda-2763e3c7128c/doc/2565ce43-8e51-e7df-0f7b-fa416f581e05/db111280-8bd4-456f-b95d-00aa58d0b608)

En los archivos suministrados hay mayor detalle

## Tablero en Power BI

![WhatsApp Image 2024-02-20 at 5.20.56 PM.jpeg](https://res.craft.do/user/full/439fe800-da20-b63d-fbda-2763e3c7128c/doc/2565ce43-8e51-e7df-0f7b-fa416f581e05/08dd4cf1-3c54-42d5-b378-fec3fe8ee9c5)

