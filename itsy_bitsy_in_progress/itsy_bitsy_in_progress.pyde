add_library('sound')

class Spider():
    
    def __init__(self):
        self.x = 320
        self.y = 440
        self.speed = 1
        self.count = 0

    def show(self):
        image(spider,self.x,self.y,60,60)

        
    def climb(self, suny):
        if self.y > 100 and (self.count == 0 or suny == 100):
            self.y = self.y - self.speed
        if self.y == 100:
            self.count += 1
            
    def fall(self):
        if self.y <= 440:
            self.y = self.y + self.speed
        if self.y > 440:
            self.count = 2
            
class Sun:
    
    def __init__(self):
        self.x = 500
        self.y = 440
        self.speed = 2
        self.count = 0
        
    def move(self):
        if self.y > 100:
            self.y -= self.speed
        if self.y == 100:
            self.count += 0
        
    def show(self):
        image(sun,self.x,self.y,48*3,36*3)

class Drop:
    
    def __init__(self):
        self.x = random(640)
        self.y = random(-300, 360)
        self.z = random(0,20)
        self.leng = map(self.z,0,20,10,20)
        self.yspeed = map(self.z,0,20,4,10)
        self.thick = map(self.z,0,20,0.1,2)
        self.count = 0
        
    
    def fall(self):
        self.y = self.y + self.yspeed
        self.yspeed = self.yspeed + 0.15
        if self.y > 500:
            self.y = 0
            self.count += 1
            self.yspeed = map(self.z,0,20,4,10)
        
    def show(self):
        stroke(224,224,224)
        strokeWeight(self.thick)
        line(self.x,self.y,self.x,self.y+self.leng)
        
        
d = Drop()
drop_list = [Drop() for i in range(500)]
myspider = Spider()
mysun = Sun()

def setup():
    size(640,500)
    global spider
    spider = loadImage("realspider.png")
    global sun
    sun = loadImage("sun.png")
    

def draw():
    background(135, 206, 235)
    fill(147,161,172)
    rectMode(CORNERS)
    rect(width/2-30,height,width/2+30,0)
    myspider.show()
    myspider.climb(mysun.y)
    if myspider.count == 1:
        for drop in drop_list:
            drop.fall()
            drop.show()
        myspider.fall()
    if myspider.count >= 2:
        mysun.show()
        mysun.move()


    
