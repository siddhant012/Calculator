import tkinter
from tkinter import font
from tkinter import PhotoImage



class Window():

    def create_window(self,title,dimension,icon):
        self.window_obj=tkinter.Tk()
        self.window_obj.title(title)
        self.window_obj.geometry(dimension)
        self.window_obj.wm_iconbitmap(icon)

    def __init__(self,title,dimension,icon):
        self.title=title
        self.dimension=dimension
        self.icon=icon
        self.create_window(title,dimension,icon)
        self.frames=[]
        self.buttons=[]
        self.labels=[]
        self.entrys=[]


fonts=[]
images=[]
exp_str=""
flag=0
def create_fonts():
    global fonts
    fonts.append(tkinter.font.Font(family='Helvetica', size=20, weight='bold'))
    fonts.append(tkinter.font.Font(family='Helvetica', size=45))

def create_images():
    global images
    images.append(PhotoImage(file=r"H:\calculator icons\0.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\1.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\2.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\3.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\4.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\5.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\6.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\7.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\8.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\9.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\plus.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\minus.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\cross.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\divide.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\dot.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\equals.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\underroot.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\cuberoot.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\exponent.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\percentage.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\open_br.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\closed_br.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\back.png"))
    images.append(PhotoImage(file=r"H:\calculator icons\clear.png"))



def insert_in_entry(str,entry_obj):
    global exp_str
    global flag

    if(flag==1 and str in ('0','1','2','3','4','5','6','7','8','9','.')):
        clear_entry(entry_obj)
        flag=0
    elif(flag==1 and str not in('0','1','2','3','4','5','6','7','8','9','.')):
        flag=0
    exp_str+=str
    entry_obj.delete(first=0,last="end")
    entry_obj.insert(0,exp_str)


def evaluate(entry_obj):
    update_exp_str(entry_obj)
    global exp_str
    global flag
    exp_str=str(eval(exp_str))
    entry_obj.delete(first=0,last="end")
    entry_obj.insert(0,exp_str)
    flag=1

def clear_entry(entry_obj):
    global exp_str
    entry_obj.delete(first=0,last="end")
    exp_str=""
    entry_obj.insert(0,"")

def pop_from_entry(entry_obj):
    global exp_str
    exp_str=exp_str[:len(exp_str)-1]
    entry_obj.delete(first=0,last="end")
    entry_obj.insert(0,exp_str)

def update_exp_str(entry_obj):
    global exp_str
    exp_str=entry_obj.get()






def main():
    window1=Window("MyCalculator","1200x600","H:/calculator icons/calculator icon.ico")

    global fonts
    global exp_str
    create_fonts()
    create_images()


    window1.frames.append( tkinter.Frame(height=200,width=1200) )
    window1.frames.append( tkinter.Frame(height=100,width=1200) )
    window1.frames.append( tkinter.Frame(height=100,width=1200) )
    window1.frames.append( tkinter.Frame(height=100,width=1200) )
    window1.frames.append( tkinter.Frame(height=100,width=1200) )

    window1.buttons.append( tkinter.Button(window1.frames[4],height=100,width=200,image=images[18],command=lambda:insert_in_entry('**',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[4],height=100,width=200,image=images[1],command=lambda:insert_in_entry('1',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[4],height=100,width=200,image=images[2],command=lambda:insert_in_entry('2',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[4],height=100,width=200,image=images[3],command=lambda:insert_in_entry('3',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[4],height=100,width=200,image=images[0],command=lambda:insert_in_entry('0',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[4],height=100,width=200,image=images[15],command=lambda:evaluate(window1.entrys[0]),bd=5) )

    window1.buttons.append( tkinter.Button(window1.frames[3],height=100,width=200,image=images[17],command=lambda:insert_in_entry('**(1/3)',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[3],height=100,width=200,image=images[4],command=lambda:insert_in_entry('4',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[3],height=100,width=200,image=images[5],command=lambda:insert_in_entry('5',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[3],height=100,width=200,image=images[6],command=lambda:insert_in_entry('6',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[3],height=100,width=200,image=images[12],command=lambda:insert_in_entry('*',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[3],height=100,width=200,image=images[13],command=lambda:insert_in_entry('/',window1.entrys[0]),bd=5) )

    window1.buttons.append( tkinter.Button(window1.frames[2],height=100,width_=200,image_=images[16],command=lambda:insert_in_entry('**(1/2)',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[2],height=100,width_=200,image_=images[7],command=lambda:insert_in_entry('7',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[2],height=100,width_=200,image_=images[8],command=lambda:insert_in_entry('8',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[2],height=100,width_=200,image_=images[9],command=lambda:insert_in_entry('9',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[2],height=100,width_=200,image_=images[10],command=lambda:insert_in_entry('+',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[2],height=100,width_=200,image_=images[11],command=lambda:insert_in_entry('-',window1.entrys[0]),bd=5) )

    window1.buttons.append( tkinter.Button(window1.frames[1],height=100,width=200,image=images[19],command=lambda:insert_in_entry('%',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[1],height=100,width=200,image=images[20],command=lambda:insert_in_entry('(',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[1],height=100,width=200,image=images[21],command=lambda:insert_in_entry(')',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[1],height=100,width=200,image=images[14],command=lambda:insert_in_entry('.',window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[1],height=100,width=200,image=images[22],command=lambda:pop_from_entry(window1.entrys[0]),bd=5) )
    window1.buttons.append( tkinter.Button(window1.frames[1],height=100,width=200,image=images[23],command=lambda:clear_entry(window1.entrys[0]),bd=5) )

    window1.entrys.append( tkinter.Entry(window1.frames[0],width=36,font=fonts[1],relief=tkinter.FLAT,justify=tkinter.RIGHT) )
    window1.entrys[0].insert(0,exp_str)


    window1.frames[0].pack(side=tkinter.TOP)
    window1.frames[1].pack(side=tkinter.TOP)
    window1.frames[2].pack(side=tkinter.TOP)
    window1.frames[3].pack(side=tkinter.TOP)
    window1.frames[4].pack(side=tkinter.TOP)

    window1.buttons[0].place(x=0,y=0)
    window1.buttons[1].place(x=200,y=0)
    window1.buttons[2].place(x=400,y=0)
    window1.buttons[3].place(x=600,y=0)
    window1.buttons[4].place(x=800,y=0)
    window1.buttons[5].place(x=1000,y=0)

    window1.buttons[6].place(x=0,y=0)
    window1.buttons[7].place(x=200,y=0)
    window1.buttons[8].place(x=400,y=0)
    window1.buttons[9].place(x=600,y=0)
    window1.buttons[10].place(x=800,y=0)
    window1.buttons[11].place(x=1000,y=0)

    window1.buttons[12].place(x=0,y=0)
    window1.buttons[13].place(x=200,y=0)
    window1.buttons[14].place(x=400,y=0)
    window1.buttons[15].place(x=600,y=0)
    window1.buttons[16].place(x=800,y=0)
    window1.buttons[17].place(x=1000,y=0)

    window1.buttons[18].place(x=0,y=0)
    window1.buttons[19].place(x=200,y=0)
    window1.buttons[20].place(x=400,y=0)
    window1.buttons[21].place(x=600,y=0)
    window1.buttons[22].place(x=800,y=0)
    window1.buttons[23].place(x=1000,y=0)

    window1.entrys[0].place(x=0,y=75)

    window1.window_obj.mainloop()



if __name__ == '__main__':
    main()


