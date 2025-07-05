saldo = 500

caso = input("Escolha uma das 3 opções: (1 Ver saldo bancário), (2 Depositar dinheiro), (3 Sacar dinheiro): ")

match caso:
    case "1":
        print(f"Seu saldo atual é: R$ {saldo}")
    case "2":
        add_saldo = float(input("Digite quanto deseja depositar: "))
        saldo += add_saldo
        print(f"Novo saldo é: R$ {saldo}")
    case "3":
        saque = float(input("Digite quanto deseja sacar: "))
        if saque <= saldo:
            saldo -= saque
            print(f"Saque realizado. Novo saldo: R$ {saldo}")
        else:
            print("Saldo insuficiente.")
    case _:
        print("Opção inválida.")