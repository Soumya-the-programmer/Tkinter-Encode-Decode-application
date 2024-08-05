from tkinter import *
import tkinter.messagebox as tmsg
import random
root=Tk()
def edcode():
    def encode_text():
        n=valentry.get()
        li=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        l={'a':"1",'b':"2",'c':"3",'d':"4",'e':"5",'f':"6",'g':"7",'h':"8",'i':"9",'j':"A",'k':"B",'l':"C",'m':"D",'n':"E",'o':"F",'p':"G",'q':"H",'r':"I",'s':"J",'t':"K",'u':"L",'v':"M",'w':"N",'x':"O",'y':"P",'z':"Q"," ":"#","_":"%","-":"@","1":"a",'2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','0':'j','!':'k','@':'l','#':'m','$':'n','%':'o','^':'p','&':'q','*':'r','(':'s',')':'t','=':'u','+':'v','~':'w',',':'x','.':'y','/':'z','?':';','<':':','>':'\'','\\':'/','\'':'~','\"':"`",'`':'\"',':':'!',';':'@','|':'#','{':'$','}':'%','[':'^',']':'&'}   
        sn=n.lower()
        hs=''
        hs1=''
        w=''
        w1=''
        fs=''
        if(len(sn)<3):
            for i in range(len(sn)-1,-1,-1):
                w=sn[i] 
                hs=hs+l[w]
            text_output.insert(END,f"{hs}")
        else:
            for i in range(1,len(sn)):
                w1=sn[i]
                hs1=hs1+l[w1]
            fs=sn[0]
            hs1=hs1+l[fs]
            rn=(f"{random.choice(li)}{random.choice(li)}{random.choice(li)}{hs1}{random.choice(li)}{random.choice(li)}{random.choice(li)}")
            text_output.insert(END,f"{rn}")
    def decode_text():
        n1=de_valentry.get()
        l={'a':"1",'b':"2",'c':"3",'d':"4",'e':"5",'f':"6",'g':"7",'h':"8",'i':"9",'j':"A",'k':"B",'l':"C",'m':"D",'n':"E",'o':"F",'p':"G",'q':"H",'r':"I",'s':"J",'t':"K",'u':"L",'v':"M",'w':"N",'x':"O",'y':"P",'z':"Q"," ":"#","_":"%","-":"@","1":"a",'2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','0':'j','!':'k','@':'l','#':'m','$':'n','%':'o','^':'p','&':'q','*':'r','(':'s',')':'t','=':'u','+':'v','~':'w',',':'x','.':'y','/':'z','?':';','<':':','>':'\'','\\':'/','\'':'~','\"':"`",'`':'\"',':':'!',';':'@','|':'#','{':'$','}':'%','[':'^',']':'&'}   
        st=n1.lower()
        dn=''
        ns=''
        os=''
        k=''
        dv=''
        k2=''
        k3=''
        if (len(n1)<3): 
            for i in range(len(st)-1,-1,-1):      
                k=st[i]
                dsv=list(l.keys())[list(l.values()).index(f"{k}")]          
                dv=dv+dsv
                dsv=None
            de_text_output.insert(END,f"{dv.upper()}")
        else:
            for i in range(3,len(n1)-3):
                k2=n1[i]
                dsv2=list(l.keys())[list(l.values()).index(f"{k2}")]
                dn=dn+dsv2
                dsv2=None
                print(dn)
            for i in range(0,len(dn)-1):
                ns=ns+dn[i]
            k3=dn[len(dn)-1]
            os=k3+ns
            de_text_output.insert(END,f"{os.upper()}")        
    p=var.get()
    if (p=="Encode"):
        #Encoding
        encode_panel=Tk()
        encode_panel.title("ENCODE PANEL")
        encode_panel.geometry("550x550")
        encode_panel.maxsize(550,550)
        encode_panel.minsize(550,550)
        enupperframe=Frame(encode_panel,bg="maroon1",pady=30,borderwidth=4,relief="groove")
        enupperframe.pack(fill=X)
        enheading=Label(enupperframe,text="ENCODE TEXT",font=("poppins",18,"bold","underline"),justify="center")
        enheading.pack()
        enupframe=Frame(encode_panel,bg="orchid1",borderwidth=4,relief='flat',pady=40)
        enupframe.pack(anchor="n",fill=X,side="top")
        enword_label=Label(enupframe,text="Enter the word:\t",font=("poppins",18,'bold'),bg="orchid1",fg="black",justify="left")
        enword_label.pack(anchor="w",side="left")
        val=StringVar()
        valentry=Entry(enupframe,textvariable=val,width=20,font=("poppins",20,"bold"))
        valentry.pack()
        enlowerbody=Frame(encode_panel,bg="orchid1")
        enlowerbody.pack(fill=BOTH)
        f=Label(enlowerbody,text="",bg="orchid1")
        f.pack()
        en_submit=Button(enlowerbody,text="Submit",bg="brown1",fg="white",font=("poppins",14,"bold"),padx=15,pady=8,command=encode_text)
        en_submit.pack(anchor="s")
        f1=Label(enlowerbody,text="\n Output:\n",bg="orchid1",font=("poppins",18,'bold'),justify="left")
        f1.pack(anchor="w",side="left")
        enlowerbody_res=Frame(encode_panel,bg="orchid1")
        enlowerbody_res.pack(fill=BOTH) 
        scbar=Scrollbar(enlowerbody_res) 
        scbar.pack(anchor="e",side="right",fill=Y)
        text_output=Text(enlowerbody_res,font=("poppins",12,"bold"),width=55,height=5,yscrollcommand=scbar.set)
        text_output.pack(anchor='center')
        f2=Label(enlowerbody_res,text="\n\n\n\n",bg="orchid1")
        f2.pack()
        encode_panel.mainloop()
    else:
        #decoding
        decode_panel=Tk()
        decode_panel.title("DECODE PANEL")
        decode_panel.geometry("550x550")
        decode_panel.maxsize(550,550)
        decode_panel.minsize(550,550)
        deupperframe=Frame(decode_panel,bg="maroon1",pady=30,borderwidth=4,relief="groove")
        deupperframe.pack(fill=X)
        deheading=Label(deupperframe,text="DECODE TEXT",font=("poppins",18,"bold","underline"),justify="center")
        deheading.pack()
        deupframe=Frame(decode_panel,bg="orchid1",borderwidth=4,relief='flat',pady=40)
        deupframe.pack(anchor="n",fill=X,side="top")
        deword_label=Label(deupframe,text="Enter the word:\t",font=("poppins",18,'bold'),bg="orchid1",fg="black",justify="left")
        deword_label.pack(anchor="w",side="left")
        de_val=StringVar()
        de_valentry=Entry(deupframe,textvariable=de_val,width=20,font=("poppins",20,"bold"))
        de_valentry.pack()
        delowerbody=Frame(decode_panel,bg="orchid1")
        delowerbody.pack(fill=BOTH)
        de_f=Label(delowerbody,text="",bg="orchid1")
        de_f.pack()
        de_submit=Button(delowerbody,text="Submit",bg="brown1",fg="white",font=("poppins",14,"bold"),padx=15,pady=8,command=decode_text)
        de_submit.pack(anchor="s")
        de_f1=Label(delowerbody,text="\n Output:\n",bg="orchid1",font=("poppins",18,'bold'),justify="left")
        de_f1.pack(anchor="w",side="left")
        delowerbody_res=Frame(decode_panel,bg="orchid1")
        delowerbody_res.pack(fill=BOTH) 
        de_scbar=Scrollbar(delowerbody_res) 
        de_scbar.pack(anchor="e",side="right",fill=Y)
        de_text_output=Text(delowerbody_res,font=("poppins",12,"bold"),width=55,height=5,yscrollcommand=de_scbar.set)
        de_text_output.pack(anchor='center')
        de_f2=Label(delowerbody_res,text="\n\n\n\n",bg="orchid1")
        de_f2.pack()
        decode_panel.mainloop()
