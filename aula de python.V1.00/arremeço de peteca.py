pontuacao1 = int(input("Digite a pontuação do jogador"))
pontuacao2 = int(input("Digite a pontuação do jogador"))
pontuacao3 = int(input("Digite a pontuação do jogador"))
soma = pontuacao1 + pontuacao2 + pontuacao3
if soma == 15 :
 print("Deus da peteca")
elif soma == 0:
 print("Nunca petequeiro")
elif soma <= 4 :
 print("pseudo-petequeiro")
elif soma <= 9 :
 print("petequeiro de final de semana")
elif soma <= 14 :
 print("petequeiro profissa")
else:
 print("invalido")