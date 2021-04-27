import time
import random
import os
import sys  # Módulos/funções importadas.


def tela_inicial():  # Função da tela inicial.
    # Cria um arquivo.txt vazio e permite a escita nele.
    telainicial = open('tela_inicial.txt', 'w')
    telainicial.write('''################################################################################
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#*************************     JOGO DO LABIRINTO     **************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#*********************    1 - Jogar no MODO TRADICIONAL    ********************#
#**********************                                   *********************#
#***********************    2 - Jogar no MODO QUIZ       **********************#
#************************                               ***********************#
#*************************    3 - Como Jogar           ************************#
#**************************                           *************************#
#***************************    4 - Créditos         **************************#
#****************************                       ***************************#
#*****************************    5 - Sair         ****************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#''')  # Escreve este conteúdo no arquivo.txt.
    telainicial = open(
        'tela_inicial.txt', 'r')  # Permite que se faça a leitura do conteúdo do arquivo.txt.
    # Lê todas as linhas do arquivo em uma lista.
    telainicial = telainicial.readlines()
    # Junta cada elemento da lista transformando-a em string.
    telainicial = ''.join(telainicial)
    return(telainicial)  # Retorna a tela inicial.


def niveis(opcao, modo):  # Função da tela de seleção de níveis.
    if opcao == '1':
        espaco1 = ''  # Para centralizar (apenas estética).
        espaco2 = ''  # Para centralizar (apenas estética).
    elif opcao == '2':
        espaco1 = '   '  # Para centralizar (apenas estética).
        espaco2 = '    '  # Para centralizar (apenas estética).
    # Apaga conteúdo do arquivo.txt já existente e permite a escita nele.
    telainicial = open('tela_niveis.txt', 'w')
    telainicial.write('''################################################################################
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#*************************     JOGO DO LABIRINTO     **************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#*************    {}Ok, você escolheu jogar no MODO {}{}    **************#
#*************          Escolha o nível de dificuldade:          **************#
#******************************                 *******************************#
#******************************   1 - FÁCIL     *******************************#
#******************************                 *******************************#
#******************************   2 - MÉDIO     *******************************#
#******************************                 *******************************#
#******************************   3 - DIFÍCIL   *******************************#
#******************************                 *******************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#
#******************************************************************************#'''.format(espaco1, modo, espaco2))  # Escreve este conteúdo no arquivo.txt.
    telainicial = open(
        'tela_niveis.txt', 'r')  # Permite que se faça a leitura do conteúdo do arquivo.txt.
    # Lê todas as linhas do arquivo em uma lista.
    telainicial = telainicial.readlines()
    # Junta cada elemento da lista transformando-a em string.
    telainicial = ''.join(telainicial)
    return(telainicial)  # Retorna tela de selção de níveis.


def como_jogar():  # Função da tela de instruções.
    return('''################################################################################
#                                                                              #
#                                                                              #
#                                 COMO JOGAR:                                  #
#                                                                              #
#                                                                              #
#       MODO TRADICIONAL:                                                      #
#       |    |                                                                 #
#       |    Você poderá escolher um, dos três níveis de dificuldade do        #
#       |    jogo com diferentes labirintos, sendo eles: FÁCIL, MÉDIO e        #
#       |    DIFÍCIL. E utilisando as teclas "W", "A", "S" e "D" do seu        #
#       |    teclado você poderá mover-se livremente pelo labirinto até        #
#       |    encontar a respectiva saída do labirinto escolhido.               #
#       |    |                                                                 #
#       MODO QUIZ:                                                             #
#       |    |                                                                 #
#       |    Você poderá escolher um, dos três níveis de dificuldade do        #
#       |    jogo com diferentes labirintos, sendo eles: FÁCIL, MÉDIO e        #
#       |    DIFÍCIL. Para avançar no labirinto em direção a saída pelo        #
#       |    caminho correto, deverá responder corretamente a perguntas        #
#       |    de múltipla escolha, em caso de erro voltará pra a posição        #
#       |    anterior.                                                         #
#       PRESSIONE "ENTER" PARA VOLTAR AO MENU                                  #
#                                                                              #
#                                                                              #
################################################################################''')  # Retorna a tela de instruções.


def tela_de_creditos():  # Função da tela de créditos.
    # Cria um arquivo.txt vazio e permite a escita nele.
    telacreditos = open('tela_de_creditos.txt', 'w')
    telacreditos.write('''################################################################################
#                                                                              #
#                                                                              #
#                                   CRÉDITOS                                   #
#                                                                              #
#                                                                              #
#           Jogo desenvolvido durante o 1º período do curso Técnico            #
#                 em Informática (2018) pela equipe JLM GAMES                  #
#                                                                              #
#                                                                              #
#                             Grupo composto por:                              #
#                                                                              #
#                                                                              #
#                          JÔNATAS TAVARES D0S SANTOS                          #
#                            LUCAS SILVA NASCIMENTO                            #
#                       MARIA GABRIELA PEREIRA DA SILVA                        #
#                                                                              #
#                                                                              #
#                                Orientado por:                                #
#                                                                              #
#                                                                              #
#                       ELAINE CRISTINA JUVINO DE ARAÚJO                       #
#                 MARCOS VINÍCIUS CANTIDIANO MARQUES DE ANDRADE                #
#                                                                              #
#                                                                              #
################################################################################''')  # Escreve este conteúdo no arquivo.txt
    telacreditos = open('tela_de_creditos.txt',
                        'r')  # Permite que se faça a leitura do conteúdo do arquivo.txt.
    # Lê todas as linhas do arquivo em uma lista.
    telacreditos = telacreditos.readlines()
    # Junta cada elemento da lista transformando-a em string.
    telacreditos = ''.join(telacreditos)
    return(telacreditos)  # Retorna a tela de créditos


