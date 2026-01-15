# pensamos no mais abstrato possivel para um item de uma biblioteca
# o que pode ter em todos esses itens de uma biblioteca

from abc import ABC, abstractmethod

class Item_biblioteca(ABC):
    def __init__(self, titulo, autor, paginas, preco):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.preco = preco
    
    @abstractmethod
    def aplica_desconto(self):
       pass