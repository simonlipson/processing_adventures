class Star():
    
    def __init__(self):
        self.x = random(-800,800)
        self.y = random(-800,800)
        self.speed = random(0,2)
        
    def move(self):
        self.x = map(self.x+self.speed,0,2,0,2)
        self.y = map(self.y+self.speed,0,2,-800,800)
        
    def show(self):
        ellipse(self.x, self.y, 2,2)
        
stars = [Star() for i in range(1000)]

def setup():
    size(800,800)
    background(0)
    

def draw():
    translate(width/2, height/2)
    for star in stars:
        star.show()
        star.move()
