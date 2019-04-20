from random import randint
from main import main


W=0.8
c1=0.5
c2=0.8
COUNT=1000
sW=1600
sH=950
DEST=[]
cent=sW/2-200,sH/2



dic={}
show=False
take=False
full=True

over=[False]*4
locked=[False]*4
sliderW=50
sliderH=10
sliders=[[(sW-225),555,sW-350,560,sW-350+300,560]]
for i in range(1,4):
    sliders.append([sliders[i-1][0],sliders[i-1][1]+70,sliders[i-1][2],sliders[i-1][3]+70,sliders[i-1][4],sliders[i-1][5]+70])
sliders[0][0]=1250+(W*250)
sliders[1][0]=1250+(c1*250)
sliders[2][0]=1250+(c2*250)

sliders[3][0]=1250+(float(COUNT-500)/1500)*250
xoff=[0.0]*4
fundo=0.0

def circ(rad):
    vert=[]
    angle=2*PI/10
    theta=0
    while theta<TWO_PI:
        y=cent[1]+rad*sin(theta)
        x=cent[0]+rad*cos(theta)
        vert.append((x,y))
        theta+=angle
    return vert
        
def star(x, y, radius1, radius2, npoints):
    angle = TWO_PI / npoints;
    halfAngle = angle/2.0;
    a=0
    vert=[]
    while a < TWO_PI: 
        sx = x + cos(a) * radius2;
        sy = y + sin(a) * radius2;
        vert.append((cent[0]+sx,cent[1]+sy))
        sx = x + cos(a+halfAngle) * radius1;
        sy = y + sin(a+halfAngle) * radius1;
        vert.append((cent[0]+sx,cent[1]+sy))
        a+=angle
    return vert

def svgLoad(filename):
    shp=loadShape(filename)
    children=shp.getChildCount()
    vert=[]
    for i in xrange(children):
        print(i)
        child=shp.getChild(i)
        # print("child vertex",child.getVertexCount(),children,child.getChildCount())
        # while child.getVertexCount()<1:
        #     if child.getChildCount()>0:
        #         print("child vertex",child.getVertexCount(),children,child.getChildCount())
        #         child=child.getChild(0)
        #     else:
        #         break
        #     # if child.getChildCount()>1:
        #     #     break
        # # print('child',child.getChild(0).getVertexCount())
        total=child.getVertexCount()
        for j in xrange(total):
            c=cent[0]-shp.width/2,cent[1]-shp.height/2
            vert.append([c[0]+child.getVertex(j).x,c[1]+child.getVertex(j).y])
    return vert

def addAll():
    shapes=[]
    shapes.append(circB)
    shapes.append(circS)
    shapes.append(svgLoad('apple.svg'))
    shapes.append(starP)
    return shapes
    

shapes=[]
circB=circ(210)
circS=circ(150)
starP=star(0,0,90,210,5)

def setup():
    size(sW,sH)
    background(0)
    frameRate(30)
    global shp,img,f,p
    img=loadImage('bg2.jpg')
    noStroke()
    f = createFont("Arial",16);    

def mousePressed():
    global show,take,DEST,space,full,frame
    x=mouseX
    y=mouseY
    if take==True:
        if len(DEST)<5 and x<sW-500:
            DEST.append((x,y))
        if len(DEST)==5:
            space=main(COUNT,DEST,(sW-500,sH),W,c1,c2)
            take=False
    else:
        if True in over:
            ind=over.index(True)
            locked[ind]=True
            over[ind]=False
            xoff[ind]=x-sliders[ind][0]
        b1=dic['Single Color']
        if x>=b1[0] and x<=b1[-2]:
            b2=dic['Multiple Color']
            b3=dic['Show/Hide Targets']
            b4=dic['Custom Targets']
            b5=dic['Pre-set Animation']
            if y>=b1[1] and y<=b1[-1]:
                fill(255,100,10,0)
                rect(b1[0],b1[1],b1[-2]-b1[0],b1[-1]-b1[1])
                space.changeColor(0)
            elif y>=b2[1] and y<=b2[-1]:
                fill(255,100,10,0)
                rect(b2[0],b2[1],b2[-2]-b2[0],b2[-1]-b2[1])
                space.changeColor(1)
            elif y>=b3[1] and y<=b3[-1]:
                    fill(255,100,10,0)
                    rect(b3[0],b3[1],b3[-2]-b3[0],b3[-1]-b3[1])
                    if show==False:
                        show=True
                    else:
                        show=False
            elif y>=b4[1] and y<=b4[-1]:
                    fill(255,100,10,0)
                    rect(b4[0],b4[1],b4[-2]-b4[0],b4[-1]-b4[1])
                    take=True
                    full=False
                    DEST=[]
            elif y>=b5[1] and y<=b5[-1] and full==False:
                fill(255,100,10,120)
                rect(b5[0],b5[1],b5[-2]-b5[0],b5[-1]-b5[1])
                if full==False:
                    full=True
                    frame=k
                    
