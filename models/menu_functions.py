from models.dataBase import register_data_in_the_database, list_all_data_in_the_database, change_records_in_the_database, delete_record_from_database, delete_all_records_from_the_database
import pandas


def register_pet() -> None:
    print(f'---- CADASTRAR PET ----\n')

    try:
        pet_type = input('Digite o tipo: ')
        pet_name = input('Digite o nome: ')
        pet_age = int(input('Digite a idade: '))

    except ValueError:
        while True:
            pet_age = input('\nDigite uma idade válida: ')

            if pet_age.isdigit():
                pet_age = int(pet_age)
                break

            else:
                print('\n🚫  Por favor, insira apenas dígitos.')

    finally:
        register_data_in_the_database(pet_type, pet_name, pet_age)


def list_pets() -> None:
    print('---- LISTAR PETS ----')

    list_data = list_all_data_in_the_database()
    list_data = sorted(list_data)

    data_dataFrame = pandas.DataFrame.from_records(
        list_data,
        columns=[
            'Id',
            'Raça',
            'Nome',
            'Idade'
        ],
        index='Id'
    )

    if data_dataFrame.empty:
        print(f'\n🚫  Não há Pets cadastrados')
    else:
        print(f'\n{data_dataFrame}')


def change_pets() -> None:
    print(f'---- ALTERAR PET ----')

    try:
        pet_id = int(input('\nDigite um ID do Pet: '))

    except ValueError:
        while True:
            pet_id = input('\nDigite um ID válido: ')

            if pet_id.isdigit():
                pet_id = int(pet_id)
                break

            else:
                print('\n🚫  Por favor, insira apenas dígitos.')

    finally:
        change_records_in_the_database(pet_id)


def delete_pet() -> None:
    print(f'---- EXCLUIR PET ----')

    try:
        pet_id = int(input('\nDigite um ID do Pet: '))

    except ValueError:
        while True:
            pet_id = input('\nDigite um ID válido: ')

            if pet_id.isdigit():
                pet_id = int(pet_id)
                break

            else:
                print('\n🚫  Por favor, insira apenas dígitos.')

    finally:
        delete_record_from_database(pet_id)


def delete_all_records() -> None:
    print(f'---- EXCLUIR TODOS OS REGISTROS ----')

    try:
        confirm_deletion = input(
            f'\n⚠️   CONFIRMA A EXCLUSÃO DE TODOS OS PETS, [S]im ou [N]ão: ')

        confirm_deletion = confirm_deletion.upper()

        if confirm_deletion != 'S' and confirm_deletion != 'N':
            while True:
                confirm_deletion = input(
                    '\nDigite [S] para SIM e [N] para Não: ')

                confirm_deletion = confirm_deletion.upper()

                if confirm_deletion == 'S' or confirm_deletion == 'N':
                    break

                else:
                    print('\n🚫  Opção inválida, tente novamente')

    finally:
        if confirm_deletion == 'S':
            delete_all_records_from_the_database()
        else:
          print(f'\n➡️   Operação cancelada pelo usuário')