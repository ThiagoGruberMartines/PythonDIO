# AND = para ser True tudo precisa ser True
# OR = para ser True apenas um precisa ser True

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = (saldo >= saque and saque <=limite) or (conta_especial and saldo >=saque)
print(exp)