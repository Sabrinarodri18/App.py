import os

restaurantes = []
#o def ele é uma função 
def exibir_nome_do_programa():
    print('𝚂𝚊𝚋𝚘𝚛 𝚎𝚡𝚙𝚛𝚎𝚜𝚜\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes cadastrados')
    print('3. Ativar restaurante')
    print('4. Sair do app\n')

def Finalizar_app():
     exibir_subtitulo('Finalizando o app\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):   #ele permite sempre mudar o subtitulo de acordo com o que estiver fazendo no menu
    os.system('cls')  #limpa o terminal 
    print(texto)
    print()

def opcao_invalida():
    print('Opção Invalida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)  #inclui o restaurante digitado pelo usuario na lista criada la em cima
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes\n')
    #PARA cada restaurante na lista eu listo os restaurantes
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    voltar_ao_menu_principal()
    #e se não tiver nenhum restaurante cadastrado, fazer função?

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) #o int ali força que seja digitado um numero inteiro 
    
        if opcao_escolhida ==   1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            Finalizar_app()
        else:
            opcao_invalida()
    except:
            opcao_invalida()
        

#main organiza a ordem do programa
def main():   
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
 
 #Se NÃO definir o if __name__ == '__main__':  Nada dentro de def roda sozinho
if __name__ == '__main__':
   main()
