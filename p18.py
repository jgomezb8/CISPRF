from tkinter import *

def createwinmain():
    winmain = Tk()
    winmain.geometry('500x500')
    winmain.title("Temperature Program")
    txt = Label(winmain,
        font=("Arial Bold", 20),
        text="Temperature Conversion",
        fg="blue")
    txt.grid(row=0, column=1)  # Center the title using row=0, column=1
    return (winmain, txt)

def labeltxt(winmain):
    txtboxlbl = Label(winmain, font=("Arial Bold", 14),
        text="Kelvin: ",
        fg="yellow", bg='black')
    txtboxlbl.grid(row=3, column=0)  # Place label in row 3, column 0
    txtbox = Entry(winmain, width=14, font=("Arial Bold", 14))
    txtbox.grid(row=3, column=1)  # Place textbox in row 3, column 1
    return (txtboxlbl, txtbox)

def labeltxt2(winmain):
    txtboxlbl2 = Label(winmain, font=("Arial Bold", 14),
        text="Celsius: ",
        fg="yellow", bg='black')
    txtboxlbl2.grid(row=5, column=0)  # Place label in row 5, column 0
    txtbox2 = Entry(winmain, width=14, font=("Arial Bold", 14))
    txtbox2.grid(row=5, column=1)  # Place textbox in row 5, column 1
    return (txtboxlbl2, txtbox2)

def labeltxt3(winmain):
    txtboxlbl3 = Label(winmain, font=("Arial Bold", 14),
        text="Fahrenheit: ",
        fg="yellow", bg='black')
    txtboxlbl3.grid(row=7, column=0)  
    txtbox3 = Entry(winmain, width=14, font=("Arial Bold", 14))
    txtbox3.grid(row=7, column=1) 
    return (txtboxlbl3, txtbox3)

def error_message(winmain):
    error_txt = Label(winmain, font=("Arial", 12),
        text="Error: Invalid input",
        fg="red", bg="black")
    error_txt.grid(row=8, column=0, columnspan=2) 
    return error_txt

def validate_kelvin(kelvin):
    try:
        kelvin = float(kelvin)
        if kelvin <= 0:
            return False
        return True
    except ValueError:
        return False

def convert_temperature(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (9/5) * (kelvin - 273) + 32
    return celsius, fahrenheit

def on_calculate(txtbox, txtbox2, txtbox3, error_lbl):
    kelvin = txtbox.get()
    
   
    if not kelvin or not validate_kelvin(kelvin):
        error_lbl.config(text="Error: Please enter a valid Kelvin temperature (greater than 0).")
        txtbox.config(bg="red")
        return
    
    kelvin = float(kelvin)
    celsius, fahrenheit = convert_temperature(kelvin)
    
    
  
    txtbox2.insert(0,str(celsius))
    

    txtbox3.insert(0,str(fahrenheit))
    
    
    txtbox.config(bg="white")
    error_lbl.config(text="")  

def clear_all(txtbox, txtbox2, txtbox3, error_lbl):
    txtbox.delete(0, END)
    txtbox2.delete(0, END)
    txtbox3.delete(0, END)
    error_lbl.config(text="")
    txtbox.config(bg="white")

def btns(winmain, txtbox, txtbox2, txtbox3, error_lbl):
    cmd_calculate = Button(winmain, font=("Arial Bold", 16),
        text="Calculate", command=lambda: on_calculate(txtbox, txtbox2, txtbox3, error_lbl))
    cmd_calculate.grid(row=9, column=0) 
    
    cmd_clear = Button(winmain, font=("Arial Bold", 16),
        text="Clear", command=lambda: clear_all(txtbox, txtbox2, txtbox3, error_lbl))
    cmd_clear.grid(row=9, column=1)  
    
    cmd_quit = Button(winmain, font=("Arial Bold", 16),
        text="QUIT", fg="red", command=winmain.destroy)
    cmd_quit.grid(row=10, column=1)  
    
    return cmd_calculate, cmd_clear, cmd_quit

def win001():
    winmain, txt = createwinmain()
    txtboxlbl, txtbox = labeltxt(winmain)
    txtboxlbl2, txtbox2 = labeltxt2(winmain)
    txtboxlbl3, txtbox3 = labeltxt3(winmain)
    error_lbl = error_message(winmain)
    cmd_calculate, cmd_clear, cmd_quit = btns(winmain, txtbox, txtbox2, txtbox3, error_lbl)
    mainloop()

win001()
