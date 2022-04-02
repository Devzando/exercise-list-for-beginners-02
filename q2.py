print('Informe o valor da base')
base = int(input())
print('informe o valor do expoente')
expo = int(input())

result = 0
i = 1

if expo == 0:
    result = 1 

while i < expo:

    if result > 0:
        result = result = result * base
    else:
        result = base * base
    i+=1

print('resultado:', result )