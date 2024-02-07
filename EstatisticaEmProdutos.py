total = produtos = maior = menor = 0
cont = 1
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    total += preco
    simounao = ' '
    while simounao not in "SN":
        simounao = str(input('Você quer continuar [S/N]: ')).upper().strip()[0]
    if simounao == 'N':
        break
    if preco >= 1000:
        produtos += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
print(f'O valor total da compra é {total:.2f}.')
print(f'Os produtos que custam mais que R$1000.00 reais são: {produtos}.')
print(f'O produto mais barato é o {barato}.')
