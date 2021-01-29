from game import * 


conf = GameMapConfig(10,10,600,600)


gmap = GameMap(conf)


pp = PPrinter()



ev = Clock([pp])




game = Game("game_test", gmap, [ev])


game.step()

game.loop(10)
#TOOD - wait and then call step again