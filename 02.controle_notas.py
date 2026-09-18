nome = input("Digite o nome do aluno: ")
nota = float(input("insira a nota: "))
mais = input("Deseja adicionar mais notas? (S/N) ")
soma = (0)
loop = (1)

while mais == "sim":
    nota = float(input("Dgitie a nota: "))
    soma = soma + nota
    loop = loop + 1
    mais = (input ("Deseja adicionar mais notas? (S/N) "))

print("Sua média é: ",soma / loop)
   