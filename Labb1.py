def cubesum():
    while True:
        a = int(input('Skriv in ett heltal: '))
        b = int(input('Skriv in ett till heltal: '))
        print('kubsumman av {} och {} är {}'.format(a,b,a**3 + b**3))

def ramujan1():
    n = int(input('Ange ett positivt heltal: '))
    resultat = ramujan2(n)
    if resultat == []:
        print('Det gick inte att hitta någon lösning')
    else:
        print('Kubsumman av talparet/talparen', resultat, 'ger talet', n)

def ramujan2(n):
    b = 0
    a = 0
    resultat = []
    while b <= a and b < round(n**(1/3)):
        a = (n - b ** 3) ** (1 / 3)
        if len(resultat) == 2:
            break
        elif round(a)**3 + b**3 == n:
            resultat.append((round(a),b))
            b += 1
        else:
            b += 1
    if resultat == []:
        return []
    else:
        return resultat
ramujan1()