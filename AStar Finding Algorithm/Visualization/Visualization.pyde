width_of_cells = 40 
grid = []
start = None
stop = None
current = None
flag=-1
global x, y
neighbour = []

openset = []
closedset = []



def setup():
    
    size(800, 800)
    global rows, columns
    rows = floor(width/width_of_cells)
    columns = floor(height/width_of_cells)
    for i in range(rows):
        for j in range(columns):
            current_cell_points = cell(i, j)
            global grid
            grid.append(current_cell_points)
            

def draw():
    if flag == -1:
        background(255)
        for i in grid:
            drawing_cells(i[0],i[1])
    
    if flag == 0:
        for i in grid:
            if i[0] == x and i[1] == y:
                fill(0, 0, 0)
                rect(x, y,width_of_cells, width_of_cells)    

                
    if flag == 1:
        for i in grid:
            if i[0] == x and i[1] == y:
                fill(0, 255, 0)
                rect(x, y,width_of_cells, width_of_cells)
                global start
                start = i
                global openset
                openset.append(start)

                print(openset)
            
                
                
    if flag == 2:
        for i in grid:
            if i[0] == x and i[1] == y:
                fill(255, 0, 0)
                rect(x, y,width_of_cells, width_of_cells)
                global stop
                stop = i
                print(stop)
    


        


def mouseDragged():
    
    global flag
    flag = 0
    global x, y
    i, j = (mouseY/width_of_cells),(mouseX/width_of_cells)
    y, x = i*width_of_cells, j*width_of_cells
    

def mouseClicked():
    
    if keyPressed:
        
        if (key=='s' or key=='S'):
                global flag
                flag = 1
                global x, y
                i, j = (mouseY/width_of_cells),(mouseX/width_of_cells)
                y, x = i*width_of_cells, j*width_of_cells

        
        if (key=='e' or key=='E'):
                global flag
                flag = 2
                global x, y
                i, j = (mouseY/width_of_cells),(mouseX/width_of_cells)
                y, x = i*width_of_cells, j*width_of_cells

def cell(i, j):
    
    x = i*width_of_cells
    y = j*width_of_cells
    
    h = 0
    g = 0
    f = 0
    
    parent = None
    
    return([x, y, h, g, f, parent])

    
def drawing_cells(x, y):

    line(x, y, x+width_of_cells, y)
    line(x+width_of_cells, y, x+width_of_cells, y+width_of_cells)
    line(x+width_of_cells, y+width_of_cells, x, y+width_of_cells)
    line(x, y+width_of_cells, x, y)
    
    
    
'''def getNeighbour(x, y):
   for i in grid:
       if (i[0] == current[0] and i[1] == current[1]):
           top = [i[current[0]],i[current[1]-width_of_cells]]
           right = [i[current[0]+width_of_cells],i[current[1]]]
           left = [i[current[0]-width_of_cells],i[current[1]]]
           bottom = top = [i[current[0]-width_of_cells],i[current[1]]]'''
                
           
    
    
