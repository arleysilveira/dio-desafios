import textwrap

def usuario_existe(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf= input("Digite seu CPF (somente números): ")
    usuario = usuario_existe(cpf, usuarios)

    if usuario:
        print("Usuário ja existe")
        return
    
    usuarios.append({
        'cpf': cpf,
        'nome': input("Digite seu nome: "),
        'data_nascimento': input("Digite sua data de nascimento: "),
        'endereco': input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    })
    
    print("Usuário criado com sucesso")
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF (somente números): ")
    usuario = usuario_existe(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso")
        return {
            'agencia': agencia,
            'numero_conta': numero_conta,
            'usuario': usuario
        }
        
    print("Usuário não encontrado")

def depositar(valor, saldo, extrato, /):
    if valor < 0:
        return "O valor do depósito não pode ser negativo"
    saldo += valor
    extrato += f"Deposito: R$ {valor:.2f}\n"
    return saldo, extrato

def visualizar_extrato(saldo, /, *, extrato):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

def sacar(*, valor, saldo, extrato, numero_saques, limite_valor_saque, limite_saque):
    if valor < 0:
        print("O valor do saque não pode ser negativo")
    elif valor > saldo:
        print("Saldo insuficiente para o saque")
    elif numero_saques >= limite_saque:
        print("Limite de saques excedido")
    elif valor > limite_valor_saque:
        print("Saque maior que o permitido")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso")
        return saldo, extrato
    
def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [nu] Novo Usuário
    [q] Sair

    => """
    
    return input(textwrap.dedent(menu))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite_valor_saque = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Quanto deseja depositar? "))
            saldo, extrato = depositar(valor, saldo, extrato)
            
        elif opcao == "s":
            saldo, extrato = sacar(
                valor=float(input("Quanto deseja sacar? ")), 
                saldo=saldo, 
                extrato=extrato, 
                numero_saques=numero_saques, 
                limite_valor_saque=limite_valor_saque, 
                limite_saque=LIMITE_SAQUES)
            
        elif opcao == "e":
            visualizar_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            conta = criar_conta(AGENCIA, len(contas) + 1, usuarios)
            
            if conta:
                contas.append(conta)
        
        elif opcao == "q":
            break

        else:
            print("Operaçãoo inválida, por favor selecione novamente a operação desejada.")
            
main()