def mouseDragged():
    if True in locked:
        ind=locked.index(True)
        sliders[ind][0]=mouseX-xoff[ind]
        if sliders[ind][0]<1250:
            sliders[ind][0]=1250
        if sliders[ind][0]>1500:
            sliders[ind][0]=1500
        
def mouseReleased():
    global W,c1,c2,COUNT
    if True in locked:
        ind=locked.index(True)
        locked[ind]=False
        r=float(sliders[ind][0]-1250)/250
        if ind==0:
            W=1-r
            space.changeInertia(W)
            print('Inertia:',1-W)
        elif ind==1:
            c1=r
            space.changeC1(c1)
            print('Personal Influence:',c1)
        elif ind==2:
            c2=r
            space.changeC1(c2)
            print('Global Influence:',c2)
        elif ind==3:
            COUNT=int((r*1500)+500)
            space.changePCount(COUNT)
            print('Total Particles:',COUNT)
        
                
def mouseHover():
    if mousePressed==False and take==False:
        x=mouseX
        y=mouseY
        b1=dic['Single Color']
        if x>=b1[0] and x<=b1[-2]:
            b2=dic['Multiple Color']
            b3=dic['Show/Hide Targets']
            b4=dic['Custom Targets']
            b5=dic['Pre-set Animation']
            if y>=b1[1] and y<=b1[-1]:
                fill(255,100,10,120)
                rect(b1[0],b1[1],b1[-2]-b1[0],b1[-1]-b1[1])
            elif y>=b2[1] and y<=b2[-1]:
                fill(255,100,10,120)
                rect(b2[0],b2[1],b2[-2]-b2[0],b2[-1]-b2[1])
            elif y>=b3[1] and y<=b3[-1]:
                fill(255,100,10,120)
                rect(b3[0],b3[1],b3[-2]-b3[0],b3[-1]-b3[1])
            elif y>=b4[1] and y<=b4[-1]:
                fill(255,100,10,120)
                rect(b4[0],b4[1],b4[-2]-b4[0],b4[-1]-b4[1])
            elif y>=b5[1] and y<=b5[-1] and full==False:
                fill(255,100,10,120)
                rect(b5[0],b5[1],b5[-2]-b5[0],b5[-1]-b5[1])
            


