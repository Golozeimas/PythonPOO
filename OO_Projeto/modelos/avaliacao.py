class Avaliacao:
    nota = []
    nome_cliente = 0
    def __init__(self, nome_cliente):
        self.nome_cliente = nome_cliente
    
    def avaliar(self):
        print(f"O avaliador - {self.nome_cliente}")
        notas = int(input("Quantas avaliações para a biblioteca:\n"))
        i = 0
        while i < notas:
            i += 1
            nota = float(input(f"Nota - {i}:\n"))
            if nota > 10 or nota < 0:
                raise ValueError("Não podemos colocar notas menores que 0 ou maior que 10")
            self.nota.append(nota) # adiciona na lista, não podemos esquecer disso

    def media_das_avaliacoes(self):
        if 1 == len(self.nota):
            print(self.nota)
        notas = sum(self.nota) # soma todos os elementos das listas
        media = notas/ len(self.nota)
        print(f"Média das notas: {media}")