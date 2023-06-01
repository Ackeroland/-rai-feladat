from versenyzo import *

versenyzok:list[Versenyzo] = []

file = open('ub2017egyeni.txt', 'r', encoding='utf-8')
file.readline()
for row in file:
    versenyzok.append(Versenyzo(row))
file.close()

print(f'3.2 feladat: Futók száma: {len(versenyzok)}')

nok = 0
for row in versenyzok:
    if row.kategoria == 'Noi'and row.tavSzazalek == 100:
        nok += 1

print(f'4. feladat: Célba érkező női sportolók: {nok} fő')

leghosszabb_nevu = versenyzok[0]

for item in versenyzok:
    if len(item.nev) > len(leghosszabb_nevu.nev):
        leghosszabb_nevu = item


