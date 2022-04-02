import random

medias = []

for i in range(10):
    medias.append(random.randint(0, 10))

for i in medias:
    if i >= 7:
        print('aprovado')
    else:
        print('reprovado')