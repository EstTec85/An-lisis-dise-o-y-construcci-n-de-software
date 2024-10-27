# Imagen base ligera de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia todos los archivos del proyecto a /app
COPY . .

# Instala las dependencias listadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8501
EXPOSE 8501

# Comando para ejecutar la aplicación con Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
