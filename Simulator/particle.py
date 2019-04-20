import math
from random import randint

class particle():
    def __init__(self,pos,dest,bound):
        self.pos=pos
        self.pBest=self.pos
        self.pBestFit=0
        self.fit=self.fitness(dest)
        self.velocity= [randint(-50,50),self.pos[1]+randint(-50,50)]
        self.bound=bound
    
    def fitness(self,dest):
        curr=self.pos
        # dest=self.dest
        fit=math.sqrt((curr[0]-dest[0])**2+(curr[1]-dest[1])**2)
        if fit<self.pBestFit:
            self.pBestFit=fit
            self.pBest=self.pos
        return fit
        # return (curr[0]-dest[0])**2
    
    def move(self):
        bound=self.bound
        if self.fit>5:
            self.pos=[self.pos[0]+self.velocity[0],self.pos[1]+self.velocity[1]]
            #wrapping around
            if self.pos[0]>bound[0]:
                self.pos[0]=bound[0]-(self.pos[0]-bound[0])
            elif self.pos[0]<0:
                self.pos[0]=bound[0]+self.pos[0]
            if self.pos[1]>bound[1]:
                self.pos[1]=bound[1]-(self.pos[1]-bound[1])
            elif self.pos[1]<0:
                self.pos[1]=bound[1]+self.pos[1]



    
    
