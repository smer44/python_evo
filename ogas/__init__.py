

class СommoditySupply:

    def __init__(self, name, brange, time, quantity, local_storage ):
        self.name = name 
        self.brange = brange 
        self.time =  time
        self.quantity = quantity 
        self.buy_motivation = 1
        
        

class Consumer:
    
    def __init__(self, comms):
        self.comms = comms 
        
    
    def step(self):
        for comm in self.comms:
            comm.interval_time -=1
            if not comm.interval_time:
                # consume:
                self.local_storage -= self.one_consume_quantity
                if (self.local_storage < 0):
                    
                
        
        


        


