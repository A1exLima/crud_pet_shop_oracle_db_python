from models.dataBase import register_data_in_the_database, list_all_data_in_the_database
import pandas

def register_pet() -> None:
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
        print(f'🚫    Não há Pets cadastrados')
    else:
        print(f'\n{data_dataFrame}')

