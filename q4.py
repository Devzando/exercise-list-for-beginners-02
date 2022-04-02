stop = True
peoplesAgeIquals = []
allM = []
allF = []
ageIquals = False
lengthPeoplesM = 0

while stop:
    newPeople = []
    print('informe o seu nome')
    name = str(input())
    newPeople.append(name)
    print('informe a sua idade')
    age = int(input())
    newPeople.append(age)
    print('informe o seu sexo. 1 para M, 2 para F')
    sex = int(input())

    while sex > 2 or sex < 1:
        print('valor não permitido, informe novamente')    
        sex = int(input())
    newPeople.append(sex)

    if sex == 1:
        allM.append(newPeople)
    else:
        allF.append(newPeople)

    print('Deseja adicionar mais pessoas? 1 para sim, 2 para não')
    choose = int(input())

    while choose > 2 or choose < 1:
        print("valor não permitido, informe novamente")
        choose = int(input())

    if choose == 1:
        stop = True
    else:
        stop = False



if len(allM) >=1:
    peopleM = allM[0][1]
    for i in range(len(allM)):
        if peopleM > allM[i][1]:
            peopleM = allM[i][1]
        else:
            if peopleM == allM[i][1] and i != 0:
                print('teste')
                ageIquals = True
            peopleM = peopleM


if len(allF) >=1:
    peopleF = allF[0][1]
    nameF = allF[0][0]
    for i in range(len(allF)):
        if peopleF > allF[i][1]:
            peopleF = peopleF
            nameF = nameF
        else:
            if peopleF == allF[i][1] and i != 0:
                print('teste')
                if nameF not in peoplesAgeIquals and allF[i][0] not in peoplesAgeIquals:
                    peoplesAgeIquals.append(nameF)
                    peoplesAgeIquals.append(allF[i][0])          
            peopleF = allF[i][1]
            nameF = allF[i][0]
    

if ageIquals:
    print('existe dois homens com a mesma idade:', peopleM)
else:
    if len(allM) < 1:
        print('Não foram encontrados homens')
    else:
        print('A menor idade encontrada entre os homens é', peopleM)

if len(peoplesAgeIquals) >= 1:
    print('Tem duas mulheres mais velhas com a mesma idade')
    print('Seus nomes São:')
    for i in peoplesAgeIquals:
        print(i)
else:
    if len(allF) < 1:
        print('Não foram encontradas mulheres')
    else:
        print('O nome da mulher mais velha é', nameF)