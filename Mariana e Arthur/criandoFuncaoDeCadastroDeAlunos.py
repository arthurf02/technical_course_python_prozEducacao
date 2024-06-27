def cadastro():
    global alunos
    alunos = []
    while True:
        nome=str(input('Nome: '))
        if nome != '' and nome != 'sair':
            alunos.append(nome)
        else:
            break
cadastro()
print(alunos)

#imprimir a lista sem colchetes e aspas
def imprime(alunos):
    for valor in alunos:
        print(valor)
imprime(alunos)