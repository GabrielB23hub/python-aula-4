def soma():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    print ("Somando...")
    print ("A soma dos números é", numero1 + numero2 )

def subtracao():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    print ("Subtraindo...")
    print ("A subtração dos números é", numero1 - numero2)

def multiplicacao():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    print("Multiplicando...")
    print ("A multiplicação dos números é", numero1 * numero2)
def divisao():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    print("Dividindo...")
    print ("A divisão dos números é", numero1 / numero2)
def pares():
    par = 0
    loop = 1
    quantidade = int(input("Digite quantos números você quer: "))
    while loop <= quantidade:
        print(par + 2)
        par += 2
        loop += 1
def impares():
    impar = -1
    loop = 1
    quantidade = int(input("Digite quantos números você quer: "))
    while loop <= quantidade:
        print(impar + 2)
        impar += 2
        loop += 1
def somatoria():
    somatoria = 1
    quantidade = int(input("Digite a quantidade que você quer: "))
    soma = 0
    while somatoria <= quantidade:
        soma = soma + somatoria
        somatoria += 1
    print (soma)
def fatorial():
    fatorial = 1
    numero = int(input("Digite o fatorial: "))
    loop = 1
    while loop <= numero:
        fatorial = fatorial * loop
        loop += 1 
    print(fatorial)
    
while True:
    print ("CALCULADORA")
    print ("1 - Adição")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")
    print ("5 - Pares")
    print ("6 - Impares")
    print ("7 - Somátoria")
    print ("8 - Fatorial")
    print ("0 - Sair")

    opcao = input ("Escolha uma opção: ")

    if opcao == "1":
        soma()

    elif opcao == "2":
        subtracao()
    elif opcao == "3":
        multiplicacao()
    elif opcao == "4":
        divisao()
    elif opcao == "5":
        pares()
    elif opcao == "6":
        impares()
    elif opcao == "7":
        somatoria()
    elif opcao == "8":
        fatorial()
    elif opcao == "0":
        print ("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

