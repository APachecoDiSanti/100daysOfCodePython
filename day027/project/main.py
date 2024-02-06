import tkinter as tk


def miles_to_kms():
    miles = round(float(miles_input.get()), 3)
    kms = round(miles * 1.609344, 3)
    conversion_label.config(text=kms)


window = tk.Tk()
window.title("Miles to KMs converter")
window.config(padx=30, pady=15)

# LAYOUT
# *         INPUT       MILES
# equals    conversion  KM
# *         BUTTON      *

miles_input = tk.Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

equals_label = tk.Label(text="is equal to")
equals_label.grid(column=0, row=1)

conversion_label = tk.Label(text="")
conversion_label.grid(column=1, row=1)

km_label = tk.Label(text="KMs")
km_label.grid(column=2, row=1)

conversion_button = tk.Button(text="Convert")
conversion_button.config(command=miles_to_kms)
conversion_button.grid(column=1, row=2)

window.mainloop()
