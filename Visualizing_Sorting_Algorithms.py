from tkinter import *
from random import *


def bubble_sort(arr,pos):
    for a in range(len(arr)):
        flag = 0
        for b in range(len(arr)-1-a):
            if arr[b]>arr[b+1]:
                arr[b],arr[b+1] = arr[b+1],arr[b]

                canvas.move(pos[b],1,0)
                canvas.move(pos[b+1],-1,0)
                pos[b],pos[b+1] = pos[b+1],pos[b]
                window.update()
                flag=1
        if flag==0:
            break
        window.update()



window = Tk()
window.title('Bubble Sort')
window.geometry('400x400')

win_height = 400
win_width = 400

canvas = Canvas(window,width=win_height,height=win_width)
canvas.pack()

cnv_mrgn = 50
base = win_height-cnv_mrgn
x=cnv_mrgn
y=0

canvas.create_rectangle(cnv_mrgn,cnv_mrgn,base,base,fill='white')
counter=0
arr=[]
pos=[]
while x<win_width-cnv_mrgn:
    counter+=1
    ln_height = randint(cnv_mrgn,win_width-cnv_mrgn)
    line = canvas.create_line(x,base,x,400-ln_height,fill='magenta')
    arr.append(ln_height)
    pos.append(line)
    x+=1

print(arr)
bubble_sort(arr,pos)
print(arr)

print(counter)
window.mainloop()