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

class StudioGame:
    def __init__(self, nome_do_estudio):
        self.nome_do_estudio = nome_do_estudio
        self.jogos_lancados = []
    
    def adiciona_jogo(self,game):
        self.jogos_lancados.append(game)

    def media_do_estudio(self):
        # pegue as notas dos jogos para cada game em jogos_lancados
        notas = sum(game.note for game in self.jogos_lancados)
        jogos = len(self.jogos_lancados)

        if jogos == 0:
            print("Não existe jogos da empresa")
        else:
            media = notas / jogos
            print(f"Essa é média do estudio: {media:.2f}")
    
    def lista_jogos(self):
        for game in self.jogos_lancados:
            print(game)


studio = StudioGame("Avalanche")

game1 = Game("Dark souls", 2008, 10, True)
game2 = Game("Dark souls 2", 2013, 8, True)
game3 = Game("Dark souls 3", 2016, 9.5, True)

studio.adiciona_jogo(game1)
studio.adiciona_jogo(game2)
studio.adiciona_jogo(game3)

studio.media_do_estudio()

studio.lista_jogos()