import os

restaurants = ['Bolos da Ju' , 'Pizzaria do João', 'Restaurante dona Maria',]

def display_the_program_name():
    print(""" 
    ██████╗  ██████╗ ███╗   ███╗     ██████╗  ██████╗ ███████╗████████╗ ██████╗     
    ██╔══██╗██╔═══██╗████╗ ████║    ██╔════╝ ██╔═══██╗██╔════╝╚══██╔══╝██╔═══██╗    
    ██████╔╝██║   ██║██╔████╔██║    ██║  ███╗██║   ██║███████╗   ██║   ██║   ██║    
    ██╔══██╗██║   ██║██║╚██╔╝██║    ██║   ██║██║   ██║╚════██║   ██║   ██║   ██║    
    ██████╔╝╚██████╔╝██║ ╚═╝ ██║    ╚██████╔╝╚██████╔╝███████║   ██║   ╚██████╔╝    
    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝     ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝     
    """)

def display_options():
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')

def finish_app():
    clear_console()
    print('Finalizando o app\n')

def invalid_option():
    print('\nOpção inválida!!\n')
    return_to_menu()

def register_new_restaurant():
    clear_console()
    print('Cadastrar restaurantes\n')
    nome_dos_restaurantes = input('Digite o nome dos restaurantes: ')
    restaurants.append(nome_dos_restaurantes)
    print(f'\nRestaurante cadastrado ({nome_dos_restaurantes})')
    return_to_menu()

def list_all_the_restaurants():
    clear_console()
    print('listando todos os restaurantes\n')
    for restaraunt in restaurants:
        print(f".{restaraunt.capitalize()}\n")
    return_to_menu()

def choose_option():
    selected_option = input('\nEscolha uma opção: ')
    if selected_option == '1':
        register_new_restaurant()
    elif selected_option == '2':
        list_all_the_restaurants()
    elif selected_option == '3':
        print('\nAtivar restaurante')
    elif selected_option == '4':
        finish_app()
        return
    else:
        invalid_option()

def return_to_menu():
    input('\nclique enter para voltar ao menu ')
    main()

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    clear_console()
    display_the_program_name()
    display_options()
    choose_option()

if __name__ == '__main__':
    main()
