# Matt Cherry - Senior Design 582  - Autofarm OS GUI

from tkinter import *

class AutoFarmGUI:
    def __init__(self):
        self.started = False
        self.window = Tk()
    def setup(self):
        # Window is a Tk object that will represent the current window.
        # mainloop() is what keeps the image on screen
        self.window.title("Autofarm OS Readings")

        # Five different statistics we initially care about
        # 1. PPM 2. Temperature 3. pH 4. PAR wavelength 5. Humidity
        label_PPM = Label(self.window, text="PPM: 0", font=("Arial", 16))
        label_PPM.grid(column=0, row=0)

        self.label_Temp = Label(self.window, text="Temperature: 20.4 C", font=("Arial", 16))
        self.label_Temp.grid(column=0, row=1)

        self.label_pH = Label(self.window, text="pH: 10.7", font=("Arial", 16))
        self.label_pH.grid(column=0, row=2)

        label_PAR = Label(self.window, text="Wavelength: 1208 ", font=("Arial", 16))
        label_PAR.grid(column=0, row=3)

        self.label_Humidity = Label(self.window, text="Humidity: 47.15%", font=("Arial", 16))
        self.label_Humidity.grid(column=0, row=4)
        
        label_liquid_level = Label(self.window, text="Liquid Level: Needs Refill", font=("Arial", 16))
        label_liquid_level.grid(column=0, row=5)
        
        self.label_datetime = Label(self.window, text = "Date/Time: ", font = ("Arial", 16))
        self.label_datetime.grid(column=0, row=6)
        #
    def after(self,ms, func):
        self.window.after(ms, func)
    def configureTemp(self,temp):
        self.label_Temp.configure(text=temp)
    def configurepH(self,ph):
        self.label_pH.configure(text=ph)
    def configureHumidity(self,hum):
        self.label_Humidity.configure(text=hum)
    def configureDateTime(self,time):
        self.label_datetime.configure(text=time)
    def destroy(self):
        self.window.destroy()
    def quit(self):
        self.window.quit()
    def run(self):
        self.window.mainloop()



