# criando uma função
def ola():
    print('Olá')

# solicitando a execução (chamando a função) do que está dentro da função
ola()

# criando uma função que quando for solicitada irá gravar o nome de um aluno até que o usuário digite 0
def cria_lista():
    global nome # definindo a variável como global. ou seja, poderá ser usada em todo o codigo
    lista=[]
    nome=''
    while nome != '0':
        nome=str(input('Digite o nome de um aluno (0 para sair): '))
        if nome != '0':
            lista.append(nome)
        print(lista)

#solicitando a execução (chamando a função) do que está dentro da função
cria_lista()

# chamando a função 10 vezes automaticamente
for i in range(11):
    cria_lista()