def rmessage():
    tmsg.showinfo("Thank You!","Thank You! for your rating :)")
def about_us():
    tmsg.showinfo("About Us","This GUI application is made by Soumyajeet Das.\nIt is created using tkinter module in Python.\nDate: 05/07/2024")
def rate_us():
    rate_window=Tk()
    rate_window.title("Rate Us")
    rate_window.geometry("300x275")
    rate_window.maxsize(300,275)
    rate_window.minsize(300,275)
    uframe=Frame(rate_window,bg="seagreen1",pady=20,borderwidth=4,relief="groove")
    uframe.pack(fill=X)
    title=Label(uframe,text="Rate us here please",font=("poppins",15,"bold"),bg="white",fg="black")
    title.pack()
    lframe=Frame(rate_window,bg="aquamarine2",pady=20,borderwidth=4,relief="groove")
    lframe.pack(fill=X)
    rate_scale=Scale(lframe,from_=0, to=100, orient="horizontal",sliderlength=5,sliderrelief="sunken",tickinterval=50,bg="aquamarine2",borderwidth=2,relief="solid",font=("poppins",10,"bold"))
    rate_scale.set(50)
    rate_scale.pack()
    f_label=Label(lframe,text="\n",bg='aquamarine2')
    f_label.pack()
    s_button=Button(lframe,text="Submit",borderwidth=2,relief="solid",font=("poppins",10,"bold"),padx=10,pady=10,bg="brown1",fg="white",command=rmessage)
    s_button.pack()
    rate_window.mainloop()
