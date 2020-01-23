import tkinter
import tkinter.filedialog

gui = tkinter.Tk()
numx = 12
numy = 9
sizex = 1000/numx
sizey = 500/numy
array = [0] * (numx*numy) 


canvas = tkinter.Canvas(gui, bg='white', width=1000, height=500)
canvas.grid(row=0, column=1)

frame = tkinter.Frame(gui)
frame.grid(row=0, column=0, sticky='n')
label1=tkinter.Label(frame, text="Figure").grid(row=0,column=0, sticky="nw")
def open_infile():
    file = tkinter.filedialog.askopenfilename(initialdir = './benchmarks/', filetypes = (("input layout","*.infile"),("all files","*.*")))
open_button = tkinter.Button(frame, text="Open", command=open_infile ).grid(row=1, column=0)


# def callback(event):
#     cv = event.widget
#     xloc = int(event.x / sizex)
#     yloc = int(event.y / sizey)
#     print("Clicked at", xloc, yloc)
#     array[yloc*numx+xloc] = -1
#     cv.create_rectangle(sizex*xloc,sizey*yloc,sizex*(xloc+1),sizey*(yloc+1), fill="blue")
#     for widget in frame.winfo_children():
#         widget.destroy()

def callback(event):
    cv = event.widget
    xloc = int(event.x / sizex)
    yloc = int(event.y / sizey)
    print("Clicked at", xloc, yloc)
    array[yloc*numx+xloc] = -1
    cv.create_rectangle(sizex*xloc,sizey*yloc,sizex*(xloc+1),sizey*(yloc+1), fill="blue")

canvas.focus_set()
canvas.bind("<Button-1>", callback)
#canvas.pack()

for x in range(0,numx):
    for y in range(0,numy):
       canvas.create_rectangle(sizex*x,sizey*y,sizex*(x+1),sizey*(y+1), fill="white")
canvas.update()
print(canvas.winfo_width())
print(canvas.winfo_height())

gui.mainloop()