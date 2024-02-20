# Usa la imagen oficial de Python 3.9.7 como base
FROM python:3.9.7

# Copia todos los scripts al directorio de trabajo del contenedor
COPY . /app

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /app/src

# Instala las dependencias de tu proyecto (si tienes un requirements.txt)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puertos para PostgreSQL
EXPOSE 5432
EXPOSE 5431

# Ejecuta el script por defecto cuando se inicie el contenedor
CMD ["python", "etl_dw_rental.py"]