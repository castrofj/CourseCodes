import copy

# ========= INÍCIO DAS DEFINIÇÕES DE FUNÇÕES =========
# Função para gerar tabuleiro de fase.
def criarTabuleiro(tabuleiro, setup):
    gameset = copy.deepcopy(tabuleiro)
    index = 0
    jogadas = 0
    
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            gameset[i][j] = setup[index]
            if (setup[index]) == "_":
                jogadas += 1
            index += 1

    print("========Tabuleiro=======")
    print("=   1    2    3    4   =")
    print(f"= {gameset[0]} =")
    print(f"= {gameset[1]} =")
    print("=   5    6    7    8   =")
    print("========================")
    
    return gameset, jogadas

# !!!FUNÇÃO PRINCIPAL QUE IMPLEMENTA A MECÂNICA DO JOGO!!!
# A idéia da função é:
# Etapa 1. transformar o tabuleiro em uma lista de vetores.
# Etapa 2. inserir os animais escolhidos pelo usuário nos quartos correspondentes.
# Etapa 3. converter os animais em um número definido pelo dicionário dict_animais_num. 
# Os número foram escolhidos de maneira que a diferença entre eles não possa resultar nos núméros da lista lista_gameover.
# Etapa 4. realizar uma série de subtrações de cada elemento do vetor com a casa(s) vizinha(s) ao lado / acima ou abaixo. O resultado da subtração é guardado em uma lista.
# Etapa 5. verificar se os elementos da lista de resultado das subtrações estão pertencem à lista_gameover. Se sim, o jogo acaba.

def checkGameOver(tabuleiro_fase, jogadas, animais):
    turno = []
    dict_animais_letra = {'GATO': 'G', 'CÃO': 'C', 'RATO': 'R', 'OSSO': 'O', 'QUEIJO': 'Q'}
    dict_animais_num = {'*':0,'G': 1, 'C': 10,'R': 2, 'O': 19, 'Q': 5}
    lista_validacao = [] # variável que será utilizada para receber conversão de matrix 2x4 to tabuleiro em um vetor 1x8 para validação se Game Over
    check = []
    lista_gameover = [-9,-1,3,9]
    index = 0
    output = False
    
    # Etapa 1
    for i in range(len(tabuleiro_fase)):
        for j in range(len(tabuleiro_fase[i])):
            lista_validacao.append(tabuleiro_fase[i][j])
            index += 1
    index = 0

    # pergunta do usuário onde o animal deverá ser jogado igual ao número de jogadas 
    # (recodardando que jogadas está baseado na quantidade de campos "_" calculado dentro da função criarTabuleiro)
    for i in range(jogadas):
        turno.append(int(input(f"Em qual posição quer alocar o {animais[i]}? - Digite o número: ")))
    
    # Etapa 2
    for i in range(jogadas):
        lista_validacao[turno[i]-1] = dict_animais_letra[animais[i]]

    # Etapa 3
    for i in range(len(lista_validacao)):
        lista_validacao[i] = dict_animais_num[lista_validacao[i]]

    # Etapa 4
    for i in range(len(lista_validacao)):
        if lista_validacao[i] == 0:
            continue
        else:
            if i == 0:
                if lista_validacao[i+1] != 0:
                    check.append(lista_validacao[i] - lista_validacao[i+1])
                if lista_validacao[i+4] != 0:
                    check.append(lista_validacao[i] - lista_validacao[i+4])
                continue
            if i == 1 or i == 2:
                if lista_validacao[i-1] != 0: 
                    check.append(lista_validacao[i] - lista_validacao[i-1])
                if lista_validacao[i+1] != 0:
                    check.append(lista_validacao[i] - lista_validacao[i+1])
                if lista_validacao[i+4] != 0:
                    check.append(lista_validacao[i] - lista_validacao[i+4])
                continue
            if i == 3:
                if lista_validacao[i-1] != 0:
                    check.append(lista_validacao[i] - lista_validacao[i-1])
                if lista_validacao[i+4] != 0:
                    check.append(lista_validacao[i] - lista_validacao[i+4])
                continue
            if i == 4:
                if lista_validacao[i-4] != 0:
                    check.append(lista_validacao[i] - lista_validacao[i-4])
                if lista_validacao[i+1] != 0:
                    check.append(lista_validacao[i] - lista_validacao[i+1])
                continue
            if i == 5 or i == 6:
                if lista_validacao[i-1] != 0:
                    check.append(lista_validacao[i] - lista_validacao[i-1])
                if lista_validacao[i+1] != 0:
                    check.append(lista_validacao[i] - lista_validacao[i+1])
                if lista_validacao[i-4] != 0:
                    check.append(lista_validacao[i] - lista_validacao[i-4])
                continue
            if i == 7:
                if lista_validacao[i-4] != 0:
                    check.append(lista_validacao[i] - lista_validacao[i-4])
                if lista_validacao[i-1] != 0:
                    check.append(lista_validacao[i] - lista_validacao[i-1])
                continue

    # Etapa 5
    for i in range(len(check)):
        if check[i] in lista_gameover: 
            output = True
            break

    if output == True:
        print("\n"+"!"*10+"Game Over"+"!"*10+"\n")
    
    return output

# Função que verifica se o jogador finalizou o jogo.
def zerouJogo(fase, tabuleiro):
    output = False
    if fase == len(tabuleiro):
        output = True
        print("\n"+"!"*10+"Você ganhou"+"!"*10+"\n")
    return output

# ========== FIM DAS DEFINIÇÕES DE FUNÇÕES ============

# DECLARAÇÕES DE VARIÁVEIS.
# Lista com configurações de cada fase.
gameboard_fase = [
    ['*', '*', '_', 'G', 'R', '_', '*', '*'],
    ['_', '*', '*', '*', '*', 'C', '_', '_'],
    ['_', '*', '*', '*', '_', 'G', '_', '*'],
    ['_', '_', '_', '*', '*', 'R', '*', '*']
]
animais = [
    ['RATO', 'GATO'],
    ['CÃO', 'CÃO', 'OSSO'],
    ['GATO', 'RATO', 'OSSO'],
    ['QUEIJO', 'QUEIJO', 'OSSO']
]
tabuleiro = [[1, 2, 3, 4], [5, 6, 7, 8]]
game_over = False
zerou = False
fase = 1

# APRESENTAÇÃO DO JOGO
print("\n")
print("="*100)
print(" "*41+"HOTEL DOS ANIMAIS")
print("="*100)

# GAME START
while game_over == False:
    #rotina to jogo.
    for i in range(len(gameboard_fase)):
        print(f"\nBem vindo à fase {fase}!")
        print(
            f"Na fase {fase}, o jogador deve alocar os animais {animais[i]} na seguinte matriz que representa os quartos!\n")

        tabuleiro_fase, jogadas = criarTabuleiro(tabuleiro, gameboard_fase[i])

        game_over = checkGameOver(tabuleiro_fase, jogadas, animais[i])
        if game_over == True:
            break
        
        game_over = zerouJogo(fase, gameboard_fase)
        if game_over == True:
            break
        else:
            fase += 1
        
   
