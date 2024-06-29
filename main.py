from tkinter import *

def button_clicked():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        BMI = weight / (height ** 2)
        print("BMI:", BMI)
        if BMI < 18.5 :
            my_label.config(text="underweight (BMI: {:.2f})".format(BMI))
        elif 18.5 <= BMI < 25:
            my_label.config(text="normal (BMI: {:.2f})".format(BMI))
        elif 25 <= BMI < 30:
            my_label.config(text="overweight (BMI: {:.2f})".format(BMI))
        else :
            my_label.config(text="obese (BMI: {:.2f})".format(BMI))

    except ValueError:
        my_label.config(text= "make sure you entered the correct value")

my_window = Tk()
my_window.title("tkinter python")
my_window.minsize(width = 300, height= 350)
my_window.config(padx=20, pady=20)

weight_label = Label(text="weight entry(kg)")
weight_label.config(bg ="orange")
weight_label.config(fg ="black")
weight_label.config(padx=46, pady=8)
weight_label.pack()

weight_entry = Entry(width=30)
weight_entry.focus()
weight_entry.pack()

height_label = Label(text="height entry(m)")
height_label.config(bg ="orange")
height_label.config(fg ="black")
height_label.config(padx=46, pady=8)
height_label.pack()

height_entry = Entry(width=30)
height_entry.pack()

my_button = Button(text ="calculate bmi", command = button_clicked)
my_button.config(padx=10, pady=10)
my_button.pack()

my_label = Label()
my_label.config(bg ="yellow")
my_label.config(fg ="black")
my_label.config(padx=57, pady=8)
my_label.pack()

my_window.mainloop()