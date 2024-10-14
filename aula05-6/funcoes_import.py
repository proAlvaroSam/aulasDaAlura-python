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
    print('1.Cadastrar restaurantes')
    print('2.Listar restaurante')
    print('3.Ativar restaurante')
    print('4.Sair')

def finish_app():
    #os.system('cls') usado apenas no corno do windows
    os.system('clear')
    print('finalizando o app\n')

def choose_option():
    selected_option = input('\nescolha uma opção : ')
    
    if selected_option == '1':
        print('\ncadastrar restaurantes')
    elif selected_option == '2':
        print('\nlistar restaurante')
    elif selected_option == '3':
        print('\nativar restaurante')
    elif selected_option == '4':
        finish_app()
    else :
        print('\nOpção inválida!!')

def main():
    display_the_program_name()
    display_options()
    choose_option()
    

if __name__ == '__main__':
    main()