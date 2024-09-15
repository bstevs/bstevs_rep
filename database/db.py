import pymysql

# Configuración de la conexión
host = "database-1-bstevs.cnmus6my2abt.us-east-2.rds.amazonaws.com"
user = "bstevs"
passw = "Aws123456789*"
db_name = "db_users"

def connection_SQL():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=passw,
            database=db_name
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except Exception as err:
        print("Error de conexión:", err)
        return None

def insert_employee_task(employee_name, job_activity, job_description, employee_id):
    try:
        instruction = """
        INSERT INTO employee_tasks (employee_name, job_activity, job_description, employee_id)
        VALUES (%s, %s, %s, %s);
        """
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction, (employee_name, job_activity, job_description, employee_id))
        connection.commit()
        connection.close()
        print("Tarea añadida")
    except Exception as err:
        print("Error al añadir tarea:", err)
