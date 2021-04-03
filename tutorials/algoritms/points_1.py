'''
Created on 17.03.2021

@author: peter
'''
lines = [[4, 7],
[1 ,3],
[2 ,5],
[5 ,6],
]

lines1 = [[5, 6],
[4 ,7],
[3 ,8],
[2 ,9],
[1,10]
]

answer_1 = (1, '6')


"""
5
5 6
4 7
3 8
2 9
1 10

------
1
6 
 

5
1 2
2 3
3 4
4 5
5 6

_______
3
2 4 6 

 

5
1 2
3 4
5 6
7 8
9 10

________
5
2 4 6 8 10 


"""


 

lines = sorted(lines, key = lambda line : line[1])

old_point = -1 

points = []

for l, r in lines :
    if l > old_point:
        old_point = r 
        points.append(old_point)
        
print(len(points)) 

print( ' '.join(str(p) for p in points))


    
