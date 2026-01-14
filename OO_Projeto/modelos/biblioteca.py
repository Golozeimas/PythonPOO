class Biblioteca:
    bibliotecas = []
    def __init__(self,nome_da_biblioteca, localizacao, ativa):
        Biblioteca.bibliotecas.append(self) # adiciona o próprio objeto dentro
        self.nome_da_biblioteca = nome_da_biblioteca
        self.localizacao = localizacao
        self.__ativa = ativa

    def __str__(self):
        return f"A {self.nome_da_biblioteca} é localizada em {self.localizacao}, e no momento está {self.__ativa}"
    
    @classmethod
    def listar_bibliotecas(cls):
        for bili in cls.bibliotecas: # não precisa do self desse modo
            print(bili)
    
    def alterna_estado(self):
        self.__ativa = not self.__ativa

    @property
    def ativa(self):
        return "Está ativada a {self.nome_da_biblioteca}" if self.__ativa == True else "Está desativada"