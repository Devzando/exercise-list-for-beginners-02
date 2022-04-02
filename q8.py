import random

loki = 0
inimigo = 0
result = []

print('Primeira disputa')

loki = random.randint(1, 100)
inimigo = random.randint(1, 100)

if loki > inimigo:
    print('loki venceu')
    result.append(True)
else:
    if loki == inimigo:
        print('Empate')
        result.append('empate')
    else:
        result.append(False)
        print('Volstagg venceu')

print('segunda disputa')
loki = 0

for i in range(10):
    loki += random.randint(0, 60)
    inimigo += random.randint(0, 60)
if loki > inimigo:
    result.append(True)
    print('Loki vencedor')
else:
    if loki == inimigo:
        result.append('empate')
        print('Empate')
    else:
        result.append(False)
        print('Frandral vencedor')

print('Terceira disputa')
inimigo = random.randint(0, 1)

if inimigo == 1:
    result.append(False)
    print('Hogum venceu')
else:
    result.append(True)
    print('Loki venceu')

print('Quarta disputa')
loki = []
inimigo = []

for i in range(12):
    if len(inimigo) > 1:
        if inimigo[0] == inimigo[1]:
            result.append(False)
            print('Valquiria venceu')
            break
        else:
            for i in range(2):
                inimigo.pop()
    else:
        inimigo.append(random.randint(0, 20))
    if len(loki) > 1:
        if loki[0] == loki[1]:
            result.append(True)
            print('Loki venceu')
            break
        else:
            for i in range(2):
                loki.pop()
    else:
        loki.append(random.randint(1, 20))
    if i == 10:
        result.append('empate')
        print('Empate')

print('Quinta dispsuta')
loki = 0
inimigo = 0
play = True
scoreCurrentLoki = 0
scoreCurrentInimigo = 0

for i in range(6):
    scoreValue = 0
    loki = random.randint(1, 20)
    inimigo = random.randint(1, 20)

    if play:
        print('Loki atacou')
        if loki == inimigo or loki%2 == inimigo%2:
            print('Lady Sif desviou')
            play = False
        else:
            print('Loki acertou um ataque')
            scoreCurrentLoki+=1
            play = False
    else:
        print('Lady Sif atacou')
        if inimigo == loki or inimigo%2 == loki%2:
            print('Loki desviou')
            play = True
        else:
            print('Lady Sif acertou um ataque')
            scoreCurrentInimigo+=1
            play = True

print('Loki:', scoreCurrentLoki, 'Lady Sif:', scoreCurrentInimigo)
if scoreCurrentLoki > scoreCurrentInimigo:
    print('Loki venceu')
    result.append(True)
else:
    if scoreCurrentLoki == scoreCurrentInimigo:
        print('empate')
        result.append('empate')
    print('Lady Sif venceu')
    result.append(False)

print('Disputa finalizada')
print(result)
if result.count(True) >= 3:
    print('loki foi escolhido para defender Asgard')
else:
    print('Devido a certos acontecimentos no sistema Loki foi escolhido para defender Asgard')