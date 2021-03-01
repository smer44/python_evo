def histo_to_xy(histo,population_size):
    tuples = histo.items()
    tuples = sorted(tuples, key = lambda t: t[0])
    xx = [ t[0] for t in tuples]
    yy = [ t[1]/population_size for t in tuples]#divide to normalize it 
    return xx,yy
     
     
     
