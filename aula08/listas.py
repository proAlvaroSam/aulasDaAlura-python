import os

restaurant = []

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
    input('Digite qualquer tecla para continuar: ')
    main()

def register_new_restaurant():
    clear_console()
    print('Cadastrar restaurantes\n')
    nome_dos_restaurantes = input('Digite o nome dos restaurantes: ')
    restaurant.append(nome_dos_restaurantes)
    print(f'\nRestaurante cadastrado ({nome_dos_restaurantes})')
    input('\nclique enter para sair ')
    main()

def choose_option():
    selected_option = input('\nEscolha uma opção: ')
    if selected_option == '1':
        register_new_restaurant()
    elif selected_option == '2':
        print('\nListar restaurante')
    elif selected_option == '3':
        print('\nAtivar restaurante')
    elif selected_option == '4':
        finish_app()
        return
    else:
        invalid_option()

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    limpar_console()
    display_the_program_name()
    display_options()
    choose_option()

if __name__ == '__main__':
    main()
