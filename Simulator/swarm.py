from random import choice, random



class swarm():
    def __init__(self,pCount,particles,col,dest,W,c1,c2):
        self.pCount=pCount
        self.W=W
        self.c1=c1
        self.c2=c2
        self.particles=particles
        gBest=choice(self.particles)
        self.gBestFit=gBest.fit
        self.gBestPos=gBest.pos
        self.col=col
        self.dest=dest
        
    def updateGBest(self):
        for i in self.particles:
            if i.fit<self.gBestFit:
                self.gBestFit=i.fit
                self.gBestPos=i.pos
    
    def moveParticles(self):
        W=self.W
        c1=self.c1
        c2=self.c2
        for i in self.particles:
            curVel=i.velocity
            rand1=random()
            rand2=random()
            newVel=[0,0]
            newVel[0]= W*curVel[0]+rand1*c1*(i.pBest[0]-i.pos[0])+rand2*c2*(self.gBestPos[0]-i.pos[0])
            newVel[1]= W*curVel[1]+rand1*c1*(i.pBest[1]-i.pos[1])+rand2*c2*(self.gBestPos[1]-i.pos[1])
            i.velocity=[newVel[0],newVel[1]]
            # print(curVel,newVel,i.pos)
            i.move()
            i.fit=i.fitness(self.dest)
            # print(i.pos)
            
        
        
