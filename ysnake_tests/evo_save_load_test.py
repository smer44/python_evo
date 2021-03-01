'''
Created on 26.02.2021

Test of  evo Population save and load 

TODO: split EvoController on PopData and EvoModell 

@author: peter
'''

from ysnake_old.evo_controller import EvoController



ec = EvoController(2, 2,3,1)

other = EvoController(2, 2,3,1)

iseq = ec.eq(other)

print(iseq)

ec.save()

other.load()

iseq = ec.eq(other)

print(iseq)

print(ec.weights)

print(other.weights)