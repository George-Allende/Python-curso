numero = int(input("Digite um número de 1 a 3: "))


match numero:
    case 1 | 2 | 3:
        print(f"opção {numero}")
    