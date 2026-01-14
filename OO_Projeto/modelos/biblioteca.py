class Biblioteca:
    bibliotecas = []
    def __init__(self,nome_da_biblioteca, localizacao, ativa):
        Biblioteca.bibliotecas.append(self) # adiciona o próprio objeto dentro
        self.nome_da_biblioteca = nome_da_biblioteca
        self.localizacao = localizacao
        self.__ativa = ativa

    def __str__(self):
        return f"A {self.nome_da_biblioteca} é localizada em {self.localizacao}, e no momento está {self.__ativa}"
    
    
    def listar_bibliotecas():
        for bili in Biblioteca.bibliotecas: # não precisa do self desse modo
            print(bili)
    
    def alterna_estado(self):
        self.__ativa = not self.__ativa

    @property
    def ativa(self):
        return "Está ativada a {self.nome_da_biblioteca}" if self.__ativa == True else "Está desativada"

biblioteca = Biblioteca("Biblioteca de são jóse", "São Jóse - PI", True)

print(biblioteca)

biblioteca2 = Biblioteca("Biblioteca de Teresina", "Teresina - PI", True)

Biblioteca.listar_bibliotecas() # serve de referência pra o método

# esse vars é usado quando queremos que retorne em formato de dicionário as váriaveis
print(vars(biblioteca))