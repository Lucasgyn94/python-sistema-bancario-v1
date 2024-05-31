menu = """
########## Menu ##########
    1- Depositar
    2- Sacar
    3- Extrato
    0- Sair
###########################
"""

saldo = 0;
limite = 500;
extrato = "";
numero_saques = 0;
LIMITE_SAQUES = 3;

while True: 
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "));
        saldo = saldo + valor;
        print(f"\nValor de R$ {valor:.2f} depositado(s) com sucesso!");

        extrato = extrato + f"Depósito de R$ {valor:.2f}\n";
    elif opcao == "2":
        valor = float(input("Informe o valor a ser sacado: "));

        excedeu_saldo = valor > saldo;
        excedeu_limite = valor > limite;
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha! Você não possui saldo suficiente.");
        
        elif excedeu_limite:
            print("Falha! O valor do saque excede o limite.");

        elif excedeu_saques:
            print("Falha! Você excedeu o limite de saques.");
        
        elif valor > 0:
            saldo = saldo - valor;
            extrato = extrato + f"Saque de R$ {valor:.2f}\n";
            numero_saques += 1;
        else:
            print("Operação falhou! Valor informado é inválido.");

    elif opcao == "3":
        print("=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato);
        print(f"\nSaldo R$ {saldo:.2f}");
        print("======================================");

    elif opcao == "0":
        break;
    
    else:
        print("Opção inválida! Selecioe uma entre as opções!");