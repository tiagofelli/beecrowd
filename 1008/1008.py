n = 2

total_a_pagar = 0

for i in range(n):
    codigo, qtde, valor = map(float, input().split())
    total_a_pagar += qtde * valor

print("VALOR A PAGAR: R$ %.2f" % total_a_pagar)

