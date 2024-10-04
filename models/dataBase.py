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

    list_data = inst_consultation.fetchall()
    return list_data


def change_records_in_the_database(pet_id: int) -> None:
    error = False

    try:
        register = f""" SELECT * FROM petshop WHERE id = {pet_id}"""
        inst_consultation.execute(register)
        list_data = inst_consultation.fetchall()

        if len(list_data) == 0:
            print(f'\nNão há um pet cadastrado com o ID = {pet_id}')

        else:
            try:
                new_pet_type = input('\nDigite um novo tipo: ')
                new_pet_name = input('Digite um novo nome: ')
                new_pet_age = int(input('Digite uma nova idade: '))

            except ValueError:
                while True:
                    new_pet_age = input('\nDigite uma nova idade válida: ')

                    if new_pet_age.isdigit():
                        new_pet_age = int(new_pet_age)
                        break

                    else:
                        print('\n🚫  Por favor, insira apenas dígitos.')

            change = f"""UPDATE petshop SET
                tipo_pet='{new_pet_type}',
                nome_pet='{new_pet_name}',
                idade={new_pet_age}
                WHERE id = {pet_id}
                """
            inst_change.execute(change)
            conn.commit()

    except:
        print(f'\n🚫  Erro na transação do DB, dados NÃO atualizados')
        error = True

    finally:
        if len(list_data) > 0 and error == False:
            print(f'\n✅  Dados atualizados com sucesso')


def delete_record_from_database(pet_id: int) -> None:
    error = False

    try:
        register = f""" SELECT * FROM petshop WHERE id = {pet_id}"""
        inst_consultation.execute(register)
        list_data = inst_consultation.fetchall()

        if len(list_data) == 0:
            print(f'\nNão há um pet cadastrado com o ID = {pet_id}')

        else:
            delete_register = f"""DELETE FROM petshop WHERE id = {pet_id}"""
            inst_exclusion.execute(delete_register)
            conn.commit()

    except:
        print(f'\n🚫  Erro na transação do DB, dados NÃO excluídos')
        error = True

    finally:
        if len(list_data) > 0 and error == False:
            print(f'\n✅  Dados deletados com sucesso')


def delete_all_records_from_the_database() -> None:
    delete_all_registers = f"""DELETE FROM petshop"""
    inst_exclusion.execute(delete_all_registers)
    conn.commit()

    data_reset_ids = f"""ALTER TABLE petshop MODIFY(ID GENERATED AS IDENTITY (START WITH 1))"""
    inst_exclusion.execute(data_reset_ids)
    conn.commit()

    print(f'\n✅   Todos os registros foram excluídos')
