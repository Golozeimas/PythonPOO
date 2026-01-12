class Game:
    gameName = ""
    yearLaunch = 0
    note = 0.0
    multiplayer = False

    # substitui o print(obj), podendo printar direto do objeto, sem precisar de acesso diret+o
    def __str__(self):
        return f"- nome do jogo: {self.gameName},\n- nota do jogo: {self.note}\n e ano de lançamento: {self.yearLaunch}"
    
    # faz o papel do construtor como no JAVA, só é que aqui é chamado de init
    def __init__(self, gameName="",yearLaunch=0, note=0.0, multiplayer=False):
        self.gameName = gameName
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note

# criando um objeto depois desse métodos especiais
game1 = Game("Demons Souls Remake", 2020, 10, True)

print(game1)