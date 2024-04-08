valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)

for nota in notas:
    qtd_notas = valor // nota
    mensagem = str(qtd_notas) + ' nota(s) de R$ ' + str(nota) + ',00'
    print(mensagem)
    valor %= nota
    

