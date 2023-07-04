# print("Hello World!")

nome = "Thiago"
idade = 21
num1 = 5
num2 = 10.3
num3 = "2"
# Verificando os tipos das variáveis num1, num2 e num3
print(type(num1))
print(type(num2))
print(type(num3))

# Convertendo num1 de int para string
num1 = str(num1)
print(type(num1))


# Convertendo string para float

num1 = float(num1)
print(type(num1))
print(num1)


# Brincando com calculo
var1 = input("Digite um número: ")  # O input sempre trás uma string, para fazer calculos com os resultadoos do input é necessário converte-los para int ou float.
var1 = int(var1)
var2 = input("Digite outro número: ") # O input sempre trás uma string, para fazer calculos com os resultadoos do input é necessário converte-los para int ou float.
var2 = int(var2)
soma = var1 + var2
print(f"A soma de {var1} + {var2} é: {soma}")