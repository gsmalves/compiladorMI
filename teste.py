file = open('entrada1.txt', 'r')
fita = []

for linha in file.readlines():
    fita.append([x for x in linha])
    fita.append([])
    file.close()
    print(fita)