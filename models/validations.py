from models.system import clean_screen

def validate_option_digit() -> int:
    try:
        option = int(input(f'\nEscolha -> '))
    except:
        while True:
            option = input('\n⚠️   Digite uma opção válida: ')

            if option.isdigit():
                option = int(option)
                break
            else:
                print('\n🚫  Por favor, insira apenas dígitos.')

    return option

def return_menu():
    input('\n⚠️   Digite qualquer tecla para retornar ao menu')
    clean_screen()