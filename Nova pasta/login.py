#Criar um programa que simule o login de um roteador. O nome de usuário
#(username) é "admin" e a senha (password) "123". Pedir ao usuário para digitar username e password.
#Caso os dados estejam corretos, mostrar uma mensagem "Login efetuado!", caso contrário "Login falhou!". 
#(DESAFIO: Mostrar mensagens específicas para erro de username, de password ou de ambos).
nome_usuario = str(input("Digite seu usuário "))
senha = int(input("Digite a sua senha "))

if nome_usuario == "admin" and senha == 123:
    print("Login efetuado!")
elif nome_usuario != "admin" and senha != 123:
    print("O login falhou! Sua senha e nome de Usuário estão incorretos")
elif senha != 123:
    print("O login falhou! Sua senha esta incorreta")
else:
    print("O login falhou! O Seu Nome De Usuário esta incorreto")