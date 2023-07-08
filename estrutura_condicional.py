MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade. Pode tirar a CNH.")
if idade < MAIOR_IDADE:
    print("Menor de idade. Não pode tirar a CNH.")





if idade >= MAIOR_IDADE:
    print("Maior de idade. Pode tirar a CNH.")
else:
    print("Menor de idade. Não pode tirar a CNH.")





if idade >= MAIOR_IDADE:
    print("Maior de idade. Pode tirar a CNH.")
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Menor de idade. Não pode tirar a CNH.")