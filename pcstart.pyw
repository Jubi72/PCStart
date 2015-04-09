######################################
# Startprogramm für den PC           #
# Erstellt 09.04.2015 Julius Bittner #
# zuletzt geändert ebenso            #
######################################

import tkinter as tk
import os

class Gui:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Willkommen, %s!" % os.getlogin())
        self.root.config(bg="#bbe6ff")
        
        self.root.bind("<Button>",lambda event:self.root.destroy())

        b, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.overrideredirect(1)
        self.root.geometry("%sx%s+0+0" % (b, h))

        self.root.mainloop()

start = Gui()
