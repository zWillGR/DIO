menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print ("Operação falho! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque:  "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print ("Operação falho! saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! você excedeu o saque limite.")

        elif excedeu_saques:
            print("Operação falho! você execeu o maximo de saques diários.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n "
            numero_saques += 1

        else:
            print("Operação falho! Valor informado é inválido.")

    elif opcao == "e":
        print("\n=================Extrato=================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("==================================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida.")



       


 
