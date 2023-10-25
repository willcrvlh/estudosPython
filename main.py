def valor(preco, desconto):
    calculo = preco*(1-(0.01)*desconto)
    mensagem = f"O valor do produto é {preco} e com desconto de {desconto} % e o novo valor é {calculo}"
    return print(mensagem)
valor(127, 15)