root.title("SECRET CODE CONVERTER")
root.geometry("450x475")
root.maxsize(450,475)
root.minsize(450,475)
icon=PhotoImage(file="key_icon.png")
root.iconphoto(False,icon)
helpmenu=Menu(root)
hmenu=Menu(helpmenu,tearoff=0)
hmenu.add_command(label="Rate Us!",command=rate_us)
hmenu.add_command(label="About Us",command=about_us)
# hmenu.add_command(label="close",command=quit)
root.config(menu=helpmenu)
upperframe=Frame(root,bg="cyan2",borderwidth=4,relief='groove',pady=20)
upperframe.pack(anchor="n",side="top",fill=X)
heading=Label(upperframe,text="SECRET CODE CONVERTER",font=("poppins",20,"bold","underline"),justify="center")
heading.pack()
helpmenu.add_cascade(label="Help",menu=hmenu)
bodyframe=Frame(root,bg="cadetblue1",borderwidth=2,relief='flat')
bodyframe.pack(fill=BOTH)
body=Label(bodyframe,text="\n\n\nChoose any option below:\n\n",bg="cadetblue1",fg="black",justify="left",font=("Times of roman",18,"bold"))
body.pack(anchor="nw")
var=StringVar()
var.set("Nothing")
r1=Radiobutton(bodyframe,text="Encode\t\t",variable=var,value="Encode",font=("poppins",20,"bold"),bg="cadetblue1",fg="blue1")
r1.pack(anchor="ne",side="left")
r2=Radiobutton(bodyframe,text="Decode",variable=var,value="Decode",font=("poppins",20,"bold"),bg="cadetblue1",fg="blue1")
r2.pack(anchor="sw",side="bottom")
lowerbody=Frame(root,bg="cadetblue1")
lowerbody.pack(fill=BOTH)
fake=Label(lowerbody,text="\n\n",bg="cadetblue1")
fake.pack()
submit=Button(lowerbody,text="Submit",bg="brown1",fg="white",font=("poppins",14,"bold"),padx=15,pady=8,command=edcode)
submit.pack(anchor="s")
show1=Label(lowerbody,text="\n\n\n",bg="cadetblue1")
show1.pack(fill=BOTH)
root.mainloop()