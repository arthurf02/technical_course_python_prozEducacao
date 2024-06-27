'''
    Crie um programa que recebe nome de ações da bolsa de valores.
    Cada vez que o programa rodar você deve adicionar o nome da ação a uma 
    lista. Permita ao usuário remover uma ação e ordene elas pelo nome. 
    Permissões: Ler a lista, Adicionar a lista, Alterar a lista e Excluir da lista
'''

lista_acao: list = []

while True:
    opc: str = input("Digite a opção:\n - A para inserir \n - D para deletar \n - S para substituir \n - V para ver dados\n")
    if opc == "A":
        dados: str = input("Digite a acão: ")
        lista_acao.append(dados)
        print("Dados inseridos com sucesso!")
    elif opc == "D":
        dados: str = input("Informe o nome da ação que deseja apagar: ")
        if dados in lista_acao:
            lista_acao.remove(dados)
        print("Dados deletados com sucesso!")
    elif opc == "S":
        dados: str = input("Digite a acão: ")
        lista_acao[1] = dados
        print("Dados substituídos")
    elif opc == "V": 
        print(lista_acao)
    else:
        break