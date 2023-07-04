# operadores aritméticos

# adição +,
# subtração -
# multiplicação *
# divisão /
# divisão retornando int //
# exponenciação **




# Armazenando os inputs em variáveis
valor1 = input("Digite um número: ")
valor2 = input("Digite outro número: ")

# Convertendo as strings das variáveis em float
valor1 = float(valor1)
valor2 = float(valor2)

# Criando os cálculos
adicao = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2
divisao = valor1 / valor2
divisaoint = valor1 // valor2
modulo = valor1 % valor2
exponenciacao = valor1 ** valor2


# Printando os calculos
print(f"A adição de {valor1} + {valor2} é: {adicao}")
print(f"A subtração de {valor1} - {valor2} é: {subtracao}")
print(f"A multiplicação de {valor1} * {valor2} é: {multiplicacao}")
print(f"A divisão de {valor1} / {valor2} é: {divisao}")
print(f"A divisão inteira de {valor1} // {valor2} é: {divisaoint}")
print(f"O módulo/resto de {valor1} % {valor2} é: {modulo}")
print(f"A exponenciação de {valor1} ** {valor2} é: {exponenciacao}")