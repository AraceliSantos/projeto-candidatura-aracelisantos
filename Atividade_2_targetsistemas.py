#iniciando exercício 2

ult=1
penult=0
soma=1

lista = [0, 1]

#determinei uma extensão da lista, para não ser uma lista infinita, mesmo sabendo que a sequência de Fibonacci é infinita. 

for n in range(0,31):
    soma = ult + penult
    penult = ult
    ult = soma
    
    lista.append(soma)
    
n=int(input('Digite um número para verificar se este faz parte da sequência de Fibonacci: '))

if n in lista:
    print('O número pertence a sequência de Fibonacci!!')
else:
    print('O número NÃO pertence a sequência de Fibonacci.')
    