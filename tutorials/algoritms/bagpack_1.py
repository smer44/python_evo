"""
bagpack  problem 
Sample Input:

3 50
60 20
100 50
120 30
Sample Output:

180.000"""

w = 50
items = [(60,20),(100,50),(120,30)]

items = sorted(items, key = lambda cw: cw[0]/cw[1], reverse=True)# sort biggest first 

bagpack = 0

for ci,wi in items:
    if w <= 0 : break 
    amount = min(wi,w)
    costs = ci/wi*amount 
    bagpack += costs 
    w = w - amount

print(bagpack) 
    
