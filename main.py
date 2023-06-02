import psycopg2
conn = psycopg2.connect(
    user="nico", password="1234", port="5432", host="localhost", database="db_curso"
)
cursor = conn.cursor()

# Crear tabla en bdd
cursor.execute(
    "CREATE TABLE IF NOT EXISTS comprador (id SERIAL PRIMARY KEY, nombre VARCHAR(255), edad INTEGER, correo VARCHAR(255))"
)

# guarda la informacion
conn.commit()