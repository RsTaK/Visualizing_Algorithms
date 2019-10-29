width_of_cells = 40
grid = []
flag = -1

openset = []
closedset = []


def setup():
    
    size(400, 400)
    global rows, columns
    rows = floor(width/width_of_cells)
    columns = floor(height/width_of_cells)
    for j in range(columns):
        for i in range(rows):
            cell_point = cell(i, j)
            global grid
            grid.append(cell_point)
        


def draw():
    if flag == -1:
        background(255)
        for i in grid:
            drawing_cells(i[0],i[1])
    
    if flag == 0:
        for i in grid:
                color_cells(x, y)
        
    if flag == 1:
        for i in grid:
                color_cells(x, y, b = 255)

    if flag == 2:
        for i in grid:
                color_cells(x, y, r = 255)
    
    if keyPressed:
        
        if (key == 'r' or key == 'R'):
            if len(openset) > 0:
                
                current_node = openset[0]
                current_index = 0
                
                for index, item in enumerate(openset):
                    if item[4] < current_node[4]:
                        current_node = item
                        current_index = index
                        
                openset.pop(current_index)
                closedset.append(current_node)
                
                
                if (current_node[0] == goal[0] and current_node[1] == goal[1]):
                    path = []
                    current = current_node
                    while current is not None:
                        path.append((current[0], current[1]))
                        current = current[5]
                    print('Path founded')
                    
                

              
            for i in openset:
                color_cells(i[0], i[1], 200,200,200)

            for i in closedset:
                color_cells(i[0], i[1], 100,0,100)               


def drawing_cells(x, y):
    
    stroke(0)
    noFill()
    rect(x, y,width_of_cells-1 , width_of_cells-1)


def color_cells(x, y, r = 0, b = 0, g = 0, a = 255):
    
    fill(r, b, g, a)
    rect(x, y,width_of_cells-1 , width_of_cells-1) 

        
def cell(i, j):
    
    x = i*width_of_cells
    y = j*width_of_cells
    
    g_cost = 0
    h_cost = 0
    f_cost = 0
    parent = None
    
    return((x, y, g_cost, h_cost, f_cost, parent))


def mouseClicked():

    if keyPressed:
        
        if (key=='s' or key=='S'):
            
                global flag
                flag = 1
                i, j = (mouseY/width_of_cells),(mouseX/width_of_cells)
                global x, y
                y, x = i*width_of_cells, j*width_of_cells 
                start = (x, y, 0, 0, 0, None)
                openset.append(start)
              
                
        if (key=='e' or key=='E'):
            
                global flag
                flag = 2
                i, j = (mouseY/width_of_cells),(mouseX/width_of_cells)
                global x, y
                y, x = i*width_of_cells, j*width_of_cells
                global goal
                goal = (x, y)
                

                        
def mouseDragged():
    
    global flag
    flag = 0
    global x, y
    i, j = (mouseY/width_of_cells),(mouseX/width_of_cells)
    y, x = i*width_of_cells, j*width_of_cells
    
