from tkinter import *
def main():
 print('--> start <--')
 mainwin = Tk()
 wcan = Canvas( mainwin,bg='black',
 width=600,height=800)
 wcan.pack()
 
 wcan.create_oval(100, 100, 500, 500,
 fill='white', outline="white", width=5)

 points = [400,450,200, 450,300, 550]
 wcan.create_polygon(points, outline='blue',
 fill='red', width=10)
 
 wcan.create_line(400,330,200,330, width=30, fill="purple")
 wcan.create_oval(270,270, 170,170,
 fill='blue', outline="white", width=5)
 
 wcan.create_oval(325,170, 430,270,
 fill='red', outline="white", width=5)
 
 mainwin.mainloop()
main()
