from csmodel.basic import *


run = action("run", active= True)


lay = action ("lay",active= False)

print(repr(run))

print(repr(lay))


dog = aliveobj("dog", active= True)


stone = object("stone",active= False)

print(repr(dog))

print(repr(stone))


dog_can_run = can_relation("dog_can_run", subject = dog, action = run)

assert dog_can_run

print(dog_can_run)

print(dog_can_run.check())

print(dog_can_run.fstr())


stone_can_run = can_relation("stone_can_run", subject = stone, action = run)

assert not stone_can_run

print(stone_can_run.check())
print(stone_can_run.fstr())





