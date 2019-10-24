class Drop:
    
    def __init__(self):
        self.x = random(640)
        self.y = random(-300, 360)
        self.z = random(0,20)
        self.leng = map(self.z,0,20,10,20)
        self.yspeed = map(self.z,0,20,4,10)
        self.thick = map(self.z,0,20,0.1,2)
        

    
    def fall(self):
        self.y = self.y + self.yspeed
        self.yspeed = self.yspeed + 0.15
        if self.y > 360:
            self.y = 0
            self.yspeed = map(self.z,0,20,4,10)
        
    def show(self):
        stroke(138,43,226)
        strokeWeight(self.thick)
        line(self.x,self.y,self.x,self.y+self.leng)
        
d = Drop()
    
drop_list = [Drop() for i in range(500)]
    
def setup():
    size(640,360)

    
def draw():
    background(230,230,250)
    for drop in drop_list:
        drop.fall()
        drop.show()
