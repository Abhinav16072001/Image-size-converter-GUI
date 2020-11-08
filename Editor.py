from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from PIL import ImageTk, Image
import cv2

window=Tk()
window.title("Editor")
window.geometry("600x600")
color="#D3D3D3"
btn_color="#A9A9A9"
window.configure(bg=color)
window.resizable(width=False,height=False)
window.focus_force()
window.iconbitmap('sa.ico')

frame1=Frame(window,height=280,bg=color)
frame1.pack(side=BOTTOM)

global filename
def browseFiles():
    try:
        filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      ("*.png*","*.jpeg*","*.jpg*")),
                                                     ("all files",
                                                      "*.*")))
        e1.insert(0,filename)
        x=filename
        img = Image.open(x)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(frame1, image=img)
        panel.pack()
        panel.image = img
        panel.pack()
    except:
        pass

    try:
        im = cv2.imread(filename)
        w,h,c = im.shape
        s1 = Label(window, text="Width", bg=color).place(x=100, y=200)

        s2 = Label(window, text="Height", bg=color).place(x=100, y=240)
        ss1 = Label(window, text=w).place(x=160, y=200)
        Label(window, text="to", bg=color).place(x=190, y=200)
        ss2 = Label(window, text=h).place(x=160, y=240)
        Label(window, text="to", bg=color).place(x=190, y=240)

        se1=Entry(window,width=4)
        se1.place(x=220, y=200)


        se2=Entry(window,width=4)
        se2.place(x=220, y=240)
        global hh,ww
        hh=se2.get()
        ww = se1.get()

    except:pass

    def ss():
        name=asksaveasfilename(initialfile='Untitled.png',
                                            defaultextension=".png",
                                            filetypes=[("All Files", "*.*"),
                                                       ("photos", "*.png")])


        try:
            hh = se2.get()
            ww = se1.get()
            hhh=int(hh)
            www=int(ww)

        except:
            messagebox.showinfo("Error","Invalid Input!!")

        img = Image.open(filename)  # images are color images
        img = img.resize((www,hhh ), Image.ANTIALIAS)
        img.save(name)

    def cc():
        frame1.forget()
        se1.delete(0, END)
        se2.delete(0, END)
        e1.delete(0, END)




    go = Button(window, text="GO",width=10, bg=btn_color, command=lambda :[ss(),cc()])
    go.place(x=400, y=200)




Label(window,text="Image Size Converter",font=("Helvetica",40),padx=45).pack(side=TOP)

b=Label(window,text="Select File",bg=color).place(x=120,y=100)
e1=Entry(window,width=40)
e1.place(x=180,y=100)
button_explore = Button(window,width=8,text="Browse",bg=btn_color,command=browseFiles)
button_explore.place(x=430,y=96)

s1 = Label(window, text="Width", bg=color).place(x=100, y=200)

s2 = Label(window, text="Height", bg=color).place(x=100, y=240)
ss1 = Label(window, text="0").place(x=160, y=200)

ss2 = Label(window, text="0").place(x=160, y=240)



mainloop()