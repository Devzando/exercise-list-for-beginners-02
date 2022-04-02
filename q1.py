import random

flashAll = [
    ['jesse quick'],
    ['barry allen'],
    ['wally west'],
    ['dr. wells'],
    ['jay garrick'],
    ['max mercury']
]
allRandomValues = []

idx = 0
valueCurrent = 0
stop = True

while stop:
    if idx < 6:
        valueCurrent = random.randint(1, 6)
        while valueCurrent in allRandomValues:
            valueCurrent = random.randint(1, 6)
        
        allRandomValues.append(valueCurrent)
        flashAll[idx].append(valueCurrent * 300000)
    else:
        stop = False
    idx+=1

vel = flashAll[0][1]
venc = flashAll[0][0]


for i in range(6):
    if vel > flashAll[i][1]:
        vel = vel
        venc = venc
    else:
        vel = flashAll[i][1]
        venc = flashAll[i][0]

print('O vencedor da corrida é', venc, 'com uma velocidade de', vel,'km/s')