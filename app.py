

import os

restaurantes = [
                {'nome':'Pizza Supreme', 'categoria':'Pizaria', 'ativo':True}, 
                {'nome':'Kyoto', 'categoria': 'Japonesa','ativo': False}, 
                {'nome':'Pasta Taste', 'categoria': 'Italiana','ativo': False} ]

def exibir_nome_do_programa():
    '''A função é responsável por exibir o nome do programa'''
    print("""
▒█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ▒█▀▀▀ █░█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
░▀▀▀▄▄ █▄▄█ █▀▀▄ █░░█ █▄▄▀ 　 ▒█▀▀▀ ▄▀▄ █░░█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
▒█▄▄▄█ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ▒█▄▄▄ ▀░▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀▀▀
      """)
    
def exibir_opcoes():
    '''A função montra a lista de opções do menu principal'''
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurante')
    print('3 - Ativar/desativar restaurante')
    print('4 - Sair \n')


def finalizar_app():
    '''A função limpa o terminal e mostra a mensagem "encerrando o app"'''
    exibir_subtitulos('Encerrando o app')


def voltar_ao_menu_principal():
    '''A função é responsável por voltar ao menu principal quando o usuário aperta enter'''
    input('\nPressione ENTER para voltar ao menu principal ')
    main()


def opcao_invalida():
    ''' A função indica ao usuário que a opção que ele digitou é inválida e retorna ao menu principal'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulos(texto):
    '''A função limpa o terminal e exibe o texto que for digitado referente a opção escolhida pelo usuário'''
    os.system('cls')
    linha = '_' * (len(texto) + 4)
    print(linha)
    print()
    print(texto)
    print(linha)
    print()


def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulos('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

    
def listar_restaurantes():
    '''Função responsável pela lista de restaurantes'''
    exibir_subtitulos('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}' )
    
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''Função responsável pelo estado do restaurante
    Inputs:
    - Nome do restaurante

    Outputs:
    - Diz se o restaurante foi encontrado ou não e alterna seu estado atual
    '''

    exibir_subtitulos('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Função responsável pela escolha das opções'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função reponsável pelo menu principal'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
