class Game:
    gameName = ""
    yearLaunch = 0
    note = 0.0
    multiplayer = False

    def __init__(self, gameName, yearLaunch, note, multiplayer):
        self.gameName = gameName
        self.yearLaunch = yearLaunch
        self.note = note
        self.multiplayer = multiplayer
    
    def substitui_os_dados(self):
        self.gameName = input("Coloque o nome do jogo:\n")
        self.note = float(input("Coloque a nota do jogo:\n"))
        self.yearLaunch = int(input("Coloque o ano de lançamento do jogo:\n"))
        print(f"- nome do jogo: {self.gameName},\n- nota do jogo: {self.note}\n e ano de lançamento: {self.yearLaunch}")
            
    def __str__(self):
        return f"- nome do jogo: {self.gameName},\n- nota do jogo: {self.note}\n e ano de lançamento: {self.yearLaunch}"
    
# essa é a assinatura da classe para herança
class SinglePlayGame(Game):
    def __init__(self, gameName = "", yearLaunch = 0, note = 0.0, multiplayer = False, storyline = ""):
        # esse super serve para utilizar dados da classe mãe
        super().__init__(gameName, yearLaunch, note, multiplayer)
        self.storyline = storyline
    
    # isso se chama sobre escrita, fazendo alterações específicas para
    # a nossa subclasse
    def substitui_os_dados(self):
        # esse super serve para utilizar dados da classe mãe
        super().substitui_os_dados()
        self.storyline = input("Coloque o enredo do jogo:\n")
        print(f"\nenredo: {self.storyline}")
    

multi_game = Game("Fortnite", 2017, 7, True)
print(multi_game)

single_game1 = SinglePlayGame("Dark souls 3", 2016, 10, False, "Você sairá em uma aventura em lothric tentando acender a fogueira final")
single_game1.substitui_os_dados()