menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>"""

# Definindo as variáveis e constantes
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

# Criando o looping do Menu
while True:
    opcao = input(f"Escolha uma das opções: {menu}")

#Criando o método de depósito

    if opcao == "1":
        valor_deposito = float(input("Qual é o valor que deseja depositar? R$ "))
        saldo += valor_deposito
        extrato.append(f"Depósito de R$ {valor_deposito:.2f}")

#Criando o método de Saque

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Qual é o valor que deseja sacar? R$ "))
            if saldo >= valor_saque and valor_saque <= limite:
                saldo -= valor_saque
                extrato.append(f"Saque de R$ {valor_saque:.2f}")
                numero_saques += 1
            else:
                print("Saldo insuficiente ou valor de saque acima do limite.")
        else:
            print("Limite de saques atingido.")

#Criando o método de Extrato:

    elif opcao == "3":
        print("\nExtrato:")
        for transacao in extrato:
            print(transacao)
        print(f"Saldo atual: R$ {saldo:.2f}\n")

    elif opcao == "4":
        print("Muito obrigado por escolher o nosso banco!")
        break

    else:
        print("Opção errada. Escolha uma opção válida.")
