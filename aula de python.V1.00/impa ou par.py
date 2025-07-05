num1 = int(input("Digite um número"))
calc = num1 % 2
if  calc == 0 and num1 > 0:
    print(f"{num1} é par e positivo")
elif calc == 0 and num1 < 0:
    print(f"{num1} é par e negativo")
elif calc != 0 and num1 >= 0:
    print(f"{num1} é impar e positivo")
else:
    print(f"{num1} é impar e negativo")