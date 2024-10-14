print("""██████╗  ██████╗ ███╗   ███╗     ██████╗  ██████╗ ███████╗████████╗ ██████╗ 
██╔══██╗██╔═══██╗████╗ ████║    ██╔════╝ ██╔═══██╗██╔════╝╚══██╔══╝██╔═══██╗
██████╔╝██║   ██║██╔████╔██║    ██║  ███╗██║   ██║███████╗   ██║   ██║   ██║
██╔══██╗██║   ██║██║╚██╔╝██║    ██║   ██║██║   ██║╚════██║   ██║   ██║   ██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║    ╚██████╔╝╚██████╔╝███████║   ██║   ╚██████╔╝
╚═════╝  ╚═════╝ ╚═╝     ╚═╝     ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ 

""")

print('1.Cadastrar restaurantes')
print('2.Listar restaurante')
print('3.Ativar restaurante')
print('4.Sair')

selected_option = input('\nescolha uma opção : ')

if selected_option == '1':
    print('\ncadastrar restaurantes')
elif selected_option == '2':
    print('\nlistar restaurante')
elif selected_option == '3':
    print('\nativar restaurante')
elif selected_option == '4':
    print('\nsair do programa')
else :
    print('\nOpção inválida')