from OO_Projeto.modelos.biblioteca import Biblioteca
from OO_Projeto.modelos.avaliacao import Avaliacao
from OO_Projeto.itens.revista import Revista
from OO_Projeto.itens.livros import Livro


biblioteca = Biblioteca("Biblioteca de Teresina", "Teresina - PI", True)

biblioteca.alterna_estado()

avaliacao = Avaliacao("Matheus")


def main():
    # avaliacao.avaliar()
    # avaliacao.media_das_avaliacoes()
    revista1 = Revista("National Geographyc", "BBC", 320, "Quinta edição", 120)
    livro1 = Livro("1984", "George Orwell", 1200, "022-2323-2", 100)
    
    biblioteca.adiciona_item(livro1)

    biblioteca.adiciona_item(revista1)

    livro1.aplica_desconto()

    revista1.aplica_desconto()
    
    biblioteca.exibir_lista()

    # print(vars(revista1))
    # print(vars(livro1))
if __name__ == "__main__":
    main()