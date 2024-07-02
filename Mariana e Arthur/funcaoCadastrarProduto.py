def cadastrar_produto():
    produto={
        'Código':'',
        'Nome':'',
        'Preço de venda':'',
        'Estoque':'',
        'Código do fabricante':''
    }
    for i in produto:
        i=input(f'Digite o {i}: ')
    produtos=produto
    return f'Produto {produto["Nome"]} cadastrado com sucesso!'