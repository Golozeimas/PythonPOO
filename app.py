from OO_Projeto.modelos.biblioteca import Biblioteca
from OO_Projeto.modelos.avaliacao import Avaliacao

biblioteca = Biblioteca("Biblioteca de Teresina", "Teresina - PI", True)

biblioteca.alterna_estado()

avaliacao = Avaliacao("Matheus")


def main():
    avaliacao.avaliar()
    avaliacao.media_das_avaliacoes()

if __name__ == "__main__":
    main()