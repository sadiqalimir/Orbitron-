# ORBITRON by Sadiq Ali.
# A simple tool to calculate the orbital speed by corresponding parameters.
# Thank YOU.

import tkinter as tk
from tkinter import *
import math

def calculate_the_orbital_speed(r):
    mu = 3.986 * (10 ** 5)
    v = math.sqrt(mu / r)
    return v

class Application(tk.Frame):
    def _init_(self, master=None):
        super()._init_(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Orbital Speed Calculator")
        self.label.pack()

        self.radius_label = tk.Label(self, text="Enter the radius (in km):")
        self.radius_label.pack()

        self.radius_entry = tk.Entry(self)
        self.radius_entry.pack()

        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def calculate(self):
        r = float(self.radius_entry.get())
        v = calculate_the_orbital_speed(r)
        self.result_label.config(text=f"The orbital speed is {v:.2f} km/s")

root = tk.Tk()
app = Application(master=root)
app.mainloop()