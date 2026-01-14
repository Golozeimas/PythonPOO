class Pessoa:
    def __init__(self, idade):
        self.__idade = idade
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter # (nome do property.setter) tem que ter o mesmo nome pra modificar
                  # sem precisar do '()'
    def idade(self, valor):
        if valor < 0:
            raise ValueError ("Digite uma idade válida!")
        else:
            self.__idade = valor
    
pessoa1 = Pessoa(13)

# uso do GETTER para pegar a idade de 13 anos
print(pessoa1.idade)

pessoa1.idade = 20

print(pessoa1.idade)

# dá erro por ter -1 de idade, isso é o uso do SETTER
pessoa1.idade = -1
