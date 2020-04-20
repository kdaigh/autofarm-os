# Matt Cherry - Senior Design 582  - Autofarm OS GUI


from tkinter import *

class AutoFarmGUI:
    def __init__(self):
        self.started = FALSE
        self.window = Tk()
    def setup(self):
        # Window is a Tk object that will represent the current window.
        # mainloop() is what keeps the image on screen
        self.window.title("Autofarm OS Readings")

        # Five different statistics we initially care about
        # 1. PPM 2. Temperature 3. pH 4. PAR wavelength 5. Humidity
        label_PPM = Label(self.window, text="PPM: ", font=("Arial", 16))
        label_PPM.grid(column=0, row=0)

        label_Temp = Label(self.window, text="Temperature: ", font=("Arial", 16))
        label_Temp.grid(column=0, row=1)

        label_pH = Label(self.window, text="pH: ", font=("Arial", 16))
        label_pH.grid(column=0, row=2)

        label_PAR = Label(self.window, text="Wavelength: ", font=("Arial", 16))
        label_PAR.grid(column=0, row=3)

        label_Humidity = Label(self.window, text="Humidity: ", font=("Arial", 16))
        label_Humidity.grid(column=0, row=4)

        #
    def run(self):
        self.window.mainloop()
x = AutoFarmGUI()
x.setup()
x.run()


