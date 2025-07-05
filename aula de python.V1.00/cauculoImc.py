#Fazer um programa no qual o usuário digite a sua altura e o seu peso, ao final mostre o IMC 
# (índice de massa corporal) e uma mensagem se está abaixo do peso (IMC menor que 18), na faixa 
# de peso ideal (IMC de 18 a 25) ou acima do peso (IMC maior 25). IMC = peso / (altura * altura).


altura = float(input("Digite sua altura "))
peso = float (input ("Digite seu peso "))
calc_imc =  peso / (altura * altura)

if calc_imc < 18 :
    print("Você Esta Abaixo Do Peso")
elif calc_imc <= 25 :
    print("na faixa de peso ideal")   
else :
    print("Você ésta a cima do peso")

