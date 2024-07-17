class Robo:

    def __init__(self, nome, bateria=100, habilidades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nome(self):
        return self.__nome
    
    @property
    def bateria(self):
        return self.__bateria
    
    @property
    def habilidade(self):
        return self.__habilidades
    
    def carregar(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'BEEP BOOP BEEP BOOP. EU SOU {self.__nome.upper()}'
        return 'Bateria Fraca. Por favorm recarregue e tente novamente'
    
    def aprendedr_habilidade(self, nova_habilidade, custo):
        if self.__bateria >= custo:
            self.__bateria -= custo
            self.__habilidades.append(nova_habilidade)
            return f'Uau eu aprendi {nova_habilidade.upper()}'
        return 'Bateria insuficiente. Por Favor, recarregue e tente novamente'
