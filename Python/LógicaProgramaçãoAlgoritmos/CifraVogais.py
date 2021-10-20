

# DECLARAÇÃO DE VARIÁVEIS
dicionario_cifra = {"A":"@","E":"&","I":"!","O":"#","U":"*"}
nome_lista = [] #lista onde irá cada caracter (consoante ou vogal encriptada).

# solicitação de dados do usuário. Variável guarda o dado em caixa alta.
nome = input("Digite um nome: ").upper()

# verifica se letra existe no dicionário e captura o valor da chave correspondente. 
for i in range(len(nome)):
    if nome[i] in dicionario_cifra:
        nome_lista.append(dicionario_cifra[nome[i]])
    else:
        nome_lista.append(nome[i])

# concatena cada um dos caracteres a uma única string atribuída à variável resultado
resultado = ''.join(nome_lista)

print(resultado)

