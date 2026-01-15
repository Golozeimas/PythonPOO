from OO_Projeto.itens.item_biblioteca import Item_biblioteca

class Revista(Item_biblioteca):
    def __init__(self, titulo, autor, paginas, edicao, preco):
        super().__init__(titulo, autor, paginas, preco)
        self.edicao = edicao
    
    def aplica_desconto(self):
        # 15% de desconto
        desconto = (self.preco * 15/100)
        valor_descontado = self.preco - desconto
        print(f"valor após desconto de 15%: {valor_descontado}")
        self.preco = valor_descontado