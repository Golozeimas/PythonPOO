from OO_Projeto.itens.item_biblioteca import Item_biblioteca

class Livro(Item_biblioteca):
    def __init__(self, titulo, autor, paginas, isbn, preco):
        super().__init__(titulo, autor, paginas, preco) # herda tudo que você precisa da classe pai
        self.isbn = isbn
    
    
    def aplica_desconto(self):
        # 10% de desconto
        desconto = (self.preco * 10/100)
        valor_descontado = self.preco - desconto 
        print(f"valor após desconto de 10%: {valor_descontado}")
        self.preco = valor_descontado