def interface():
    r,g,b,a=255,100,10,80
    #bg image
    image(img,0,0,sW,sH)
    if take==True:
        r,g,b,a=150,150,150,150
        txt=str(len(DEST))+"/"+str(5)+" Targets selected"
        fill(255)
        text(txt,40,40)
        for p in DEST:
            fill(120,34,215)
            ellipse(p[0],p[1],20,20)
        
    #menu space
    fill(255,100,10,50)
    rect(width-400,0,400,height)
    
    #buttons
    bX=width-350
    bY=60
    bW=300
    bH=50
    step=40
    fill(r,g,b,a)
    rect(bX,bY,bW,bH)
    rect(bX,bY+bH+step,bW,bH)
    rect(bX,bY+2*(bH+step),bW,bH)
    rect(bX,bY+3*(bH+step),bW,bH)
    if full==True:
        fill(150,150,150,150)
    rect(bX,bY+4*(bH+step),bW,bH)
    
    #sliders
    posX=bX
    posY=bY+5*(bH+step)+50
    stroke(255)
    line(posX,posY-10,posX,posY+10)
    line(posX+bW,posY-10,posX+bW,posY+10)
    posY=posY+70
    line(posX,posY-10,posX,posY+10)
    line(posX+bW,posY-10,posX+bW,posY+10)
    posY+=70
    line(posX,posY-10,posX,posY+10)
    line(posX+bW,posY-10,posX+bW,posY+10)
    posY+=70
    line(posX,posY-10,posX,posY+10)
    line(posX+bW,posY-10,posX+bW,posY+10)
    for i in range(len(sliders)):
        line(sliders[i][2],sliders[i][3],sliders[i][4],sliders[i][5])
    stroke(0)
    global over
    over=[False]*4
    if take==True:
        fill(r,g,b)
    else:
        x=mouseX
        y=mouseY
        for i in range(len(sliders)):
            if x>=sliders[i][0] and x<=sliders[i][0]+sliderW:
                if y>=sliders[i][1] and y<=sliders[i][1]+sliderH:
                        fill(200)
                        rect(sliders[i][0],sliders[i][1],sliderW,sliderH)
                        over[i]=True
                        break
                else:
                    continue
            else:
                continue
        fill(255)
    for i in range(len(over)):
        if over[i]==False:
            rect(sliders[i][0],sliders[i][1],sliderW,sliderH)
    
    noStroke()
    #text
    textFont(f,20)
    fill(255)
    string1='Single Color'
    tX=bX+(bW-(len(string1)*9))/2
    tY=bY+30
    text(string1,tX,tY)
    string2='Multiple Color'
    tX=bX+(bW-(len(string2)*9))/2
    tY=bY+bH+step+30
    text(string2,tX,tY)
    string3='Show/Hide Targets'
    tX=bX+(bW-(len(string3)*9))/2
    tY=bY+2*(bH+step)+30
    text(string3,tX,tY)
    string4='Custom Targets'
    tX=bX+(bW-(len(string4)*9))/2
    tY=bY+3*(bH+step)+30
    text(string4,tX,tY)
    string5='Pre-set Animation'
    tX=bX+(bW-(len(string5)*9))/2
    tY=bY+4*(bH+step)+30
    text(string5,tX,tY)
    string6='Inertia'
    tX=bX
    tY=bY+5*(bH+step)+20
    text(string6,tX,tY)    
    string7='Personal Influence'
    tY=tY+70
    text(string7,tX,tY)
    string8='Global Influence'
    tY+=70
    text(string8,tX,tY)
    string8='Total Particles'
    tY+=70
    text(string8,tX,tY)
    
    in1='0'
    textFont(f,15)
    tX=tX-5
    tY=bY+5*(bH+step)+38
    text(in1,tX,tY)
    f1='1'
    text(f1,tX+300,tY)
    tY+=70
    text(in1,tX,tY)
    text(f1,tX+300,tY)
    tY+=70
    text(in1,tX,tY)
    text(f1,tX+300,tY)
    in2='500'
    tY+=70
    text(in2,tX,tY)
    f2='2000'
    f1='1'
    text(f2,tX+295,tY)
    
    
    dic[string1]=[bX,bY,bX+bW,bY+bH]
    dic[string2]=[bX,bY+bH+step,bX+bW,bY+bH+step+bH]
    dic[string3]=[bX,bY+2*(bH+step),bX+bW,bY+2*(bH+step)+bH]
    dic[string4]=[bX,bY+3*(bH+step),bX+bW,bY+3*(bH+step)+bH]
    dic[string5]=[bX,bY+4*(bH+step),bX+bW,bY+4*(bH+step)+bH]
    
    #small circle, large circle, star, apple
    #inertia
    #global influence
    #personal influence
    #no. of particles
    


shapes.append(circB)    
DEST=shapes[0]  
space=main(COUNT,DEST,(sW-500,sH),W,c1,c2)
frame=100
k=100
def draw():
    global DEST,frame,space,shapes
    interface()
    mouseHover()
    if full==True:
        if frame==100:
            shapes=addAll()
        if (frame-k)%k==0:
            ind=((frame-k)/k)%len(shapes)
            DEST=shapes[ind]
            space.updateShape(DEST)
    frame+=1
    space.run(show,take)





    


    


    



        
