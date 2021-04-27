import funcoes
import time
import platform
import os  # Módulos/funções importadas.


sistema = platform.system()  # Retorna o sitema operacional embaracado na máquina.
if (sistema == 'Windows'):
    limpar = 'cls'  # Comando para limpar a tela no Windows.
else:
    limpar = 'clear'  # Comando para limpar a tela no Linux, Mac OS, etc.
while True:
    tela = (funcoes.tela_inicial())  # Atribui a tela inicial como tela a ser printada.
    os.system(limpar)  # Limpa a tela.
    print(tela, end='')  # Printa a tela inicial.
    opcoes = ['1', '2', '3', '4', '5']  # Possíveis opções entrada.
    opcao = input('''\n###################    Escolha uma opção e tecle "ENTER"    ####################
''')  # Lê a opção desejada.
    opcao = opcao.strip()  # Remove espaços vazios antes e depois do texto.
    opcao = opcao.lower()  # Converte toda string em letra minúscula.
    os.system(limpar)  # Limpa tela.
    opcao = (funcoes.entrada(opcao, opcoes, tela, limpar))  # Função chamada caso o valor digitado como opção não seja válido.
    if (opcao == '1'):
        modo = 'TRADICIONAL'  # Executa como  modo tradicional.
        tela = (funcoes.niveis(opcao, modo))  # Atribui a tela inicial como tela a ser printada.
        os.system(limpar)  # Limpa tela.
        print(tela, end='')  # Printa a tela de escolha de níveis.
        opcoes = ['1', '2', '3']  # Possíveis opções de entrada.
        opcao = input('''\n###################    Escolha uma opção e tecle "ENTER"    ####################
''')  # Lê a opção desejada.
        opcao = opcao.strip()  # Remove espaços vazios antes e depois do texto.
        opcao = opcao.lower()  # Converte toda string em letra minúscula.
        os.system(limpar)  # Limpa tela.
        opcao = (funcoes.entrada(opcao, opcoes, tela, limpar))  # Função chamada caso o valor digitado como opção não seja válido.
        funcoes.modo_tradicional(opcao, limpar)  # Função do modo tradicional.
    elif (opcao == '2'):
        modo = 'QUIZ'  # Executa como  modo quiz.
        tela = (funcoes.niveis(opcao, modo))  # Atribui a tela inicial como tela a ser printada.
        os.system(limpar)  # Limpa tela.
        print(tela, end='')  # Printa a tela de escolha de níveis.
        opcoes = ['1', '2', '3']  # Possíveis opções de entrada.
        opcao = input('''\n###################    Escolha uma opção e tecle "ENTER"    ####################
''')  # Lê a opção desejada.
        opcao = opcao.strip()  # Remove espaços vazios antes e depois do texto.
        opcao = opcao.lower()  # Converte toda string em letra minúscula.
        os.system(limpar)  # Limpa tela.
        opcao = (funcoes.entrada(opcao, opcoes, tela, limpar))  # Função chamada caso o valor digitado como opção não seja válido.
        funcoes.modo_quiz(opcao, limpar)  # Função do modo quiz.
    elif (opcao == '3'):
        os.system(limpar)  # Limpa tela.
        print(funcoes.como_jogar())  # Printa tela de instruções.
        prox = input()  # Aguarda algo ser digitado para mudar de tela.
        os.system(limpar)  # Limpa tela.
    elif opcao == '4':
        os.system(limpar)  # Limpa tela.
        print(funcoes.tela_de_creditos())  # Printa tela de créditos.
        prox = input()  # Aguarda algo ser digitado para mudar de tela.
        os.system(limpar)  # Limpa tela.
    elif opcao == '5':
        break  # Encerra a estrutura de repetição.
os.system(limpar)  # Limpa tela.
print(funcoes.encerrar(limpar))  # Função para encerrar o programa e fechar janela.
