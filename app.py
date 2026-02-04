import os

#restaurantes adicionados na lista 
restaurantes = [{'nome': 'Sasa´s burguer', 'categoria':'Lanches', 'ativo':False}, 
                {'nome': 'Pizza supreme', 'categoria':'Italiana', 'ativo':True}, 
                {'nome': 'Restaurante da vovó', 'categoria':'Comida caseira', 'ativo':True}]

#o def ele é uma função 
def exibir_nome_do_programa():
    print('𝚂𝚊𝚋𝚘𝚛 𝚎𝚡𝚙𝚛𝚎𝚜𝚜\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes cadastrados')
    print('3. Alternar estado do restaurante')
    print('4. Sair do app\n')

def Finalizar_app():
     exibir_subtitulo('Finalizando o app\n')

def exibir_subtitulo(texto):   #ele permite sempre mudar o subtitulo de acordo com o que estiver fazendo no menu
    os.system('cls')  #limpa o terminal 
    linha = '*' *(len(texto)) #ele cria uma linha para o texto acima
    print(linha) #linha encima
    print(texto)  #texto
    print(linha) #linha embaixo
    print()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção Invalida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False} #dicionario que passa as informações
    restaurantes.append(dados_do_restaurante)  #inclui o restaurante digitado pelo usuario na lista criada la em cima
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes')
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    
    #PARA cada restaurante na lista eu listo os restaurantes
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'  #Ternario
        print(f' • {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()
    #e se não tiver nenhum restaurante cadastrado, fazer função?

    #ativar e desativar restaurante
def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    #para cada restaurante na lista restaurantes
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'  #aqui foi usado ternário
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()



def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) #o int ali força que seja digitado um numero inteiro 
    
        if opcao_escolhida ==   1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
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