def encerrar(limpar):  # Procedimento para encerrar o programa.
    os.system(limpar)  # Limpa a tela.
    print(tela_de_creditos())  # Printa a tela de créditos.
    time.sleep(5)  # Aguarda 5 segundos para prosseguir.
    # Recebe a função tela de créditos como parâmentro.
    telacreditos = tela_de_creditos()
    # Tranforma cada caracatere de "telacreditos" em uma elemento de uma lista.
    telacreditos = list(telacreditos)
    x = 0  # Atribui um valor inicial a x.
    # Loop pela quantidade de linhas que existe na tela de crédito.
    for i in range(telacreditos.count('\n')+1):
        os.system(limpar)  # Limpa a tela.
        # Loop pela quantidade de caracteres que existe em uma linha da tela de crédito.
        for i in range(len(telacreditos[:telacreditos.index('\n')])):
            # Substitiu cada um dos caracateres de cada linha por um espaço vazio
            telacreditos[x] = ' '
            x += 1  # Adiciona +1 a x.
        x += 1  # Adiciona mais um a x para poder pular de linha.
        # Printa a tela de créditos (agora com umalinah em branco) juntantos todos os elementos dessa lista.
        print(''.join(telacreditos))
        time.sleep(0.3)  # Aguarda 0.3 segundos para prosseguir.
    sys.exit()  # Encerra o programa e fecha a janela.


# Funçao para o ncadsoo da entrada ser inválida.
def entrada(opcao, opcoes, tela, limpar):
    while ((opcao in opcoes) == False):  # Faz se o teste.
        os.system(limpar)  # Limpa a tela.
        print(tela, end='')  # Printa a referida tela.
        opcao = input('''#############################    Opção inválida    #############################
''')  # LÊ o novo valor.
        opcao = opcao.strip()  # Remove espaços vazios antes e depois do texto.
        opcao = opcao.lower()  # Converte toda string em letra minúscula.
        os.system(limpar)  # Limpa a tela.
    return(opcao)  # Retorna o novo valor da opção.


def labirinto_facil(modo):  # Função dos labirintos fáceis.
    if modo == 'TRADICIONAL':  # Modo tradicional.
        return(['''#                      +---------------+---------------+                       #
#                    . E               |               |                       #
#                      +-----------+   +-----+   +-----+                       #
#                      |               |               |                       #
#                      |   +-------+   +-----------+   |                       #
#                      |           |               |   |                       #
#                      +-----+   +-+---+-------+   +   |                       #
#                      |               |               |                       #
#                      +-----------+   +-------+   +   |                       #
#                      |                       |   |   |                       #
#                      +-----------------------+ S +---+                       #'''])  # Retorna o labirinto em lista no seguinte formato.
    elif modo == 'QUIZ':  # Modo quiz.
        return('''#                      +---------------+---------------+                       #
#                      * ~ ~ ~ ~ ~ ~ . |               |                       #
#                      +-----------+ ~ +-----+   +-----+                       #
#                      |             ~ |               |                       #
#                      |   +-------+ ~ +-----------+   |                       #
#                      |           | . ~ ~ ~ ~ ~ . |   |                       #
#                      +-----+   +-+---+-------+ ~ +   |                       #
#                      |               |         ~     |                       #
#                      +-----------+   +-------+ ~ +   |                       #
#                      |                       | ~ |   |                       #
#                      +-----------------------+ . +---+                       #''')  # Retorna o labirinto em string no seguinte formato.


def labirinto_medio(modo):  # Função dos labirintos medianos.
    if modo == 'TRADICIONAL':  # Modo tradicional.
        return(['''#                    +-----------------+-----------------+                     #
#                  . E                 |                 |                     #
#                    +---+   +---------+   +---------+   |                     #
#                    |       |             |             |                     #
#                    +---+   +---------+   +-+-------+   |                     #
#                    |                       |           |                     #
#                    +-------+   +-----+   +-+-------+   |                     #
#                    |           |           |           |                     #
#                    +---+   +-+-+-----+   +-+   +-------+                     #
#                    |         |                         |                     #
#                    +---------+   +-------------+   +---+                     #
#                    |                                   S                     #
#                    +-----------------------------------+                     #'''])  # Retorna o labirinto em lista no seguinte formato.
    elif modo == 'QUIZ':  # Modo quiz.
        return('''#                    +-----------------+-----------------+                     #
#                    * ~ ~ .           |                 |                     #
#                    +---+ ~ +---------+   +---------+   |                     #
#                    |     ~ |             |             |                     #
#                    +---+ ~ +---------+   +-+-------+   |                     #
#                    |     . ~ ~ ~ ~ ~ ~ .   |           |                     #
#                    +-------+   +-----+ ~ +-+-------+   |                     #
#                    |           |       ~ |             |                     #
#                    +---+   +-+-+-----+ ~ +-+   +-------+                     #
#                    |         |         . ~ ~ ~ ~ .     |                     #
#                    +---------+   +-------------+ ~ +---+                     #
#                    |                             . ~ ~ .                     #
#                    +-----------------------------------+                     #''')  # Retorna o labirinto em string no seguinte formato.


def labirinto_dificil(modo):  # Função dos labirintos difíceis.
    if modo == 'TRADICIONAL':  # Modo tradicional.
        return(['''#                  +-----------+---------------------------+                   #
#                . E           |                           |                   #
#                  +-------+   +-----+   +-----------------+                   #
#                  |           |                           |                   #
#                  |   +---+   +-----+   +---+---------+   |                   #
#                  |                         |             |                   #
#                  +-----------------+-------+   +---------+                   #
#                  |                 |                     |                   #
#                  +---+   +---------+-------+   +-----+   |                   #
#                  |                             |         |                   #
#                  +-----------------+   +-------+---------+                   #
#                  |                                       |                   #
#                  |   +---------+   +---------------------+                   #
#                  |             |                         |                   #
#                  +-------------+-----------------+ S +---+                   #'''])  # Retorna o labirinto em lista no seguinte formato.
    elif modo == 'QUIZ':  # Modo quiz.
        return('''#                  +-------+-------------------------------+                   #
#                  * ~ ~ . |                               |                   #
#                  +---+   +-------+   +-------------------+                   #
#                  |     . ~ ~ ~ ~ ~ . |                   |                   #
#                  |   +-----------+ ~ +---------------+   |                   #
#                  |                 . ~ ~ ~ .             |                   #
#                  +---------------+-------+ ~ +-----------+                   #
#                  |               |        ~              |                   #
#                  +---+   +-------+-----+ ~ +---------+   |                   #
#                  |                       . |             |                   #
#                  +---------------------+ ~ +-------------+                   #
#                  |                       . ~ ~ ~ ~ .     |                   #
#                  |   +---------+   +-------------+ ~ +---+                   #
#                  |                                 . ~ ~ .                   #
#                  +---------------------------------------+                   #''')  # Retorna o labirinto em string no seguinte formato.

