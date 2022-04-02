import random

moto = random.randint(0, 400)
carro = random.randint(0, 400 - moto)
onibus = random.randint(0, 400 - carro)

print('Valor final R$:', moto * 4 + carro * 8 + onibus * 20)

