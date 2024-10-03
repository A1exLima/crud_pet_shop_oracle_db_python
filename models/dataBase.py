from dotenv import load_dotenv
import os
import oracledb
from models.system import clean_screen

def database_connection() -> bool:
    load_dotenv()
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')

    global conn, inst_register, inst_consultation, inst_change, inst_exclusion

    try:
        conn = oracledb.connect(
            user=user,
            password=password,
            dsn='localhost:1521/XE'
        )

        inst_register = conn.cursor()
        inst_consultation = conn.cursor()
        inst_change = conn.cursor()
        inst_exclusion = conn.cursor()

    except Exception as Error:
        print(f'Erro: {Error}')
        connection = False
        return connection

    else:
        connection = True
        return connection

    finally:
        clean_screen()
        print(f"➡️   Oracle database connection... {
              '✅' if connection == True else '🚫'}\n")


def register_data_in_the_database(pet_type: str, pet_name: str, pet_age: int) -> None:
    try:
        register = f"""
          INSERT INTO petshop (tipo_pet, nome_pet, idade)
          VALUES ('{pet_type}', '{pet_name}', {pet_age})"""

        inst_register.execute(register)
        conn.commit()

    except:
        print(f'\n🚫    Erro na transação do DB')
    
    else:
        print(f'\n✅    Dados gravados com sucesso')


def list_all_data_in_the_database() -> list:
    inst_consultation.execute(" SELECT * FROM petshop")
    
    data = inst_consultation.fetchall()
    return data