# Estrutura das perguntas: As perguntas estão em um dicionário, cada chave, com números a partir de "1", é uma pergunta que tem como valor outro dicionário, este com a
# chave "p" que correspode ao enunciado da pergunta; chave "a", "b", "c" e "d" que correspondem a cada alternativa; e achave "e" que corresponde a alternativa correta.


def perguntas_facil():  # Função das pergutas fáceis.
    return({'1': {'p': 'O menor e maior país do mundo respectivamente são: ', 'a': 'Vaticano e Rússia', 'b': 'Naruru e China', 'c': 'Mônaco e Canadá', 'd': 'São Marinho e Índia', 'e': 'a'},
            '2': {'p': 'Qual o nome do presidente do Brasil que ficou conhecido como Jango? ', 'a': 'Jânio Quadros ', 'b': 'Jacinto Anjos', 'c': 'Getúlio Vargas', 'd': 'João Goulart', 'e': 'd'},
            '3': {'p': 'Quantas casas decimais tem o numero pi? ', 'a': 'Duas', 'b': 'Centenas', 'c': 'Vinte', 'd': 'Trilhares', 'e': 'd'},
            '4': {'p': 'Quanto é 5 elevado ao quadrado? ', 'a': '25', 'b': '10', 'c': '30', 'd': '20', 'e': 'a'},
            '5': {'p': 'Quem foi autor do hino nacional? ', 'a': 'Vila-Lobos', 'b': 'D. Pedro I', 'c': 'D. Pedro II', 'd': 'Olavo Bilac', 'e': 'd'},
            '6': {'p': 'Qual planeta do nosso Sistema Solar é mais próximo do Sol? ', 'a': 'Mercúrio', 'b': 'Marte', 'c': 'Saturno', 'd': 'Terra', 'e': 'a'},
            '7': {'p': 'Nome do navegador português que, conforme a lenda oficial, descobriu o Brasil? ', 'a': 'Vasco da Gama', 'b': 'Pedro Álvares Cabral', 'c': 'Dom João V', 'd': 'Cristóvão Colombo', 'e': 'b'},
            '8': {'p': 'Qual o maior planeta do Sistema Solar? ', 'a': 'Terra', 'b': 'Saturno', 'c': 'Júpiter', 'd': 'Urano', 'e': 'b'},
            '9': {'p': 'Qual é a estrela que fica mais próxima do Planeta Terra? ', 'a': 'A Lua', 'b': 'O Sol', 'c': 'Alfa Centauri', 'd': 'Estrela de Barnard', 'e': 'b'},
            '10': {'p': 'Qual o segundo país da América do Sul? ', 'a': 'Uruguai', 'b': 'Peru', 'c': 'Argentina', 'd': 'Chile', 'e': 'c'},
            '11': {'p': 'Qual o nome de nossa galáxia? ', 'a': 'Via Lácta', 'b': 'Via Láctea', 'c': 'Sol', 'd': 'Sistema Solar', 'e': 'b'}})


def perguntas_medio():  # Função das pergutas medianas.
    return({'1': {'p': 'Qual o ponto mais alto do Brasil? ', 'a': 'Pico da Neblina', 'b': 'Pico Paraná', 'c': 'Monte Roraima ', 'd': 'Pico Bandeira', 'e': 'a'},
            '2': {'p': 'Em qual local da Ásia o português é língua oficial? ', 'a': 'Índia', 'b': 'Filipinas', 'c': 'Macau', 'd': 'Moçambique', 'e': 'c'},
            '3': {'p': 'De quem é a famosa frase "Penso, logo existo"? ', 'a': 'Platão', 'b': 'Galileu Galilei', 'c': 'Descartes', 'd': 'Sócrates', 'e': 'c'},
            '4': {'p': 'Atualmente, quantos elementos químicos possuem na tabela periódica? ', 'a': '113', 'b': '118', 'c': '108', 'd': '109', 'e': 'b'},
            '5': {'p': 'Qual o número mínimo de jogadores em uma partida de futebol? ', 'a': '8', 'b': '7', 'c': '10', 'd': '11', 'e': 'b'},
            '6': {'p': 'Quanto tempo a luz do Sol demora para chegar na Terra? ', 'a': '12 minutos', 'b': '1 dia', 'c': '12 horas', 'd': '8 minutos', 'e': 'd'},
            '7': {'p': 'Qual recurso foi ultilizado inicialmente pelo homem para explicar a origem das coisas? ', 'a': 'A Filosofia', 'b': 'A Ciência', 'c': 'A Mitologia', 'd': 'A Matemática', 'e': 'c'},
            '8': {'p': 'Em que periodo da pré-história o fogo foi descoberto? ', 'a': 'Neolítico', 'b': 'Paleolítico', 'c': 'Idade Média', 'd': 'Idade dos Metais', 'e': 'b'},
            '9': {'p': 'Quem é o autor do famoso discurso "Eu tenho um sonho"? ', 'a': 'Nelson Mandela', 'b': 'Martin Luther King', 'c': 'Zumbi dos Palmares', 'd': 'Barack Obama', 'e': 'b'},
            '10': {'p': 'Qual vitamina absovermos quando entramos em contato com o Sol? ', 'a': 'Vitamina A', 'b': 'Vitamina C', 'c': 'Vitamina D', 'd': 'Vitamina F', 'e': 'c'},
            '11': {'p': 'Quem inventou a luz elétrica? ', 'a': 'Vasco da Gama', 'b': 'Santos Dumont', 'c': 'Thomas Edson', 'd': 'Albert Einstein', 'e': 'c'},
            '12': {'p': 'Qual desses órgãos do corpo humano filtra o nosso sangue? ', 'a': 'Cérebro', 'b': 'Pulmão', 'c': 'Rins', 'd': 'Traqueia', 'e': 'c'},
            '13': {'p': 'Qual o significado da sigla O.N.U? ', 'a': 'Organização Não Universal', 'b': 'Ordens Na Unidade', 'c': 'Organização das Nações Unidas', 'd': 'Organização Não Unidas', 'e': 'c'},
            '14': {'p': 'Qual o nome da famosa torre inclinada na Itália? ', 'a': 'Torre de Babel', 'b': 'Torre de Belini', 'c': 'Torre Eiffel', 'd': 'Torre de Pisa', 'e': 'd'},
            '15': {'p': 'Andromeda, Ursa Maior, Pegasus e Perseus são: ', 'a': 'Cometas', 'b': 'Planetas', 'c': 'Arquipélagos', 'd': 'Constelações', 'e': 'd'},
            '16': {'p': 'É uma das sete maravilhas do mundo moderno: ', 'a': 'Cristo Redentor', 'b': 'Estátua de Shiva', 'c': 'Estátua da Liberdade', 'd': 'Torre Eiffel', 'e': 'a'}})


