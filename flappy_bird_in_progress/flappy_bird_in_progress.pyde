class Bird():
    def __init__(self):
        self.x = 60
        self.y = 325
        self.speed = 4
        
    def show(self):
        fill(255,153,51)
        stroke(0)
        ellipse(self.x,self.y,60,60) 
        fill(3)
        stroke(0)
        ellipse(self.x+28,self.y-7,10,10)  
        fill(250)
        stroke(0)
        ellipse(self.x+30,self.y-7,4,4)
        fill(255,255,102)
        stroke(0)
        arc(self.x,self.y+5,40,30,0,PI+QUARTER_PI, CHORD)
    
    def fall(self, block_count):
        self.y = self.y -- ((block_count/5)+self.speed)
            
    def jump(self, block_count):
        self.y = self.y - ((block_count/5)+(self.speed*2))
        
class UpperBlocks():
    def __init__(self):
        self.xa = 760
        self.ya = 0
        self.xb = 780
        self.yb = random(10,550)
        self.count = 0
        self.speed = 4
        
    def move(self):
        self.xa = self.xa - ((self.count/3) + self.speed)
        self.xb = self.xb - ((self.count/3) + self.speed)
        if self.xb <= 0:
            self.xa = 760
            self.ya = 0
            self.xb = 780
            self.yb = random(10,550)
            self.count += 1
            
    def show(self):
        fill(51,255,51)
        stroke(0)
        rectMode(CORNERS)
        rect(self.xa,self.ya,self.xb,self.yb)
        textSize(32)
        fill(255)
        text("SCORE: {}".format(self.count),600, 30) 
        
    def reset(self):
        self.xa = 760
        self.ya = 0
        self.xb = 780
        self.yb = random(10,550)
        self.count = 0
        
class LowerBlocks():
    def __init__(self, upper_height):
        self.xa = 760
        self.ya = upper_height + random(150,220)
        self.xb = 780
        self.yb = 650
        self.speed = 4
        self.count = 0
        
    def move(self, upper_height):
        self.xa = self.xa - ((self.count/3) + self.speed)
        self.xb = self.xb - ((self.count/3) + self.speed)
        if self.xb <= 0:
            self.xa = 760
            self.ya = upper_height + random(150,220)
            self.xb = 780
            self.yb = 650
            self.count += 1
           
    def show(self):
        fill(51,255,51)
        stroke(0)
        rectMode(CORNERS)
        rect(self.xa,self.ya,self.xb,self.yb)
        
    def reset(self, upper_height):
        self.count = 0
        self.xa = 760
        self.ya = upper_height + random(150,220)
        self.xb = 780
        self.yb = 650 
        

bird = Bird()
upper_blocks = UpperBlocks()
lower_blocks = LowerBlocks(upper_blocks.yb)


def setup():
    size(800,650)
    global tree
    global tree2
    global sun
    sun = loadImage("sun.png")
    tree = loadImage("redtree.png")
    tree2 = loadImage("tree1.png")
   
   
def draw():
    background(135, 206, 235)
    fill(0)
    text("Simon's Flappy Bird", 40, 40)
    fill(153,76,0)
    noStroke()
    rectMode(CORNERS)
    rect(0,450,800,650)
    image(tree, 170, height/2, 88*2, 83*2)
    image(tree, 620, height/2, 88*2, 83*2)
    image(tree2, 400, height/2, 88*2, 83*2)
    image(sun, 550, 75, 48*4, 36*4)
    bird.fall(upper_blocks.count)
    bird.show()
    if keyPressed:
        bird.jump(upper_blocks.count)    
    upper_blocks.show()
    upper_blocks.move()
    lower_blocks.show()
    lower_blocks.move(upper_blocks.yb)
        
    if bird.y >= 650 or bird.y < 0:
        textSize(32)
        fill(255)
        text("YOU LOSE!!!\n\n To Play Again Press Any Key", 300, 200)
        if keyPressed:
            bird.y = 325    
            upper_blocks.reset()
            lower_blocks.reset(upper_blocks.yb)

            
    if bird.x >= upper_blocks.xa and dist(bird.x, bird.y, upper_blocks.xa, upper_blocks.ya) < upper_blocks.yb + 30:
        bird.y = -10
        textSize(32)
        fill(255)
        text("YOU LOSE!!!\n\n To Play Again Press Any Key", 300, 300)
        bird.y = 325    
        upper_blocks.reset()
        lower_blocks.reset(upper_blocks.yb) 

        
    if bird.x >= lower_blocks.xa and dist(bird.x, bird.y, lower_blocks.xa, lower_blocks.yb) < (height-lower_blocks.ya) + 30:
        bird.y = -10
        textSize(32)
        fill(255)
        text("YOU LOSE!!!\n\n To Play Again Press Any Key", 300, 300)
        bird.y = 325    
        upper_blocks.reset()
        lower_blocks.reset(upper_blocks.yb)

    

    
