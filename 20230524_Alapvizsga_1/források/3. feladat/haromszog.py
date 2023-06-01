print('1. feladat: a haáromszög szerkeszthetősége')
print('Kérem a háromszög oldalait!')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and b +c > a and a +c > b:
    print('A háromszög szerkeszthető.')
else:
    print('A háromszög nem szerkeszthető a megadott adatokkal.')