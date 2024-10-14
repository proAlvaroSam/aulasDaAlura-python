import os

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
    # os.system('cls') usado apenas no Windows
    os.system('clear')
    print('Finalizando o app\n')

def invalid_option():
    os.system('clear')
    print('\nOpção inválida!!\n')
    input('Digite qualquer tecla para continuar: ')
    main()
    print('\nEscolha novamente\n')

def choose_option():
    selected_option = input('\nEscolha uma opção: ')
    if selected_option == 1:
        print('\nCadastrar restaurantes')
    elif selected_option == 2:
        print('\nListar restaurante')
    elif selected_option == 3:
        print('\nAtivar restaurante')
    elif selected_option == 4:
        finish_app()
        return
    else:
        invalid_option()

def main():
    os.system('clear')
    display_the_program_name()
    display_options()
    choose_option()

if __name__ == '__main__':
    main()
