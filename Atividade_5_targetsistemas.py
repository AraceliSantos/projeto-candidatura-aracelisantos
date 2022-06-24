a = input('Digite uma palavra ou frase: ')
print(a, '\n')

list(a)


len(a) #apenas para retornar o valor do tamanho da str

new_a = list()

n = 0
n = len(a)

for i in a:
    if n != 0:
        new_a.append(a[n - 1])
        n = n - 1

print(new_a, '\n')
 #para verificar se inverteu corretamente a str

text = "" .join(new_a)
print(text)