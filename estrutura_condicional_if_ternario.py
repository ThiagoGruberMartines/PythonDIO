saldo = 500
saque = float(input("Informe o saque: "))

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")