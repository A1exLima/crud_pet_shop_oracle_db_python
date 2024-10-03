import os
from dotenv import load_dotenv

import oracledb
import pandas as pd

from models.validations import validate_option_digit, return_menu
from models.system import clean_screen


def menu():
    print('---- CRUD - PETSHOP ----\n')

    menu_options = (
        '1 - Cadastrar Pet',
        '2 - Listar Pets',
        '3 - Alterar Pets',
        '4 - Excluir Pets',
        '5 - EXCLUIR TODOS OS REGISTROS',
        '6 - Sair',
    )

    for option in menu_options:
        print(option)


def menu_options():
    while True:
        menu()
        option = validate_option_digit()

        match option:
            case 1:
                clean_screen()
                print('Opção 1 selecionada')
                return_menu()
            case 2:
                clean_screen()
                print('Opção 2 selecionada')
                return_menu()
            case 3:
                clean_screen()
                print('Opção 3 selecionada')
                return_menu()
            case 4:
                clean_screen()
                print('Opção 4 selecionada')
                return_menu()
            case 5:
                clean_screen()
                print('Opção 5 selecionada')
                return_menu()
            case 6:
                clean_screen()
                print('📲  OBRIGADO POR USAR O APP CRUD - PETSHOP\n')
                break
            case _:
                print('\n🚫  Opção inválida, tente novamente.')


def database_connection() -> bool:
    load_dotenv()
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')

    try:
        conn = oracledb.connect(
            user=user,
            password=password,
            dsn='oracle.fiap.com.br:1521/ORCL'
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


def main():
    connection_status = database_connection()
    menu_options()


if __name__ == "__main__":
    main()