def perguntas_dificil():  # Função das pergutas difíceis.
    return({'1': {'p': 'Qual a função da ONU? ', 'a': 'Zelar pela cultura em todas as nações', 'b': 'Unir as nações com o objetivo de manter a paz e a segurança mundial', 'c': 'Financiar países em desenvolvimento ', 'd': 'Gerenciar acordos de comércio entre os países', 'e': 'b'},
            '2': {'p': 'Qual doença sexualmente transmissível que virou surto no Brasil em 2017? ', 'a': 'Febre Amarela', 'b': 'Zika', 'c': 'Sífilis', 'd': 'Hepatite B', 'e': 'c'},
            '3': {'p': 'Os países com maior e a menor expectativa de vida do mundo, respectivamente são: ', 'a': 'Japão e Serra Leoa', 'b': 'Austrália e Afeganistão', 'c': 'Itália e Chade', 'd': 'Estados Unidos e Angola', 'e': 'a'},
            '4': {'p': 'Quais as duas datas comemorativas em Novembro no Brasil? ', 'a': 'Independência do Brasil e e Dia da Bandeira', 'b': 'Proclamação da República e Dia Nacional da Consciência Negra', 'c': 'Páscoa', 'd': 'Black Friday e Dia da Árvore', 'e': 'b'},
            '5': {'p': 'Em que ordem surgiram os modelos atômicos? ', 'a': 'Thomson, Dalton, Rutherford, Rutherford-Bohr', 'b': 'Rutherford-Bohr, Rutherford, Thomson, Dalton', 'c': 'Dalton, Thomson, Rutherford, Rutherford-Bohr', 'd': 'Dalton, Rutherford-Bohr, Thomson, Rutherford', 'e': 'c'},
            '6': {'p': 'Qual a velocidade da luz? ', 'a': '299 792 458 metros por segundo (m/s)', 'b': '300 000 000 metros por segundo (m/s)', 'c': '150 000 000 metros por segundo (m/s)', 'd': '30 000 000 metros por segundo (m/s)', 'e': 'a'},
            '7': {'p': '“It is six twenty ou twenty past six”. Que horas são em inglês? ', 'a': '12:06', 'b': '6:20', 'c': '2:20', 'd': '12:20', 'e': 'b'},
            '8': {'p': 'Como é a conjugação do verbo caber na 1ª pessoa do singular do presente do indicativo? ', 'a': 'Eu caibo', 'b': 'Ele cabe', 'c': 'Que eu caiba', 'd': 'Eu cabo', 'e': 'a'},
            '9': {'p': 'Quais destas construções famosas ficam nos Estados Unidos? ', 'a': 'Estátua da Liberdade, Golden Gate Bridge e Empire State Building', 'b': 'Estátua da Liberdade, Big Ben e The High Line', 'c': 'Angkor Wat, Taj Mahal e Skywalk no Grand Canyon', 'd': 'Lincoln Memorial, Sidney Opera House e Burj Khalifa', 'e': 'a'},
            '10': {'p': 'Qual destes países é transcontinental? ', 'a': 'Rússia', 'b': 'Filipinas', 'c': 'Istambul', 'd': 'Groenlândia', 'e':  'a'},
            '11': {'p': 'Em qual das orações abaixo a palavra foi empregada incorretamente? ', 'a': 'Mais uma vez, portou-se mal.', 'b': 'É um homem mal.', 'c': 'Esse é o mal de todos.', 'd': 'Mal falou nele, o fulano apareceu.', 'e': 'b'},
            '12': {'p': 'Quais os planetas do sistema solar? ', 'a': 'Terra, Vênus, Saturno, Urano, Júpiter, Marte, Netuno, Mercúrio', 'b': 'Júpiter, Marte, Mercúrio, Netuno, Plutão, Saturno, Terra, Urano, Vênus', 'c': 'Terra, Vênus, Saturno, Júpiter, Marte, Netuno, Mercúrio', 'd': 'Vênus, Saturno, Urano, Júpiter, Marte, Netuno, Mercúrio', 'e': 'a'},
            '13': {'p': 'Júpiter e Plutão são os correlatos romanos de quais deuses gregos? ', 'a': 'Ares e Hermes', 'b': 'Cronos e Apolo', 'c': 'Zeus e Hades', 'd': 'Zeus e Ares', 'e': 'c'},
            '14': {'p': 'Qual o maior animal terrestre? ', 'a': 'Baleia Azul', 'b': 'Dinossauro', 'c': 'Elefante africano', 'd': 'Girafa', 'e': 'c'},
            '15': {'p': 'De onde é a invenção do chuveiro elétrico? ', 'a': 'França', 'b': 'Itália', 'c': 'Brasil', 'd': 'Inglaterra', 'e': 'c'},
            '16': {'p': 'As pessoas de qual tipo sanguíneo são consideradas doadores universais? ', 'a': 'Tipo A', 'b': 'Tipo B', 'c': 'Tipo O', 'd': 'Tipo AB', 'e': 'c'},
            '17': {'p': 'Qual o nome do cientista que descobriu o processo de pasteurização e a vacina contra a raiva? ', 'a': 'Marie Curie', 'b': 'Louis Pasteurs', 'c': 'Darwin', 'd': 'Antoine Lavoisier', 'e': 'b'},
            '18': {'p': 'Quem foi o primeiro homem a pisar na Lua? Em que ano aconteceu? ', 'a': ' Yuri Gagarin, em 1961', 'b': 'Buzz Aldrin, em 1969', 'c': 'Charles Conrad, em 1969', 'd': 'Neils Armstrong, em 1969', 'e': 'd'},
            '19': {'p': 'Qual desses filmes foi baseado na obra de Shakespeare? ', 'a': 'Muito Barulho por Nada (2012)', 'b': 'Capitães de Areia (2011)', 'c': 'Excalibur (1981)', 'd': 'A Revolução dos Bichos (1954)', 'e': 'a'},
            '20': {'p': 'Quais os nomes dos três Reis Magos? ', 'a': 'Gaspar, Nicolau e Natanael', 'b': 'Belchior, Gaspar e Baltazar', 'c': 'Belchior, Gaspar e Nataniel', 'd': 'Gabriel, Benjamim e Melchior', 'e': 'b'},
            '21': {'p': 'Quem desenvolveu a teoria da relatividade? ', 'a': 'Galileu Galilei', 'b': 'Benjamin Franklin', 'c': 'Isaac Newton', 'd': 'Albert Einsten', 'e': 'd'}})


