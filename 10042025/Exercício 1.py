valor = 0.0
while (True):
    lista = [1, 2, 3, 5, 9]
    list = [0.5, 1, 4, 7, 8]
    code = int(input('Digite o código do produto comprado:'))
    if code == 0:
        print(f'O valor da compra é de R$ {valor:.1f}')
        break
    elif code not in lista:
        print('Código inválido')
        break
    else: 
        quant = int(input('Digite a quantidade do produto:'))
        for i in range (5):
            if code == lista[i]:
                valor += list [i] * quant 