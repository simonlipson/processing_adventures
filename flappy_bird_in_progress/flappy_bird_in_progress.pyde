class Bird():
    def __init__(self):
        self.x = 60
        self.y = 325
        self.speed = 4
        
    def show(self):
        fill(255,153,51)
        ellipse(self.x,self.y,60,60) 
        fill(3)
        ellipse(self.x+28,self.y-7,10,10)  
        fill(250)
        ellipse(self.x+30,self.y-7,4,4)
        fill(255,255,102)
        arc(self.x,self.y+5,40,30,0,PI+QUARTER_PI, CHORD)
    
    def fall(self):
        self.y = self.y -- self.speed
            
    def jump(self):
        self.y = self.y - (self.speed*2)
        
class UpperBlocks():
    def __init__(self):
        self.xa = 760
        self.ya = 0
        self.xb = 780
        self.yb = random(10,600)
        
    def move(self):
        self.xa = self.xa - 4
        self.xb = self.xb - 4
        if self.xb == 0:
            self.xa = 760
            self.ya = 0
            self.xb = 780
            self.yb = random(10,600)
            
    def show(self):
        fill(51,255,51)
        rectMode(CORNERS)
        rect(self.xa,self.ya,self.xb,self.yb)
        
class LowerBlocks():
    def __init__(self, upper_height):
        self.xa = 760
        self.ya = upper_height + random(150,220)
        self.xb = 780
        self.yb = 650
        
    def move(self, upper_height):
        self.xa = self.xa - 4
        self.xb = self.xb - 4
        if self.xb == 0:
            self.xa = 760
            self.ya = upper_height + random(150,220)
            self.xb = 780
            self.yb = 650
           
        
    def show(self):
        rectMode(CORNERS)
        rect(self.xa,self.ya,self.xb,self.yb)
        

bird = Bird()
upper_blocks = UpperBlocks()
lower_blocks = LowerBlocks(upper_blocks.yb)

def setup():
    size(800,650)
    

def draw():
    background(135, 206, 235)
    bird.fall()
    bird.show()
    if keyPressed:
        bird.jump()    
    upper_blocks.show()
    upper_blocks.move()
    lower_blocks.show()
    lower_blocks.move(upper_blocks.yb)
    
    if bird.y >= 650 or bird.y < 0:
        textSize(32)
        fill(255)
        text("YOU LOSE!!!\n\n To Play Again Press Any Key", 300, 300)
        if keyPressed:
            bird.y = 325    
            upper_blocks.xa = 760
            upper_blocks.ya = 0
            upper_blocks.xb = 780
            upper_blocks.yb = random(10,600)
            lower_blocks.xa = 760
            lower_blocks.ya = upper_blocks.yb + random(150,220)
            lower_blocks.xb = 780
            lower_blocks.yb = 650 
      

    

    
