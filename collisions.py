import pygame,math,sys,random
pygame.init()
#Adrians Problem

Colours=['red','blue','green','yellow','black','orange']
background=(255,255,255)
(width,height)=(800,600)

def collide(p1,p2):
    dx=p1.x-p2.x
    dy=p1.y-p2.y

    distance=math.hypot(dx,dy)
    if distance<p1.size+p2.size:
        tangent=math.atan2(dy,dx)
        angle=0.5*math.pi+tangent
        
        p1.angle=2*tangent-p1.angle
        p2.angle=2*tangent-p2.angle

        p1.x+=math.sin(angle)
        p1.y-=math.cos(angle)
        
        p2.x-=math.sin(angle)
        p2.y+=math.cos(angle)
    

class Particle:
    def __init__(self,(x,y),size):
        self.x=x
        self.y=y
        self.size=size
        
        self.color=(0,0,255)
        self.thickness=0
        self.angle=0
        self.speed=0

    def display(self):
        pygame.draw.circle(screen,self.color,(int(self.x),int(self.y)),self.size,self.thickness)

    def move(self):
        self.x+=math.sin(self.angle) * self.speed
        self.y+=math.cos(self.angle) * self.speed
        self.speed*=drag


screen = pygame.display.set_mode((width,height))



particles=[]

drag=1


x1=width/2+math.sin(math.pi/3)*100
y1=height/2+math.cos(math.pi/3)*100
size1=20
p1=Particle((x1,y1),size1)
p1.speed=-1
p1.angle=math.pi/3
particles.append(p1)

x2=width/2-math.sin(math.pi/3)*100
y2=height/2+math.cos(math.pi/3)*100
p2=Particle((x2,y2),size1)
p2.angle=-math.pi/3
p2.speed=-1
particles.append(p2)

x3=width/2
y3=height/2-100
p3=Particle((x3,y3),size1)
p3.angle=-math.pi
p3.speed = -1
particles.append(p3)



def check(particle):
    if (particle.x-particle.size)<0:
        particle.x=particle.size
        particle.angle=-particle.angle
        

    if (particle.x+particle.size)>width:
        particle.x=width-particle.size
        particle.angle=-particle.angle
        
        
        
    if (particle.y-particle.size)<0:
        particle.y=particle.size
        particle.angle=math.pi-particle.angle
        

    if (particle.y+particle.size)>height:
        particle.y=height-particle.size
        particle.angle=math.pi-particle.angle
"""       
for i in range(0,20):
    
    size=random.randint(10,20)
    x=random.randint(30,width-30)
    y=random.randint(30,height-30)

    particle = Particle((x,y),size)
    particle.speed=random.randint(1,1)
    particle.angle=random.uniform(0,2*math.pi)
    particles.append(particle)
"""
while True:
    pygame.time.wait(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            

    screen.fill(background)

   
        
        
        

    for i,particle in enumerate(particles):
    
        particle.move()
        check(particle)
        for particle2 in particles[i+1:]:
            collide(particle,particle2)
        particle.display()
        


    
        
    
    
    
    pygame.display.flip()
