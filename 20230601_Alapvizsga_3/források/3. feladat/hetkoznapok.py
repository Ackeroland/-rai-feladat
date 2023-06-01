def maganhangzokSzama(nap):
    maganhangzok = 'aáeéiíoóöőuúüű'
    darab = 0
    for item in nap:
        if item in maganhangzok:
            darab += 1
    return darab

napok = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']


legtobb = napok[0]
for item in napok:
    if maganhangzokSzama(legtobb) < maganhangzokSzama(item):
        legtobb = item

print(F'A legtöbb magánhangzó a {legtobb}-ben van.')