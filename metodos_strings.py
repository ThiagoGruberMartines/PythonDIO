texto = input("Digite algo: ")

print(texto.upper())    # Deixa tudo maiúsculo

print(texto.lower())    # Deixa tudo minúsculo

print(texto.title())    # Deixa só a primeira letra maiúscula e o resto minúsculo




curso = "   Python   "

print(curso.strip() + ".")    # Remove os espaços da esquerda e da direita

print(curso.lstrip() + ".")   # Remove os espaços da esquerda

print(curso.rstrip() + ".")   # Remove os espaços da direita




livro = "A Cabana"

print(livro.center(14, "#")) # Primeiro parâmetro define qual é o tamanho da string, caso a string seja menor que o parâmetro passado será atribuido o segundo parâmetro na string até que se complete o valor passado no primeiro parâmetro (Caso não seja definido o segundo parâmetro, automaticamente será adicionado espaçamentos na String)

print(".".join(livro)) # Separa toda letra pelo caracter passado no primeiro parâmetro