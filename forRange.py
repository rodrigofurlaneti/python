corredores = {}
voltas = {}
result = {}
total = 0
while True:
    for j in range(6):
        corredor = input('Digite nome do corredor: ')
        for i in range(10):
            volta = int(input ('Digite o tempo em segundos: '))
            if corredor != "" and volta!= "":
                corredores [corredor] = [volta]
                voltas [i] = [volta]
                total += volta
                print (corredores)
                #print (voltas)
                #print (total)
            result [i] = [total]
        print (result[len(result)-1])
