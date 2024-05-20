saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo, extrato
    if valor < 0:
        return "O valor do depósito não pode ser negativo"
    saldo += valor
    extrato += f"Deposito: R$ {valor:.2f}\n"
    return saldo

def visualizar_extrato():
    global saldo, extrato
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

def sacar(valor):
    global saldo, extrato, numero_saques, limite
    if valor < 0:
        print("O valor do saque não pode ser negativo")
    elif valor > saldo:
        print("Saldo insuficiente para o saque")
    elif numero_saques >= LIMITE_SAQUES:
        print("Limite de saques excedido")
    elif valor > limite:
        print("Saque maior que o permitido")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo
    
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


while True:

    opcao = input(menu)

    if opcao == "d":
        depositar(float(input("Quanto deseja depositar? ")))
    elif opcao == "s":
        sacar(float(input("Quanto deseja sacar? ")))
    elif opcao == "e":
        visualizar_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
