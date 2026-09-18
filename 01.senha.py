nome_cadastro = ()
senha_cadastrada = ()
senha_digitada = ()
nome_digitado = ()
cadastro = input("Você já possui um cdastro? (S/N)").lower()


if cadastro == "n".lower():
    nome_cadastro = input("Digite seu nome: ")
    senha_cadastrada = input("Digite sua senha: ")
    print("Cadastro realizado com sucesso!")
    print("Agora faça o login para acessar o sistema.")
    nome_digitado = nome_cadastro
    senha_digitada = senha_cadastrada
    nome_digitado = input("Digite o nome cadastrado: ")
    senha_digitada = input("Digite sua senha: ")
else :
    nome_digitado = input("Digite o nome cadastrado: ")
    senha_digitada = input("Digite sua senha: ")
while senha_digitada != senha_cadastrada and nome_digitado != nome_cadastro:
    print("algo esta incorreto! Tente novamente.")
    nome_digitado = input("Digite o nome cadastrado: ")
    senha_digitada = input("Digite sua senha: ")

print ("Bem-vindo ao Sistema...")