def modo_tradicional(opcao, limpar):
    if opcao == '1':
        nivel = 'FÁCIL!                        #'
        # Atribui o labirinto de nível fácil a parte principal.
        labirinto = labirinto_facil('TRADICIONAL')
    elif opcao == '2':
        nivel = 'MÉDIO!                        #'
        # Atribui o labirinto de nível médio a parte principal.
        labirinto = labirinto_medio('TRADICIONAL')
    elif opcao == '3':
        nivel = 'DIFÍCIL!                      #'
        # Atribui o labirinto de nível difícil a parte principal.
        labirinto = labirinto_dificil('TRADICIONAL')
    os.system(limpar)  # Limpa a tela.
    print('''################################################################################
#                                                                              #
#                   JOGO DO LABIRINTO - MODO TRADICIONAL                       #
#                                                                              #
#                      Ok, você escolheu o NÍVEL {}
#                                                                              #
################################################################################
#                                                                              #'''.format(nivel))
    for i in range(len(labirinto[0])):
        # Printa caractere por caractere do labirinto
        print(labirinto[0][i].replace('.', ' '), end='')
    print('''
#                                                                              #
#                        Legenda: E - Entrada; S - Saída                       #
#                                                                              #
#########################    Aguarde um instante...   ##########################''')
    time.sleep(3)  # Aguarda 3 segudos para prosseguir.
    os.system(limpar)  # Limpa a tela.
    print('''################################################################################
#                                                                              #
#        Seja bem-vindo ao Jogo do Labirinto!                                  #
#        Siga as instruções para conseguir chegar a saída.                     #
#        Vamos lá!                                                             #
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
#                        Legenda: E - Entrada; S - Saída                       #
#                                                                              #
####################    Pressione "ENTER" para prosseguir    ###################'''.format(labirinto[0].replace('.', ' ')))  # Printa labirinto e instruções.
    prox = input()  # Aguarda algo ser digitado para mudar de tela.
    os.system(limpar)  # Limpa a tela.
    print('''################################################################################
#                                                                              #
#         Você está na entrada do labirinto.                                   #
#         Para mover-se use as teclas "A", "S", "D" e "W" de seu teclado.      #
#         Para voltar à tela inicial pressione "X" a qualquer momento.         #
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
#                        Legenda: E - Entrada; S - Saída                       #
#                                                                              #
####################    Pressione "ENTER" para prosseguir    ###################'''.format(labirinto[0].replace('.', ' ')))  # Printa labirinto e instruções.
    prox = input()  # Aguarda algo ser digitado para mudar de tela.
    os.system(limpar)  # Limpa a tela.
    # Calcula a quantidade de caracteres em uma linha do labirinto.
    tamanho = len(labirinto[0][:labirinto[0].index('\n')])+1
    # Converte o item no índice 0 da lista "labirinto" que é uma string em várias strings, cada caractere se torna um elemento da lista.
    labirinto[0] = list(labirinto[0])
    entrada = labirinto[0].index('E')  # Essa é a entrada do labirinto.
    saida = labirinto[0].index('S')  # Essa é a saída do labirinto.
    # O asterisco (*) foi colocado na entrada do labirinto, substituindo o "E".
    labirinto[0][entrada] = '*'
    # Salva onde está o ponto para evitar que o asterisco saia de dentro do labirinto.
    ponto = labirinto[0].index('.')
    situacao = '''#                                                                              #
#        Aguardando movimento...                                               #'''  # Atribui esse valor a variável para ser printada.
    while (labirinto[0][saida] == 'S'):  # Se o local de saída tiver um "S" significa que o usuário ainda não cegou a saída.
        if (labirinto[0][entrada] == ' '):
            # Se na entrada estiver um espaço em braco será adicionado um "E" apenas poir estética.
            labirinto[0][entrada] = 'E'
        labirinto[0][ponto] = ' '  # O ponto é removido para ser printado
        # Junta cada elemento transformando a lista "labirinto" novamente em string.)
        imprimir = ''.join(labirinto[0])
        # O ponto é colocado de volta para não ter erros.
        labirinto[0][ponto] = '.'
        # "estado" é o índice em "labirinto[0]" da posição atual do usuário (asterisco) no labirinto.
        estado = labirinto[0].index('*')
        os.system(limpar)  # Limpa a tela.
        movimento = input('''################################################################################
#                                                                              #
#                   JOGO DO LABIRINTO - MODO TRADICIONAL                       #
{}
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
#         Movimentos:                                                          #
#         W - Cima | S - Baixo | A - Esquerda | D - Direita | X - Menu         #
##################    Informe o movimento que deseja fazer    ##################
'''.format(situacao, imprimir))  # O usuário informa o movimento que deseja fazer.
        os.system(limpar)  # Limpa a tela.
        situacao = '''#                                                                              #
#        Aguardando movimento...                                               #'''  # Atribui esse valor a variável para ser printada.
        movimento = movimento.strip()  # Remove espaços vazios antes e depois do texto.
        # Converte toda string em letra minúscula.
        movimento = movimento.lower()
        if (movimento == 'w'):
            # Se faz o teste para ver se é possível realizar o movimento.
            if (labirinto[0][estado-tamanho] == '|' or labirinto[0][estado-tamanho] == '-' or labirinto[0][estado-tamanho] == '+' or labirinto[0][estado-tamanho] == '.'):
                situacao = '''#         Não é possível realizar esse movimento.                              #
#         Tente novamente...                                                   #'''  # Atribui esse valor a variável para ser printada.
            else:
                # Remove o asterisco da posição onde estava adicionando um espaço vazio em seu lugar.
                labirinto[0][estado] = ' '
                # O coloca na posição na linha acima.
                labirinto[0][estado-tamanho] = '*'
        elif (movimento == 's'):
            # Se faz o teste para ver se é possível realizar o movimento.
            if (labirinto[0][estado+tamanho] == '|' or labirinto[0][estado+tamanho] == '-' or labirinto[0][estado+tamanho] == '+' or labirinto[0][estado+tamanho] == '.'):
                situacao = '''#         Não é possível realizar esse movimento.                              #
#         Tente novamente...                                                   #'''  # Atribui esse valor a variável para ser printada.
            else:
                # Remove o asterisco da posição onde estava adicionando um espaço vazio em seu lugar.
                labirinto[0][estado] = ' '
                # O coloca na posição na linha abaixo.
                labirinto[0][estado+tamanho] = '*'
        elif (movimento == 'a'):
            # Se faz o teste para ver se é possível realizar o movimento.
            if (labirinto[0][estado-2] == '|' or labirinto[0][estado-2] == '-' or labirinto[0][estado-2] == '+' or labirinto[0][estado-2] == '.'):
                situacao = '''#         Não é possível realizar esse movimento.                              #
#         Tente novamente...                                                   #'''  # Atribui esse valor a variável para ser printada.
            else:
                # Remove o asterisco da posição onde estava adicionando um espaço vazio em seu lugar.
                labirinto[0][estado] = ' '
                # O coloca na "posição atual menos 2" espaços atrás (2 porqure usamos 2 espaços por questões de estética).
                labirinto[0][estado-2] = '*'
        elif (movimento == 'd'):
            # Se faz o teste para ver se é possível realizar o movimento.
            if (labirinto[0][estado+2] == '|' or labirinto[0][estado+2] == '-' or labirinto[0][estado+2] == '+' or labirinto[0][estado+2] == '.'):
                situacao = '''#         Não é possível realizar esse movimento.                              #
#         Tente novamente...                                                   #'''  # Atribui esse valor a variável para ser printada.
            else:
                # Remove o asterisco da posição onde estava adicionando um espaço vazio em seu lugar.
                labirinto[0][estado] = ' '
                # O coloca na "posição atual mais 2" espaços a frente (2 porqure usamos 2 espaços por questões de estética).
                labirinto[0][estado+2] = '*'
        elif (movimento == 'x'):
            fim = '0'  # Apenas para evitar erros.
            # Encerra o loop se for digitado "x", voltando para a tela inicial.
            break
        else:
            situacao = '''#         Código de movimento inexistente/incorreto!                           #
#         Tente novamente usando um dos códigos descritos a baixo.             #'''  # Atribui esse valor a variável para ser printada.
        if (labirinto[0][saida] == '*'):  # Se na posição da saída tiver um asterisco é porque chegou a saída.
            labirinto[0][ponto] = ' '  # O ponto é removido para ser printado.
            # Junta todos os elemetos da lista em uma string.
            imprimir = ''.join(labirinto[0])
            # O ponto é colocado de volta para não ter erros.
            labirinto[0][ponto] = '.'
            os.system(limpar)  # Limpa a tela.
            fim = input('''################################################################################
#                                                                              #
#                   JOGO DO LABIRINTO - MODO TRADICIONAL                       #
#         Parabéns! Você conseguiu chegar a saída.                             #
#         Deseja jogar novamente? [1 - Sim; 2 - Não]                           #
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
#                        Legenda: E - Entrada; S - Saída                       #
#                                                                              #
################################################################################
'''.format(imprimir))  # Ao chegar ao fim pergunat s eo usuário deseja jogar novamente.
            fim = fim.strip()  # Remove espaços vazios antes e depois do texto.
            fim = fim.lower()  # Converte toda string em letra minúscula.
            os.system(limpar)  # Limpa a tela.
            possiveis = ['1', '2', 'x']  # Possíveis valores a serem digitados.
            while ((fim in possiveis) == False):
                os.system(limpar)  # Limpa a tela.
                fim = input('''################################################################################
#                                                                              #
#                     JOGO DO LABIRINTO - MODO TRADICIONAL                     #
#         Opção inválida.                                                      #
#         Deseja jogar novamente? [1 - Sim; 2 - Não]                           #
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
################################################################################
'''.format(imprimir.replace('~', ' ')))  # Lê se novos valores.
                fim = fim.strip()  # Remove espaços vazios antes e depois do texto.
                fim = fim.lower()  # Converte toda string em letra minúscula.
                os.system(limpar)  # Limpa a tela.
    if fim == '2':
        os.system(limpar)  # Limpa a tela.
        print(encerrar(limpar))  # Encerra o jogo.
    else:
        time.sleep(0)  # Não permite que a execução pare.


