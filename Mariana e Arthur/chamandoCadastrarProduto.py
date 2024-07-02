import funcaoCadastrarProduto
produtos=list()
usuario=''
while usuario != '0' or usuario != 'n':
    usuario=input('Cadastrar um produto (s para sim, n para não)? ')
    if usuario == 's':
        funcaoCadastrarProduto.cadastrar_produto()
    print(produtos)