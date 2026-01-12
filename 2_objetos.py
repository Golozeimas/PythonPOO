class Game:
    gameName = ""
    yearLaunch = 0
    note = 0.0
    multiplayer = False

# 1 - criando o primeiro jogo
game1 = Game() # usamos Game() como função em uma variável para entrar no atributo ou método
# endereço de memória do objeto {print(game1)} 
game1.gameName = "Star wars jedi fallen order"
game1.yearLaunch = 2019
game1.note = 9.5
game1.multiplayer = False

print(f"Esse jogo: {game1.gameName},\né nota: {game1.note},\ne o seu ano de lançamento: {game1.yearLaunch}")

print("")
# 2 - criando o segundo jogo
game2 = Game()

game2.gameName = "Devil may cry 5"
game2.yearLaunch = 2019
game2.multiplayer = False
game2.note = 9

print(f"Esse jogo: {game2.gameName},\né nota: {game2.note},\ne o seu ano de lançamento: {game2.yearLaunch}")