def modo_quiz(opcao, limpar):
    if opcao == '1':
        # Atribui o labirinto de nível fácil a parte principal.
        labirinto = labirinto_facil('QUIZ')
        # Atribui as perguntas de nível fácil a parte principal.
        perguntas = perguntas_facil()
        nivel = 'FÁCIL!                        #'
    elif opcao == '2':
        # Atribui o labirinto de nível médio a parte principal.
        labirinto = labirinto_medio('QUIZ')
        # Atribui as perguntas de nível médio a parte principal.
        perguntas = perguntas_medio()
        nivel = 'MÉDIO!                        #'
    elif opcao == '3':
        # Atribui o labirinto de nível difícil a parte principal.
        labirinto = labirinto_dificil('QUIZ')
        # Atribui as perguntas de nível difícil a parte principal.
        perguntas = perguntas_dificil()
        nivel = 'DIFÍCIL!                      #'
    # Remove todos os pontos e substitui por um espaço para que se possa imprimir.
    imprimir = labirinto.replace('.', ' ')
    os.system(limpar)  # Limpa a tela.
    print('''################################################################################
#                                                                              #
#                        JOGO DO LABIRINTO - MODO QUIZ                         #
#                                                                              #
#                      Ok, você escolheu o NÍVEL {}
#                                                                              #
################################################################################
#                                                                              #'''.format(nivel))
    for i in range(len(labirinto)):
        # Printa caractere por caractere.
        print(imprimir[i].replace('~', ' '), end='')
    print('''
#                                                                              #
#########################    Aguarde um instante...   ##########################''')
    time.sleep(3)  # Aguarda 3 segundos para prosseguir.
    os.system(limpar)  # Limpa a tela.
    print('''################################################################################
#                                                                              #
#        Seja bem-vindo ao Jogo do Labirinto!                                  #
#        Siga as instruções para chegar a saída.                               #
#        Vamos lá!                                                             #
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
####################    Pressione "ENTER" para prosseguir    ###################'''.format(imprimir.replace('~', ' ')))  # Printa substituindo "~" por " ".
    prox = input()  # Aguarda algo ser digitado para mudar de tela.
    os.system(limpar)  # Limpa a tela.
    print('''################################################################################
#                                                                              #
#        Responda corretamente as perguntas para chegar a saída.               #
#        Em caso de erro retornará para a sua posição anterior.                #
#        Para voltar à tela inicial pressione "X" a qualquer momento.          #
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
####################    Pressione "ENTER" para prosseguir    ###################'''.format(imprimir.replace('~', ' ')))  # Printa substituindo "~" por " ".
    prox = input()  # Aguarda algo ser digitado para mudar de tela.
    os.system(limpar)  # Limpa a tela.
    voltar = []  # Cria uma lista para armazenar todos os movimentos.
    sorteados = []  # Cria uma lista para armazernar as perguntas ja sorteadas.
    indice = 0  # Indice 0 pois o usuário não se moveu.
    situacao = '''#                                                                              #
#         Aguardando resposta...                                               #'''  # Atribui esse valor a variável para ser printada.
    while labirinto.find('.') != -1:  # Enquanto houver pontos o programa vai rodar.
        sorteio = random.randint(1, len(perguntas))  # Sorteia a pergunta.
        # Converte o número inteiro sorteado em string pois é o tipo de chave do dicionário.
        sorteio = str(sorteio)
        if len(sorteados) == len(perguntas):
            # Se todas as perguntas ja forem feitas será zerado e poderão se repetir.
            sorteados = []
        while sorteio in sorteados:
            sorteio = random.randint(1, len(perguntas))  # Sorteia a pergunta.
            # Converte o número inteiro sorteado em string pois é o tipo de chave do dicionário.
            sorteio = str(sorteio)
        # Adiciona o número da pergunta sorteada a lista
        sorteados.append(sorteio)
        os.system(limpar)  # Limpa a tela.
        resposta = input('''################################################################################
#                                                                              #
#                        JOGO DO LABIRINTO - MODO QUIZ                         #
{}
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
################################################################################

     {}

     a) {}
     b) {}
     c) {}
     d) {}

     X - Voltar ao menu.
################################    Responda    ################################
'''.format(situacao, imprimir.replace('~', ' '), perguntas[sorteio]['p'], perguntas[sorteio]['a'], perguntas[sorteio]['b'], perguntas[sorteio]['c'], perguntas[sorteio]['d']))  # LÊ se a resposta.
        disponiveis = ['a', 'b', 'c', 'd', 'x']  # POssiveis entradas.
        # Remove espaços vazios antes e depois do texto.
        resposta = resposta.strip()
        resposta = resposta.lower()  # Converte toda string em letra minúscula.
        os.system(limpar)  # Limpa a tela.
        # Executa caso seja dado um valor inválido.
        while ((resposta in disponiveis) == False):
            situacao = '''#         Opção inválida!                                                      #
#         Tente novamente...                                                   #'''  # Atribui esse valor a variável para ser printada.
            os.system(limpar)  # Limpa a tela.
            resposta = input('''################################################################################
#                                                                              #
#                        JOGO DO LABIRINTO - MODO QUIZ                         #
{}
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
################################################################################

     {}

     a) {}
     b) {}
     c) {}
     d) {}

################################    Responda    ################################
'''.format(situacao, imprimir.replace('~', ' '), perguntas[sorteio]['p'], perguntas[sorteio]['a'], perguntas[sorteio]['b'], perguntas[sorteio]['c'], perguntas[sorteio]['d']))  # Lê se a nova entrada.
            resposta = resposta.strip()  # Remove espaços vazios antes e depois do texto.
            # Converte toda string em letra minúscula.
            resposta = resposta.lower()
            os.system(limpar)  # Limpa a tela.
        # Verifica se a resposta está correta.
        if resposta == perguntas[sorteio]['e']:
            situacao = '''#                                                                              #
#         Aguardando resposta...                                               #'''  # Atribui esse valor a variável para ser printada.
            voltar.append([])  # Adiciona uma lista vazia a lista ja existente.
            # Enquanto houverem "*" e "." há possibilidade de movimento.
            for i in range(labirinto[:labirinto.find('.')].count('~')):
                # Adiciona o movimento a última lista.
                voltar[-1].append(labirinto)
                # Substitui o asterisco por um espço vazio.
                labirinto = labirinto.replace('*', ' ')
                # Substitui o próximo passo por asterisco uma vez.
                labirinto = labirinto.replace('~', '*', 1)
                # substitui todos os pontos por espaços vazios para imprimir.
                imprimir = labirinto.replace('.', ' ')
                print('''################################################################################
#                                                                              #
#                        JOGO DO LABIRINTO - MODO QUIZ                         #
#         Resposta correta!                                                    #
#         Siga em frente.                                                      #
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
################################################################################'''.format(imprimir.replace('~', ' ')))  # Printa substituindo todos os "~" por " ".
                time.sleep(0.3)  # Aguarda 0.3 segundos para prosseguir.
                os.system(limpar)  # Limpa a tela.
            # Substitui o asterisco por um espço vazio.
            labirinto = labirinto.replace('*', ' ')
            # Substitui o próximo passo por asterisco uma vez.
            labirinto = labirinto.replace('.', '*', 1)
            # substitui todos os pontos por espaços vazios para imprimir.
            imprimir = labirinto.replace('.', ' ')
            voltar[-1].append(imprimir.replace('~', ' ')
                              )  # Salav esse movimento
            print('''################################################################################
#                                                                              #
#                        JOGO DO LABIRINTO - MODO QUIZ                         #
#         Resposta correta!                                                    #
#         Siga em frente.                                                      #
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
####################    Pressione "ENTER" para prosseguir    ###################'''.format(imprimir.replace('~', ' ')))  # Printa substituindo todos os "~" por " ".
            prox = input()  # Aguarda algo ser digitado para mudar de tela.
            os.system(limpar)  # Limpa a tela.
            if prox == 'x':
                # Encerra o loop se for digitado "x", voltando para a tela inicial.
                break
            indice += 1  # O usuário se movimentou mais uma vez.
        elif resposta == 'x':
            # Encerra o loop se for digitado "x", voltando para a tela inicial.
            break
        else:  # Em caso de resposta errada.
            situacao = '''#                                                                              #
#         Aguardando resposta...                                               #'''  # Atribui esse valor a variável para ser printada.
            if (indice == 0):  # Indice 0 significa que o usuário está na entrada, não podendo retroceder.
                os.system(limpar)  # Limpa a tela.
                print('''################################################################################
#                                                                              #
#                        JOGO DO LABIRINTO - MODO QUIZ                         #
#         Resposta incorreta!                                                  #
#         Você não saiu do lugar.                                              #
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
####################    Pressione "ENTER" para prosseguir    ###################'''.format(imprimir.replace('~', ' ')))  # Printa substituindo todos os "~" por " ".
                prox = input()  # Aguarda algo ser digitado para mudar de tela.
                os.system(limpar)  # Limpa a tela.
            else:
                indice -= 1  # Retrocedeu, eliminou um ponto.
                # Atribui o ponto anterior a variável de labirinto.
                labirinto = voltar[-1][0]
                # Faz a quantidade de movimentos que foram "salvos".
                for i in range(len(voltar[-1])):
                    # Atribui o último movimento a uma variável.
                    imprimir = voltar[-1][-1]
                    # Junta todos os elementos em uma string.
                    imprimir = ''.join(imprimir)
                    # Imprime substituindo pontos por espaços.
                    imprimir = imprimir.replace('.', ' ')
                    print('''################################################################################
#                                                                              #
#                        JOGO DO LABIRINTO - MODO QUIZ                         #
#         Resposta incorreta!                                                  #
#         Você voltará para a posição anterior.                                #
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
##########################################################33####################'''.format(imprimir.replace('~', ' ')))  # Printa substituindo todos os "~" por " ".
                    time.sleep(0.3)  # Aguarda 0.3 segundos para prosseguir.
                    os.system(limpar)  # Limpa a tela.
                    # Deleta o último movimento já printado, para que se possa imprimir a sequência em ordem inversa.
                    del voltar[-1][-1]
                print('''################################################################################
#                                                                              #
#                        JOGO DO LABIRINTO - MODO QUIZ                         #
#         Resposta incorreta!                                                  #
#         Você voltou para a posição anterior.                                 #
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
####################    Pressione "ENTER" para prosseguir    ###################'''.format(imprimir.replace('~', ' ')))  # Printa substituindo todos os "~" por " ".
                prox = input()  # Aguarda algo ser digitado para mudar de tela.
                os.system(limpar)  # Limpa a tela.
                if prox == 'x':
                    # Encerra o loop se for digitado "x", voltando para a tela inicial.
                    break
                # Deleta a última lista de sequência de movimentos.
                del voltar[-1]
    # Se não tem pontos significa que o usuário chegou ao fim.
    if labirinto.find('.') == -1:
        os.system(limpar)  # Limpa a tela.
        fim = input('''################################################################################
#                                                                              #
#                        JOGO DO LABIRINTO - MODO QUIZ                         #
#         Parabéns! Você conseguiu chegar a saída.                             #
#         Deseja jogar novamente? [1 - Sim; 2 - Não]                           #
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
################################################################################
'''.format(imprimir.replace('~', ' ')))  # Printa substituindo todos os "~" por " ".
        fim = fim.strip()  # Remove espaços vazios antes e depois do texto.
        fim = fim.lower()  # Converte toda string em letra minúscula.
        os.system(limpar)  # Limpa a tela.
        possiveis = ['1', '2', 'x']  # Possíveis entradas.
        while ((fim in possiveis) == False):
            os.system(limpar)  # Limpa a tela.
            fim = input('''################################################################################
#                                                                              #
#                        JOGO DO LABIRINTO - MODO QUIZ                         #
#         Opção inválida.                                                      #
#         Deseja jogar novamente? [1 - Sim; 2 - Não]                           #
#                                                                              #
################################################################################
#                                                                              #
{}
#                                                                              #
################################################################################
'''.format(imprimir.replace('~', ' ')))  # Lê se o usário deseja jogar novamente.
            fim = fim.strip()  # Remove espaços vazios antes e depois do texto.
            fim = fim.lower()  # Converte toda string em letra minúscula.
            os.system(limpar)  # Limpa a tela.
    if fim == '2':
        os.system(limpar)  # Limpa a tela.
        print(encerrar(limpar))  # Função para encerrar o programa.
    else:
        time.sleep(0)  # Não permite que a execução pare.
