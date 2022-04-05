#marvel.py


#classe mãe genérica
class Heroi:

    def __init__(self, nome):
        self.nome = nome

    def voar(self):
        print(f'{self.nome} Voando...')

    def levantarPeso(self):
        print(f'{self.nome} Levantando um caminhão')
        
    def destruir(self):
        print(f'{self.nome} Destruir armas do inimigos')

    def salvar(self):
        print(f'{self.nome} Salvando pessoas...')


#Thor é um Herói
class Thor(Heroi):
    def __init__(self):
        super().__init__('Thor')

    def jogarMartelo(self):
        print('Thor jogando Martello...')


class Ironman(Heroi):
    def __init__(self):
        super().__init__('IronMan')

    def chamarDrones(self):
        print('Chamar drones com armas')


class Shazam(Heroi):
    def __init__(self):
        super().__init__('Shazam')

    def trasformando(self):
        print('Shazam!!!')



thor = Thor()
thor.voar()
thor.levantarPeso()
thor.destruir()
thor.salvar()
thor.jogarMartelo()

ironman = Ironman()
ironman.voar()
ironman.levantarPeso()
ironman.destruir()
ironman.salvar()
ironman.chamarDrones()

shazam = Shazam()
shazam.voar()
shazam.levantarPeso()
shazam.destruir()
shazam.salvar()
shazam.trasformando()
