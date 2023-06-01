class Versenyzo:
    def __init__(self, row) -> None:
        splitted = row.strip().split(';')
        self.nev = splitted[0]
        self.rajtszam = splitted[1]
        self.kategoria = splitted[2]
        self.versenyido = splitted[3]
        # self.versenyido = self.ido[1] + self.ido[2] * 60
        self.tavSzazalek = int(splitted[4])
    
    def IdőÓrában(self):
        splitted = self.versenyido.split(':')
        ora = int(splitted[0])
        perc = int(splitted[1])
        masodperc = int(splitted[2])
        return ora + perc/60 + masodperc/3600 