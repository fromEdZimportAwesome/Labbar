def rektangel(spaces,rows,columns,sign):
    for i in range(rows):
        print(spaces*' ' + columns*sign)

def ram(rows, columns, thickness, sign):
    for i in range(rows):
        if thickness < i + 1 and rows - i > thickness:
            print(thickness*sign + (columns-2*thickness)*' ' + thickness*sign)
        else:
            print(columns*sign)

def triangelBasUpp(distance, base):
    while base >= 1:
        print(distance*' ' + base*'*')
        base -= 2
        distance += 1

def triangelBasNed(distance, base):
    counter = 1
    distancecount = distance + int((base+1)/2 - 1)
    while counter <= base:
        print(distancecount*' ' + counter*'*')
        counter += 2
        distancecount -= 1

def romb(spaces, base):
    triangelBasNed(spaces, base)
    triangelBasUpp(spaces + 1, base - 2)



def triangelBasUpp2(distance, base):
    returvärde = ''
    while base >= 1:
        returvärde += distance*' ' + base*'*' + '\n'
        base -= 2
        distance += 1
    return returvärde

def triangelBasNed2(distance, base):
    counter = 1
    distancecount = distance + int((base+1)/2 - 1)
    returvärde = ''
    while counter <= base:
        returvärde += distancecount*' ' + counter*'*' + '\n'
        counter += 2
        distancecount -= 1
    return returvärde

def romb2(spaces, base):
    y = triangelBasNed2(spaces, base)
    x = triangelBasUpp2(spaces + 1, base - 2)
    return y + x
