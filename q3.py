import random
from tkinter.colorchooser import Chooser

allRandomValues = []
stop = True
valueRandomCurrent = 0

while stop:
    if len(allRandomValues) == 2:
        stop = False

    valueRandomCurrent = random.randint(0, 30)
    while valueRandomCurrent in allRandomValues:
        valueRandomCurrent = random.randint(0, 30)

    allRandomValues.append(valueRandomCurrent)

print('Escolha uma das 3 terras listadas asseguir')

stop = True
while stop:
    for i in allRandomValues:
        print(i)
    choose = int(input())
    if choose in allRandomValues:
        stop = False
    else:
        print('Essa terra não existe, escolha novamente')
    

print('Você escolheu a terra', choose)