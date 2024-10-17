import os

restaurants = [
    {'nome': 'Bolos da Ju', 'ativo': True},
    {'nome': 'Pizzaria do João', 'ativo': False},
    {'nome': 'Restaurante dona Maria', 'ativo': True}
]

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
    print('2. Listar restaurantes')
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
    print("""****************************
Registrar novos Restaurantes
****************************""")
    restaurant_name = input('Registre um novo restaurante: ')
    new_restaurant = {'nome': restaurant_name, 'ativo': False}
    restaurants.append(new_restaurant)
    print(f'\nRestaurante ({restaurant_name}) foi registrado')
    return_to_menu()

def list_all_the_restaurants():
    clear_console()
    print('listando todos os restaurantes\n')
    for restaurant in restaurants:
        status = 'Ativo' if restaurant['ativo'] else 'Inativo'
        print(f". {restaurant['nome'].capitalize()} | {status}")
    return_to_menu()

def toggle_restaurant_activity():
    clear_console()
    print('Alternando estado do restaurante')
    name_to_restaurant = input('Digite o nome do restaurante: ')
    restaurant_found = False
    for restaurant in restaurants:
        if name_to_restaurant == restaurant['nome']:
            restaurant_found = True
            restaurant['ativo'] = not restaurant['ativo']
            message = f'O restaurante {name_to_restaurant} foi {"ativado" if restaurant["ativo"] else "desativado"} com sucesso'
            print(message)
    if not restaurant_found:
        print('O restaurante não foi encontrado')
    return_to_menu()

def choose_option():
    selected_option = input('\nEscolha uma opção: ')
    if selected_option == '1':
        register_new_restaurant()
    elif selected_option == '2':
        list_all_the_restaurants()
    elif selected_option == '3':
        toggle_restaurant_activity()
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