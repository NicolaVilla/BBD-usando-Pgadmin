import psycopg2
conn = psycopg2.connect(
    user="nico", password="1234", port="5432", host="localhost", database="db_curso"
)
cursor = conn.cursor()

# Crear tabla en bdd
cursor.execute(
    "CREATE TABLE IF NOT EXISTS compradores (id SERIAL PRIMARY KEY, nombre VARCHAR(255), edad INTEGER, correo VARCHAR(255))"
)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS autos (id SERIAL PRIMARY KEY, marca VARCHAR(255), modelo INTEGER, patente VARCHAR(255))"
)
# guarda la informacion
conn.commit()

def insertar_comprador(nombre,edad,correo):
    cursor.execute(
        "INSERT INTO compradores (nombre, edad, correo) VALUES (%s, %s, %s)",
        (nombre, edad, correo),
    )
def insertar_auto(marca, modelo, patente):
    cursor.execute(
        "INSERT INTO autos (nombre, edad, correo) VALUES (%s, %s, %s)",
        (marca, modelo, patente),
    )

def mostrar_compradores():
    cursor.execute("SELECT * FROM compradores")
    print(cursor.fetchall())

def mostrar_clientes():
    cursor.execute("SELECT * FROM compradores")
    print(cursor.fetchall())