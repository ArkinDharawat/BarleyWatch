from Tkinter import * #For GUI

CITY = ""
DATE = ""
BUTTON_HIT = False

class starter_window:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.master.geometry('%dx%d+%d+%d' % (self.screen_width,self.screen_height, 0, 0))

        self.master.wm_title("Login Window")

        #Quit and Go buttons
        self.Quit=Button(self.frame,text="Quit",command=self.close_windows)
        self.Quit.grid(row=1,column=0)

        self.Go=Button(self.frame,text="Go",command=self.Go)
        self.Go.grid(row=1,column=3)

        #Port selection
        self.L1=Label(self.frame,text="Enter Name")
        self.L1.grid(row=0,column=0)

        #self.V1=StringVar(self.frame)
        self.E1 = Entry(self.frame)
        self.E1.grid(row=0,column=1)


        #Baudrate selection
        self.L2=Label(self.frame,text="Enter Password")
        self.L2.grid(row=1,column=0)

        #self.V2=StringVar(self.frame)
        self.E2 = Entry(self.frame)
        self.E2.grid(row=1,column=1)


        #final window configuration
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.frame.grid()

    def close_windows(self):
        self.master.destroy()

    def Go(self):
        global CITY
        global DATE
        global BUTTON_HIT
        BUTTON_HIT = True
        C,D=self.E1.get(),self.E2.get()
        if C=="":
            CITY=""
            self.close_windows()
        elif D=="":
            DATE=""
            self.close_windows()
        else:
            CITY,DATE = self.E1.get(),self.E2.get()
            self.master.destroy()
def main():
    Root=Tk()
    app = starter_window(Root)
    Root.mainloop()
    return BUTTON_HIT,CITY,DATE
