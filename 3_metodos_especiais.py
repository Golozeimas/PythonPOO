class Game:
    gameName = ""
    yearLaunch = 0
    note = 0.0
    multiplayer = False
    total_games = 0

    # substitui o print(obj), podendo printar direto do objeto, sem precisar de acesso diret+o
    def __str__(self):
        return f"- nome do jogo: {self.gameName},\n- nota do jogo: {self.note}\n e ano de lançamento: {self.yearLaunch}"
    
    # faz o papel do construtor como no JAVA, só é que aqui é chamado de init
    def __init__(self, gameName="",yearLaunch=0, note=0.0, multiplayer=False):
        self.gameName = gameName
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        Game.total_games += 1
        self.note = note
        self.notas = 0.0
        self.avaliacao = 0

    def substitui_os_dados(self):
        self.gameName = input("Coloque o nome do jogo:\n")
        self.note = float(input("Coloque a nota do jogo:\n"))
        self.yearLaunch = int(input("Coloque o ano de lançamento do jogo:\n"))
        print(f"- nome do jogo: {self.gameName},\n- nota do jogo: {self.note}\n e ano de lançamento: {self.yearLaunch}")    

    def nota_do_jogo(self, note):
        self.notas += note
        self.avaliacao += 1
    
    def media_das_notas(self):
        print(f"Nome do jogo: {self.gameName}, sua média de notas:{self.notas / self.avaliacao:.2f}")

# criando um objeto depois desse métodos especiais
"""
game1 = Game("Demons Souls Remake", 2020, 10, True)
print(game1)
"""
game1 = Game("Demons Souls Remake", 2020, 10, True)
# notas e média
game1.nota_do_jogo(6)
game1.nota_do_jogo(7)
game1.nota_do_jogo(10)
game1.media_das_notas()

game2 = Game("Dark souls", 2013, 10, True)

# usando variável de instância para contar o número de jogos
print(f"Números total de jogos: {Game.total_games}")