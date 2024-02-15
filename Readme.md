# Prueba técnica ingeniero de datos BD Guidance

## Objetivo

Evaluar los conocimientos de los candidatos relacionados al uso de herramientas utilizadas en la ingeniería de datos y las actividades propias del cargo en BD Guidance, como lo son: el uso de Docker, GitHub, Python y Power BI para la generación de bases de datos, consultas SQL y el uso de Python (o cualquier otro lenguaje y herramientas como pyspark y airflow) para la creación de pipelines que permitan la extracción, transformación y creación de una bodega de datos, así como su uso en la creación de un dashboard analitico en Power BI. 

## Problema propuesto

Se propone la creación de un Data Warehouse para una tienda ficticia que comercializa dvd 's llamada dvdrental, se debe partir de los datos transaccionales para generar procesos de extracción, transformación y carga. Posterior a la creación del data warehouse se debe diseñar un dashboard en Power BI, en el que se muestren los siguientes indicadores y gráficos:

1. Ventas totales en USD.
2. Cantidad total de las transacciones de ventas.
3. Gráfico con las ventas en dólares por país en los que se ubican las tiendas.
4. Gráfico de ventas en dólares a través del tiempo.
5. Identificar los cinco clientes con mayor valor total en compras.
6. Identificar las cinco películas con mayores ventas totales.

Las tareas a desarrollar son las siguientes:

- Clonar el repositorio https://github.com/bdg-ittic/prueba_ing_datos_bdguidance_template.git de GitHub, en el que se encuentra la plantilla general y los datos a usar. 
- Levantar los contenedores Docker que se encuentra en el repositorio, estos crearan las bases de datos con motor Postgres a usar, tanto para la consulta como donde debe ubicarse el Data Warehouse.
- Familiarizarse con la base de datos dvdrental.
- Proponer un modelo físico del almacén de datos, este debe ser un modelo de estrella compuesto por tablas de dimensiones y hechos, la finalidad del data warehouse es el de asistir con datos que permitan la creación del Dashboard en Power BI con los elementos propuestos.
- En el contenedor Docker en el que se encuentra el proceso para la generación de los ETLs, se debe generar el código requerido para la ejecución de los pipelines que se encargan de las transformaciones de datos y llevarlos al contenedor Docker en el que se levanta el almacén de datos.
- El contenedor Docker con el Data Warehouse debe contener un modelo de estrella que se encuentre conformado por las tablas de dimensiones y hechos propuestas. El objetivo del almacén de datos es el de permitir el análisis de datos.
- Se debe generar un dashboard en Power BI, debe conectarse al contenedor en el que se encuentra el almacén de datos, este debe de permitir visualizar los elementos propuestos. Aplicar técnicas de visualización de datos y buenas prácticas en la creación de tableros de control.

## Entregables

1. Se debe crear un nuevo repositorio de GitHub, que contenga el código usado, junto con los documentos con las tareas resueltas y se debe cargar una imagen en el que se muestre el modelo de estrella propuesto (modelo físico). 
2. Se debe de cargar al repositorio de GitHub el archivo .pbix que contiene el tablero de control.
3. Incluir en el GitHub un documento tipo Markdown en el que se documente de manera general las tareas realizadas, agregando los comentarios que considere necesarios e imágenes de los resultados.

Para BD Guidance es muy importante que sus trabajadores tengan un alma investigativa e inquieta intelectualmente, así que si no conoce o ha usado alguna de estas herramientas, esta es una oportunidad para aprender y mostrarnos sus cualidades en la resolución de problemas técnicos y el aprendizaje continuo. Proponemos algunas herramientas, pero queda a su criterio la utilización de las que considere necesarias para ejecutar las tareas propuestas.

Le deseamos un feliz desarrollo de la prueba, quedamos atentos ante cualquier duda que se presente. La fecha límite de plazo para la entrega de la prueba es el 20 de febrero a las 5:00 pm, el medio de entrega usado es la notificación por medio de correo electrónico a fabian.pedreros@bdguidance.com, en el que se comparte el link al repositorio en el que se encuentran todos los entregables mencionados.

Gracias.