import os

#restaurantes adicionados na lista 
restaurantes = [{'nome': 'Sasa´s burguer', 'categoria':'Lanches', 'ativo':False}, 
                {'nome': 'Pizza supreme', 'categoria':'Italiana', 'ativo':True}, 
                {'nome': 'Restaurante da vovó', 'categoria':'Comida caseira', 'ativo':True}]

#o def ele é uma função 
def exibir_nome_do_programa():
    '''Nesta função é exibido o nome do programa assim que abre o app'''
    print('𝚂𝚊𝚋𝚘𝚛 𝚎𝚡𝚙𝚛𝚎𝚜𝚜\n')

def exibir_opcoes():
    '''Essa função exibe as opções disponiveis do app'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes cadastrados')
    print('3. Alternar estado do restaurante')
    print('4. Sair do app\n')

def Finalizar_app():
    '''Essa função finaliza o app '''
    exibir_subtitulo('Finalizando o app\n')

def exibir_subtitulo(texto):  
    ''' Essa função  exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')  #limpa o terminal 
    linha = '*' *(len(texto)) #ele cria uma linha para o texto acima
    print(linha) #linha encima
    print(texto)  #texto
    print(linha) #linha embaixo
    print()

def voltar_ao_menu_principal():
    '''solicita uma tecla para voltar ao menu principal
    Outputs:
    - retorna ao menu principal  
    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    ''' Essa função mostra a mensagem 'opção invalida' e volta para o menu principal onde estão as perguntas'''
    print('Opção Invalida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função cadastra um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria
    
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False} #dicionario que passa as informações
    restaurantes.append(dados_do_restaurante)  #inclui o restaurante digitado pelo usuario na lista criada la em cima
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''
    Essa função permite listar os restaurantes que foram cadastrados
    o ijust é usado para definir o espaçamento
    output
    - mostra o nome do restaurante, a categoria e se ele esta ativo ou não
    '''
    exibir_subtitulo('Listando Restaurantes')
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")  #ljust Completa com espaços até atingir um tamanho fixo.
    
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
    '''
    essa função permite ativar ou desativar um restaurante
    
    input
    - se o restaurante digitado pelo usuario existir

    uotput 
    - ele desativa\ativa o resturante 
    '''
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
    '''essa função permite que o usuario escolha uma opção para manipular
    Input
    -numero inteiro

    output
    - Opção escolhida pelo usuario 
    '''
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
    '''Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
 
 #Se NÃO definir o if __name__ == '__main__':  Nada dentro de def roda sozinho
if __name__ == '__main__':
   main()