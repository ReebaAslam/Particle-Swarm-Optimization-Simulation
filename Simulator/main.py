from swarm import swarm
from random import randint
from particle import particle

randC=lambda : [randint(0,255),randint(0,255),randint(0,255),randint(0,255)]
randP=lambda bound: [randint(0,bound[0]),randint(0,bound[1])]

defaultCol=[255,100,10,255]


class main():
    def __init__(self,count,dest, bound,W,c1,c2):
        self.swarms=[]
        self.particles=[]
        self.nSwarms=len(dest)
        self.bound=bound
        self.singCol=True
        for i in range(self.nSwarms):
            parts=[]
            for n in range(count/self.nSwarms):
                pos=[i*30,n*30]
                temp=particle(randP(bound),dest[i],bound)
                self.particles.append(temp)
                parts.append(temp)
            self.swarms.append(swarm(count/self.nSwarms,parts,defaultCol,dest[i],W,c1,c2))

        
    def run(self,show,take):
        s=self.swarms
        if take==False:
            for i in range(self.nSwarms):
                s[i].updateGBest()
                s[i].moveParticles()
            self.display(show)
            
    def display(self,show):
        # background(2,6,83)
        for i in range(self.nSwarms):
            if show==True:
                fill(225,33,235)
                ellipse(self.swarms[i].dest[0], self.swarms[i].dest[1],20,20)
            r=self.swarms[i].col[0]
            g=self.swarms[i].col[1]
            b=self.swarms[i].col[2]
            a=self.swarms[i].col[3]
            # r,g,b,a=255,100,10,255
            for n in self.swarms[i].particles:
                fill(r,g,b,a) 
                ellipse(n.pos[0],n.pos[1],10,10)
                a=randint(0,255)
            
    def updateShape(self,shp):
        n=len(self.particles)/len(shp)
        m=0
        for i in range(len(shp)):
            sys=0
            if i<len(self.swarms):
                sys=self.swarms[i]
                sys.dest=shp[i]
                sys.particles=self.particles[m:n*(i+1)]
                
            else:
                parts=self.particles[m:n*(i+1)]
                col=defaultCol
                if self.singCol==False:
                    col=randC()
                W,c1,c2=self.swarms[-1].W,self.swarms[-1].c1,self.swarms[-1].c2
                self.swarms.append(swarm(n,parts,col,shp[i],W,c1,c2))
                sys=self.swarms[i]
                
            for p in sys.particles:
                p.fit=p.fitness(sys.dest)
                p.pBest=p.pos
                p.pBestFit=p.fit 
            gBest=sys.particles[randint(0,len(sys.particles)-1)]
            sys.gBestFit=gBest.fit
            sys.gBestPos=gBest.pos
            sys.updateGBest()
            m+=n
        self.nSwarms=len(shp)
    
    def changeColor(self,k):
        if k==0:
            if self.singCol==False:
                for i in self.swarms:
                    i.col=defaultCol
                self.singCol=True
        else:
            if self.singCol==True and self.nSwarms>1:
                for i in self.swarms:
                    i.col=randC()
                self.singCol=False
    
    def changeInertia(self,val):
        for i in self.swarms:
            i.W=val
    
    def changeC1(self,val):
        for i in self.swarms:
            i.c1=val
    
    def changeC2(self,val):
        for i in self.swarms:
            i.c2=val    
    
    def changePCount(self,val):
        total=val
        perSwarm=total/self.nSwarms
        if len(self.particles)<total:
            self.particles=self.particles[:total]
        elif len(self.particles)>total:
            curr=len(self.particles)
            bound=self.particles[-1].bound
            for i in range(total-curr):
                self.particles.append(particle(randP(bound),dest[i],bound))
        m=0
        n=perSwarm
        for i in range(self.nSwarms):
            self.swarms[i].particles=self.particles[m:n]
            self.swarms[i].pCount=n-m
            m+=n
            n+=n
            
            
            
            
        
