import random
from operator import itemgetter

# ========= INÍCIO DAS DEFINIÇÕES DE FUNÇÕES =========
# Função que produz um dicionário baseado nas entradas do usuário.
def Inserir():
    dic_temp = {}
    voucher = random.randint(100,400)
    nome = input("Digite seu nome: ")
    email = input("Digite email: ")
    fone = input("Digite telefone: ")
    curso = input("Digite curso: ")
    
    dic_temp = {'Voucher': voucher,
                'Nome': nome, 
                'Email': email, 
                'Telefone': fone,
                'Curso': curso
                }
    
    return dic_temp

#Função para visualizar os dados constantes na lista de dicionários.
def visualizar(basedados):
    print("\n")
    print("-"*7+"Lista inscritos"+"-"*7)
    v = list(map(itemgetter('Voucher'), basedados))
    n = list(map(itemgetter('Nome'), basedados))
    e = list(map(itemgetter('Email'), basedados))
    f = list(map(itemgetter('Telefone'), basedados))
    c = list(map(itemgetter('Curso'), basedados))

    for i in range(len(basedados)):
        print(f"Voucher   : {v[i]}")
        print(f"Nome      : {n[i]}")
        print(f"Email     : {e[i]}")
        print(f"Telefone  : {f[i]}")
        print(f"Curso     : {c[i]}")
    print("\n")
# ========== FIM DAS DEFINIÇÕES DE FUNÇÕES ============
# Declaração de variáveis
baseDados = list()
encerrar = 0

# Rotina principal do programa\
while encerrar != 1:
    print("\n")
    print("*"*15+" Menu "+"*"*15)
    print("1 - Nova inscrição")
    print("2 - Visualizar inscrição")
    print("0 - Encerrar")
    opcao_selecionada = int(input("Opção escolhida: "))

    if opcao_selecionada == 0:
        encerrar = 1

    elif opcao_selecionada == 1:
        baseDados.append(Inserir())

    elif opcao_selecionada == 2:
        visualizar(baseDados)
    
    else:
        print("\nErro: digite uma opção válida!\n")
