'''
This programn is a GUI program to convert miles into kilometers
'''

import tkinter as tk

window = tk.Tk()
window.title("Converter")
#window.minsize(width=500, height=300)
#window.maxsize(width=500, height=300)

def miles_to_km():
    km_label.config(text=str(int(miles_entry.get())*1.60934))

miles_entry = tk.Entry()
text_label = tk.Label(text=" miles is ")
km_label = tk.Label(text="_____")
text_label2 = tk.Label(text=" kilometers")
transform_button = tk.Button(text="convert", command=miles_to_km)

miles_entry.grid(column=0, row=0)
text_label.grid(column=1, row=0)
km_label.grid(column=2, row=0)
text_label2.grid(column=3, row=0)
transform_button.grid(column=0, row=1)

window.mainloop()