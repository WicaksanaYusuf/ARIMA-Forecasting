from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from os import path
import shutil

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title('ARIMA Prototype')
        self.minsize(640,400)
        self.geometry("320x400")
        self.wm_iconbitmap('assets/favicon.ico')

        self.AppLabel = ttk.Label(self,text="Forecasting Produksi Sparepart",font=("Arial",18))
        self.AppLabel.pack()
        self.FileLabel = ttk.LabelFrame(self,text="Unggah file: *csv")
        self.FileLabel.pack(padx=5,pady=1)

        self.DeleteFile = ttk.Button(self,text="Delete File",command=self.deleteFile)
        self.DeleteFile.pack()

        orderLabel = ttk.Label(self, text="Order:")
        orderLabel.pack()
        entry1 = ttk.Entry(self, width="5")
        entry1.pack()

        entry2 = ttk.Entry(self, width="5")
        entry2.pack()

        entry3 = ttk.Entry(self, width="5")
        entry3.pack()


        submitButton = ttk.Button(self,text="Submit",command=lambda : self.submitProgram(entry1.get(),entry2.get(),entry3.get()))
        submitButton.pack()

        self.buttonBrowseFile()

    def buttonBrowseFile(self):
        self.buttonBrowse = ttk.Button(self.FileLabel,text="Browse", command=self.fileDialog)
        self.buttonBrowse.pack()

    def deleteFile(self):
        shutil.rmtree('csv')

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/csv", title="Select a File", filetypes = (("CSV Files","*.csv"),))
        self.label = ttk.Label(self.FileLabel,text="")
        self.label.pack()
        self.label.configure(text = self.filename)

        if path.exists('csv/'+self.filename):
            shutil.copy(self.filename,'csv')
        else:
            shutil.copy(self.filename,'csv')



    def submitProgram(self,order1,order2,order3):
        print("test")

if __name__ == "__main__":
    root = Root()
    root.mainloop()