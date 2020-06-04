from dot_path import DotPath

dotpaths = []

def setup():
    global dotpaths
    size(800, 600)
    dotpaths.append(DotPath(width, height))
    

def draw():
    global dotpaths
    
    noStroke()
    background(190, 229, 191)
    fill(73, 54, 87)

    for d in dotpaths:
        d.draw()
        
    if d.finished:
        dotpaths.append(DotPath(width, height))
        
    saveFrame('points-and-lines-#####.png')
