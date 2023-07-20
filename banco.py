menu = """
********* MENU *******
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
**********************
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print('Depositar')
        valor = int(input('Insira valor que deseja depositar: '))
        if valor > 0 :
            saldo += valor
            extrato += f"Deposito : + R${valor:.2f}\n"
        else:
            print('Valor negativo , tente novamente!')

    elif opcao == 's':
        print('Sacar')
        if numero_saques < LIMITE_SAQUES:
            valor = int(input('Insira o valor deseja sacar: '))

            if valor <=0:
                print("Valor menor ou igual a 0, insira um número válido")
            elif valor > limite:
                print("Valor do saque é limitado a R$500 por saque!")  
            elif valor > saldo:
                print("Não é possível sacar por falta de saldo!")      
            else :
                saldo -= valor
                extrato += f"Saque : - R${valor:.2f}\n"
                numero_saques += 1
        else:
            print('Limite de 3 saques diários atingido!')

    elif opcao == 'e':
        if extrato == '':
            print("Não foram realizadas movimentações.")
        else:    
            print('## Extrato ##') 
            print(f"{extrato}Saldo = {saldo}") 

    elif opcao == 'q':
        print('Obrigado por usar nosso sistema bancário !')  
        break  