vokaler = 'AOUÅEIYÄÖaouåeiyäö'
konsonanter = 'BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz'

def viskspråket(mening):
    översatt = ''
    for letter in mening:
        if letter not in vokaler:
            översatt += letter
    print(översatt)

def rövarspråket(mening):
    översatt = ''
    for letter in mening:
        if letter in konsonanter:
            översatt += '{0}o{0}'.format(letter)
        else:
            översatt += letter
    print(översatt)

def bebisspråket(mening):
    översatt = ''
    lista = mening.split()
    for ord in lista:
        for bokstav in ord:
            if bokstav in vokaler:
                översatt += ord[:ord.index(bokstav) + 1]*3 + ' '
                break
    print(översatt)

def allspråket(mening):
    översatt = ''
    lista = mening.split()
    for ord in lista:
        for bokstav in ord:
            if bokstav in vokaler:
                översatt += ord[ord.index(bokstav):] + ord[:ord.index(bokstav)] + 'all '
                break
    print(översatt)

def fikonspråket(mening):
    översatt = ''
    lista = mening.split()
    for ord in lista:
        for bokstav in ord:
            if bokstav in vokaler:
                översatt += 'fi' + ord[ord.index(bokstav) + 1:] + ord[:ord.index(bokstav) + 1] + 'kon '
                break
    print(översatt)

