
## declaração de variáveis.
parar = "N"
nome = ""
idade = 0
niveis_de_ensino = ["Educação Infantil", "Ensino Fundamental I",
                    "Ensino Fundamental II", "Ensino Médio"]

## while loop para manter o programa em execução após o fim da rotina.
while parar != "S":

## apresentação e captura de informações do usuário para validação.
    print("\n===========================================================")
    print("Programa para identificar a etapa de ensino. Por gentileza forneça:")
    nome = input("Nome do aluno(a): ")
    idade = int(input("Idade do aluno(a): "))
    
## condicionais para validação dos dados inseridos dentro de cada categoria de ensino.
    if idade >= 1 and idade <= 5:
        print(f"\nEstudante {nome} tem {idade} anos e está no {niveis_de_ensino[0]}.")
        print("===========================================================")
    elif idade > 5 and idade <= 10:
        print(f"\nEstudante {nome} tem {idade} anos e está no {niveis_de_ensino[1]}.")
        print("===========================================================")
    elif idade > 10 and idade <= 14:
        print(f"\nEstudante {nome} tem {idade} anos e está no {niveis_de_ensino[2]}.")
        print("===========================================================")
    elif idade > 14:
        print(f"\nEstudante {nome} tem {idade} anos e está no {niveis_de_ensino[3]}.")
        print("===========================================================")
    else:
        print("Idade não fornecida corretamente.\n")

    # condição de avaliação para término de programa.
    print("\nDeseja sair do programa? S - Sim     Qualquer tecla - Não")
    parar = input("Digite sua resposta: ")
    if parar == 'S':
        break
