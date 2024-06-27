#Cadastrar adultos
def cadastroAluno():
    global aluno
    nome = str(input('Nome: '))
    matricula = str(input('Matricula: '))
    telefone = str(input('Telefone: '))
    aluno = [nome, matricula, telefone]
    return aluno
def cadastroProfessor():
    global professor
    nome = str(input('Nome: '))
    matricula = str(input('Matrícula: '))
    telefone = str(input('Telefone: '))
    professor = [nome, matricula, telefone]
    return professor
def imprimeLista(lista):
    for valor in lista:
        print(valor)