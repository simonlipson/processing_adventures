def climb_pipe(x):
    return x + 100

def setup():
    size(640,500)
    global spider
    spider = loadImage("purple_spider.jpg")

def draw():
    background(135, 206, 235)
    fill(147,161,172)
    rectMode(CORNERS)
    rect(width/2-30,height,width/2+30,0)
    image(spider,width/2,height-climb_pipe(x),60,60)
    
