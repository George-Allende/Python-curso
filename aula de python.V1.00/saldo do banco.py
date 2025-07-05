saldo =int(500)

caso = input("escolha uma das 3 opções (1 Ver saldo bancário), (2 Depositar dinheir, (3 Sacar dinheiro) ")
match caso:
    case "1":
        print(f"Seu Saldo é {saldo}")
    case "2":
        add_saldo = float(input("Digite quanto deseja depositar"))
        saldo = saldo + add_saldo
        print(f"Novo saldo é igual á {saldo}")
    case "3":
        sacar_dinheiro = float(input("digite o valor que deseja sacar"))
        if saldo >= sacar_dinheiro:
         saldo = saldo - sacar_dinheiro
         print(f"seu novo saldo é {saldo}")
        else: 
           print("Você não tem saldo suficiente")
    case _:
        print("Digite uma opção valida") 