from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg='#f0f1f5')

def BMI():
    try:
        h = float(Height.get())
        w = float(Weight.get())
        m = h / 100
        bmi = round(w / m ** 2, 1)
        label1.config(text=bmi)

        if bmi <= 18.5:
            label2.config(text="Underweight")
            label3.config(text="It indicates that you have lower weight than normal body!")
        elif 18.5 < bmi <= 25:
            label2.config(text="Normal")
            label3.config(text="It indicates that you are healthy!")
        elif 25 < bmi <= 30:
            label2.config(text="Overweight")
            label3.config(text="It indicates that you are slightly overweight!")
        else:
            label2.config(text="Obesity")
            label3.config(text="It indicates you are in the levels of obesity!")
    except ValueError:
        label1.config(text="Error")
        label2.config(text="")
        label3.config(text="Enter valid numbers!")

# Icon and other images
try:
    image_icon = PhotoImage(file="images/icon.png")
    root.iconphoto(False, image_icon)
except:
    pass

try:
    top = PhotoImage(file="images/top.png")
    Label(root, image=top, background='#f0f1f5').place(x=-10, y=-10)
except:
    pass

Label(root, width=72, height=18, bg='lightblue').pack(side=BOTTOM)

try:
    box = PhotoImage(file="images/box.png")
    Label(root, image=box).place(x=20, y=100)
    Label(root, image=box).place(x=240, y=100)
except:
    pass

try:
    scale = PhotoImage(file="images/scale.png")
    Label(root, image=scale, bg='lightblue').place(x=20, y=310)
except:
    pass

# Sliders
current_value = tk.DoubleVar()
current_value2 = tk.DoubleVar()

def get_current_value():
    return '{:.2f}'.format(current_value.get())

def get_current_value2():
    return '{:.2f}'.format(current_value2.get())

def slider_changed(event):
    Height.set(get_current_value())
    update_man_image()

def slider_changed2(event):
    Weight.set(get_current_value2())

style = ttk.Style()
style.configure("TScale", background='white')

slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style='TScale',
                   command=slider_changed, variable=current_value)
slider.place(x=80, y=250)

slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style='TScale',
                    command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

# Entry boxes
Height = StringVar()
Weight = StringVar()

Entry(root, textvariable=Height, width=5, font='arial 50',
      bg='#fff', fg='#000', bd=0, justify='center').place(x=35, y=160)
Label(root, text="Height (cm)", font=('Segoe UI', 10, 'bold'), bg='#f5f7fa', fg='#333').place(x=100, y=280)

Entry(root, textvariable=Weight, width=5, font='arial 50',
      bg='#fff', fg='#000', bd=0, justify='center').place(x=255, y=160)
Label(root, text="Weight (kg)", font=('Segoe UI', 10, 'bold'), bg='#f5f7fa', fg='#333').place(x=320, y=280)

Height.set(get_current_value())
Weight.set(get_current_value2())

# Load original image using Pillow
try:
    original_pil_img = Image.open("images/man.png")
    original_width, original_height = original_pil_img.size
    pil_img = original_pil_img.copy()
    tk_img = ImageTk.PhotoImage(pil_img)
except:
    original_pil_img = None
    tk_img = None

# Label to display image
image_label = Label(root, bg='lightblue')
image_label.place(x=185, y=380)

def update_man_image():
    global tk_img
    if not original_pil_img:
        return

    height_val = current_value.get()
    scale_factor = 1 + (height_val / 220)  # scaling based on height
    new_height = int(original_height * scale_factor)
    if new_height < original_height:
        new_height = original_height

    resized = original_pil_img.resize((original_width, new_height), Image.ANTIALIAS)
    tk_img = ImageTk.PhotoImage(resized)
    image_label.config(image=tk_img)

# Labels
label1 = Label(root, font='arial 60 bold', bg='lightblue', fg='#fff')
label1.place(x=125, y=305)

label2 = Label(root, font='arial 20 bold', bg='lightblue', fg='#3b3a3a')
label2.place(x=280, y=430)

label3 = Label(root, wraplength=200, justify="center", font='arial 12', bg='lightblue')
label3.place(x=200, y=470)

# Buttons
Button(root, text="View Report", width=15, height=2, font='arial 10 bold',
       bg='#1f6e68', fg='white', command=BMI).place(x=280, y=340)

def reset():
    Height.set("")
    Weight.set("")
    current_value.set(0)
    current_value2.set(0)
    slider.set(0)
    slider2.set(0)
    label1.config(text="")
    label2.config(text="")
    label3.config(text="")
    update_man_image()

Button(root, text="Reset", width=15, height=2, font=('Segoe UI', 10, 'bold'),
       bg='#9e2a2b', fg='white', bd=0, command=reset).place(x=280, y=400)

# Show default image once
update_man_image()

root.mainloop()
