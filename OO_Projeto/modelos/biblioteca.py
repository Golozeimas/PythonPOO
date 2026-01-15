from OO_Projeto.itens.item_biblioteca import Item_biblioteca

class Biblioteca:
    bibliotecas = []
    def __init__(self,nome_da_biblioteca, localizacao, ativa):
        Biblioteca.bibliotecas.append(self) # adiciona o próprio objeto dentro
        self.nome_da_biblioteca = nome_da_biblioteca
        self.localizacao = localizacao
        self.__ativa = ativa
        self.lista_de_itens = []
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
    
    def adiciona_item(self, item):
        if isinstance(item, Item_biblioteca): # isInstance é usado para saber se um
            self.lista_de_itens.append(item)  # determinado item herda de uma classe mãe
    
    def exibir_lista(self):
        print(f"itens da biblioteca: {self.nome_da_biblioteca}")
        for i,item in enumerate(self.lista_de_itens, start=1):
            print(f"item de número: {i} -")
            if hasattr(item, "isbn"):
                msg_livro = f"Livro -> Titulo - {item.titulo}, Autor - {item.autor}, Páginas - {item.paginas}, Preço - {item.preco} e ISBN - {item.isbn}"
                print(msg_livro)
            else:
                msg_revista = f"Revista -> Titulo - {item.titulo}, Autor - {item.autor}, Páginas - {item.paginas}, Preço - {item.preco} e Edição - {item.edicao}"
                print(msg_revista)
            
            """
            o enumerate serve para revelar o index de uma lista, e o start
            para startar de um determina indice, como o enumerate começa do 0
            então colocamos para começar do 1
            """