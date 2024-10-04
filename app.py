import sys
from typing import Callable
from models.dataBase import database_connection
from models.validations import validate_option_digit, return_menu
from models.system import clean_screen
from models.menu_functions import register_pet, list_pets, change_pets, delete_pet, delete_all_records


def clean_and_return(option: Callable) -> None:
    clean_screen()
    option()
    return_menu()


def menu() -> None:
    print('---- CRUD - PETSHOP ----\n')

    menu_options = (
        '1 - Cadastrar Pet',
        '2 - Listar Pets',
        '3 - Alterar Pet',
        '4 - Excluir Pet',
        '5 - EXCLUIR TODOS OS REGISTROS',
        '6 - Sair',
    )

    for option in menu_options:
        print(option)


def menu_options() -> None:
    while True:
        menu()
        option = validate_option_digit()

        match option:
            case 1:
                clean_and_return(register_pet)
            case 2:
                clean_and_return(list_pets)
            case 3:
                clean_and_return(change_pets)
            case 4:
                clean_and_return(delete_pet)
            case 5:
                clean_and_return(delete_all_records)
            case 6:
                clean_screen()
                print('📲  OBRIGADO POR USAR O APP CRUD - PETSHOP\n')
                sys.exit()
            case _:
                print('\n🚫  Opção inválida, tente novamente.')


def main():
    connection_database = database_connection()

    if connection_database:
        menu_options()
    else:
        input('    Verifique a conexão com o banco de dados e tente novamente.')
        clean_screen()
        sys.exit()


if __name__ == "__main__":
    main()
