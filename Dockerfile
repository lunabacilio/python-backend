# Usa una imagen base de Python
FROM python:3.13-alpine

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY users.json users.json

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación con gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]