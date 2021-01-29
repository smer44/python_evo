import time





class EventSource:
    
    def __init__(self,  listeners):
        self.listeners =  listeners
        
        
    def data(self):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        
        
        return "EventSource : " + str(current_time)
    
        
    def send(self):
        
        for listener in self.listeners:
            listener.receive(self.data())
            
            
    def step(self):
        raise Exception('EventSource.step called but is abstract ')    
        


class PPrinter:
    
    def __init__(self):
        pass 
    
    def receive(self,data):
        print("PPrinter : " , str(data))



class MapConverter:
    
    cellobjtype = {1:"grass"}   
    
    cellobjtypebk = {"grass" : 1}  
    
    
    def nameToCellObj(self,typename):
        
        return CellObject(self.cellobjtypebk[typename])
    
    
    def CellObjToName(self,cellobj):
        return self.cellobjtype[cellobj.id]
 
    
class CellObject:
    
    
    def __init__(self,id):
        self.id = id 
        
    
    
    

class Clock(EventSource):
    
    def __init__(self, listeners, startTime = 0, lastTimeStamp = 0):    
        super().__init__(listeners)
        self.startTime = startTime
        self.lastTime = 0 
        self.lastTimeStamp = lastTimeStamp
        
        
    def step(self):
        self.send()


class Game:
    
    
    def __init__(self, id, gamemap, activeObjects):
        
        self.id = id       
        self.gamemap = gamemap
        
        self.activeObjects = activeObjects
        self.sleep_time = 0.5
        
        #turn on event processors
        
    def step(self):
        for obj in self.activeObjects:
            obj.step()
        
        
    def on_render(self):
        pass 
        
    def loop(self,loops):
        
        for self.count in range(loops):
            self.step() 
            self.pause_after_step()
            
        
    def pause_after_step(self):
            time.sleep(self.sleep_time)
        
class GameMapConfig:
    
    def __init__(self, widthInCells, heightInCells, pixWidth, pixHeigth ):   
        self.heightInCells = heightInCells
        self.widthInCells = widthInCells
        self.widthOfCell = pixWidth / widthInCells
        self.heigthOfCell = pixHeigth / heightInCells
        self.pixWidth = pixWidth
        self.pixHeigth = pixHeigth
        
    def __str__(self):
        return "GameMapConfig : "
        


class GameMap:
    
    def __init__(self, conf):
        
        self.conf = conf    
        
    
    def init_empty_2d(self):
        dx = self.conf.heightInCells
        dy = self.conf.widthInCells
        
        self.grid = [[None for _ in range(dx) ] for _ in range(dy) ]
        
        
        
        
        
        