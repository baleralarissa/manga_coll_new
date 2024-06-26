import json
import mysql.connector

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# insert dados na tabela manga_collection.all_volumes
def insert_data(data, conn):
    cursor = conn.cursor()
    for item in data:
        volume = item.get('volume')
        titulo = item.get('titulo')
        author = item.get('author')
        status = item.get('status')
        col_id = item.get('id_col')
        
        insert_query = """
        INSERT INTO manga_collection.all_volumes (volume, titulo, author, status, col_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (volume, titulo, author, status, col_id))
    conn.commit()
    cursor.close()

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="manga_collection"
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

json_file_path = 'manga_collection.all_volumes.json'

data = read_json(json_file_path)

conn = connect_db()

if conn:
    insert_data(data, conn)
    conn.close()
