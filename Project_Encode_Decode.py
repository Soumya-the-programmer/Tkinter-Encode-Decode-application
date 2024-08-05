from tkinter import *# importing tkinter module to generate the GUI window
import tkinter.messagebox as tmsg# importing messagebox to show the message to the user
import random# importing random module to generate random values
root=Tk()# Tk() class instance
# encode() function to generate the encode and decode window
def edcode():
    # text encryption done using this encode_text() function
    def encode_text():
        n=valentry.get()
        # using list to generate random values
        li=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
            'P','Q','R','S','T','U','V','W','X','Y','Z']
        # using Dictionary to encrypt the key into the corresponding value
        l={'a':"1",'b':"2",'c':"3",'d':"4",'e':"5",'f':"6",'g':"7",'h':"8",
           'i':"9",'j':"A",'k':"B",'l':"C",'m':"D",'n':"E",'o':"F",'p':"G",
           'q':"H",'r':"I",'s':"J",'t':"K",'u':"L",'v':"M",'w':"N",'x':"O",
           'y':"P",'z':"Q"," ":"#","_":"%","-":"@","1":"a",'2':'b','3':'c',
           '4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','0':'j','!':'k',
           '@':'l','#':'m','$':'n','%':'o','^':'p','&':'q','*':'r','(':'s',
           ')':'t','=':'u','+':'v','~':'w',',':'x','.':'y','/':'z','?':';',
           '<':':','>':'\'','\\':'/','\'':'~','\"':"`",'`':'\"',':':'!',';':'@',
           '|':'#','{':'$','}':'%','[':'^',']':'&'}   
        
        sn=n.lower()# converting the entered text into lower to match with the dictionary key
        hs=''# empty string to store the encode text for less than < 3 length words
        hs1=''# empty string to store the encode text for greater than > 3 length words
        w=''# empty string to store one by one character for less than < 3 length words
        w1=''# empty string to store one by one character for greater than > 3 length words
        fs=''# empty string to store the first character of the word for the greater than > 3 length words
        
        # encryption condition for less than 3 length words
        if(len(sn)<3):
            for i in range(len(sn)-1,-1,-1):# loop starts from the end index to starting index
                w=sn[i] # collecting each character
                hs=hs+l[w] # storing each character
            text_output.insert(END,f"{hs}") # inserting the encrypted text into text box
        # encryption condition for greater than 3 length words
        else:
            for i in range(1,len(sn)):# loop starts from the starting index to len(string)-1
                w1=sn[i] # collecting each character
                hs1=hs1+l[w1] # storing each character
            fs=sn[0] # storing the first character
            hs1=hs1+l[fs] # storing the whole encrypted word with the first character 
            # rn is a string used to store the encrypted string with 6 random generated characters from the list li[]
            rn=(f"{random.choice(li)}{random.choice(li)}{random.choice(li)}{hs1}{random.choice(li)}{random.choice(li)}{random.choice(li)}")
            text_output.insert(END,f"{rn}")# after encoding the whole text inserting the text into the text box
    # text decryption done using this decode_text() function
    def decode_text():
        n1=de_valentry.get()# n1 variable to get the value from the entry widget
        # l{} dictionary to find the decrypted value from the key
        l={'a':"1",'b':"2",'c':"3",'d':"4",'e':"5",'f':"6",'g':"7",'h':"8",'i':"9",
           'j':"A",'k':"B",'l':"C",'m':"D",'n':"E",'o':"F",'p':"G",'q':"H",'r':"I",
           's':"J",'t':"K",'u':"L",'v':"M",'w':"N",'x':"O",'y':"P",'z':"Q"," ":"#",
           "_":"%","-":"@","1":"a",'2':'b','3':'c','4':'d','5':'e','6':'f','7':'g',
           '8':'h','9':'i','0':'j','!':'k','@':'l','#':'m','$':'n','%':'o','^':'p',
           '&':'q','*':'r','(':'s',')':'t','=':'u','+':'v','~':'w',',':'x','.':'y',
           '/':'z','?':';','<':':','>':'\'','\\':'/','\'':'~','\"':"`",'`':'\"',':':'!',
           ';':'@','|':'#','{':'$','}':'%','[':'^',']':'&'}   
        
        st=n1.lower()# converting the getting text into lower for matching with dictionary key
        dn=''# empty string to store the decrypted text for the input text when length is greater than 3
        ns=''# empty string to store the decrypted text for the input text when length is greater than 3 
            #  and storing only starting length to length(string)-1 string
        os=''# empty string to concatenate the last word and total word of string
        k=''# empty string to collect the character from the word when length is lesser than 3
        dv=''# storing the decrypted text for the input text when length is lesser than 3
        k2=''# empty string to collect the character from the word when length is greater than 3
        k3=''# empty string to store the last character of the word
        
        # condition for less than 3 length string
        if (len(n1)<3): 
            for i in range(len(st)-1,-1,-1): # loop starts from len(string)-1 to starting index 
                k=st[i]# collecting each character from the string
                dsv=list(l.keys())[list(l.values()).index(f"{k}")] # matching the value k with the dictionary key and finding the value          
                dv=dv+dsv # storing every characters in dv
                dsv=None # declaring the dsv None to empty the variable
            de_text_output.insert(END,f"{dv.upper()}")# inserting the decrypted text into the text box
        # condition for greater than 3 length string
        else:
            for i in range(3,len(n1)-3): # loop starts from 3 index to len(string)-3 index to extract random values
                k2=n1[i]# collecting each character
                dsv2=list(l.keys())[list(l.values()).index(f"{k2}")] # matching the value k with the dictionary key and finding the value
                dn=dn+dsv2 # storing every characters in dn
                dsv2=None # declaring the dsv None to empty the variable  
            for i in range(0,len(dn)-1): # loop starts from 0 index to (end-1) length
                ns=ns+dn[i] # collecting and storing the decrypted string here extracting last character 
            k3=dn[len(dn)-1] # storing the last character here
            os=k3+ns # concatenating the whole string with last character
            de_text_output.insert(END,f"{os.upper()}") # inserting the upper decrypted text into the text box
    p=var.get() # getting the radiobutton input
    if (p=="Encode"): # if user click on encode this will execute
        #Encoding window
        encode_panel=Toplevel(root)# using Toplevel() to collecting the main window instance
        encode_panel.title("ENCODE PANEL") # title for encode window
        encode_panel.iconbitmap("c:\\Users\\user\\Downloads\\keyiconimg.ico") # icon for encode window
        encode_panel.geometry("550x550") # declaring the size
        encode_panel.maxsize(550,550) # fixing max size
        encode_panel.minsize(550,550) # fixing min size
        enupperframe=Frame(encode_panel,bg="maroon1",pady=30,borderwidth=4,relief="groove") # upper frame
        enupperframe.pack(fill=X)
        # heading
        enheading=Label(enupperframe,text="ENCODE TEXT",font=("poppins",18,"bold","underline"),justify="center")
        enheading.pack()
        # frame 2
        enupframe=Frame(encode_panel,bg="orchid1",borderwidth=4,relief='flat',pady=40)
        enupframe.pack(anchor="n",fill=X,side="top")
        #label
        enword_label=Label(enupframe,text="Enter the word:\t",font=("poppins",18,'bold'),bg="orchid1",fg="black",justify="left")
        enword_label.pack(anchor="w",side="left")
        val=StringVar()# declaring val as StringVar() variable
        valentry=Entry(enupframe,textvariable=val,width=20,font=("poppins",20,"bold"))# Entry widget
        valentry.pack()
        enlowerbody=Frame(encode_panel,bg="orchid1")# frame 3
        enlowerbody.pack(fill=BOTH)
        f=Label(enlowerbody,text="",bg="orchid1")# show label to create space
        f.pack()
        # submit button
        en_submit=Button(enlowerbody,text="Submit",bg="brown1",fg="white",font=("poppins",14,"bold"),padx=15,pady=8,command=encode_text)
        en_submit.pack(anchor="s")
        # label
        f1=Label(enlowerbody,text="\n Output:\n",bg="orchid1",font=("poppins",18,'bold'),justify="left")
        f1.pack(anchor="w",side="left")
        enlowerbody_res=Frame(encode_panel,bg="orchid1")# frame 4
        enlowerbody_res.pack(fill=BOTH) 
        scbar=Scrollbar(enlowerbody_res) # scrollbar to scroll in text window
        scbar.pack(anchor="e",side="right",fill=Y)
        # text window
        text_output=Text(enlowerbody_res,font=("poppins",12,"bold"),width=55,height=5,yscrollcommand=scbar.set)
        text_output.pack(anchor='center')
        # show label to create space
        f2=Label(enlowerbody_res,text="\n\n\n\n",bg="orchid1")
        f2.pack()
        encode_panel.mainloop()# declaring mainloop() to execute the window
    # if user click on decode this will execute
    elif (p=="Decode"):
        # decoding window
        decode_panel=Toplevel(root)# using Toplevel() to collecting the main window instance
        decode_panel.title("DECODE PANEL")# title
        decode_panel.iconbitmap("c:\\Users\\user\\Downloads\\keyiconimg.ico") # icon for decode window
        decode_panel.geometry("550x550")# declaring the size
        decode_panel.maxsize(550,550)# fixing max size
        decode_panel.minsize(550,550)# fixing min size
        deupperframe=Frame(decode_panel,bg="maroon1",pady=30,borderwidth=4,relief="groove")# frame 1
        deupperframe.pack(fill=X)
        # Heading
        deheading=Label(deupperframe,text="DECODE TEXT",font=("poppins",18,"bold","underline"),justify="center")
        deheading.pack()
        # frame 2
        deupframe=Frame(decode_panel,bg="orchid1",borderwidth=4,relief='flat',pady=40)
        deupframe.pack(anchor="n",fill=X,side="top")
        # label
        deword_label=Label(deupframe,text="Enter the word:\t",font=("poppins",18,'bold'),bg="orchid1",fg="black",justify="left")
        deword_label.pack(anchor="w",side="left")
        de_val=StringVar() # de_val is a sting type variable
        de_valentry=Entry(deupframe,textvariable=de_val,width=20,font=("poppins",20,"bold"))# entry
        de_valentry.pack()
        delowerbody=Frame(decode_panel,bg="orchid1")#frame 3
        delowerbody.pack(fill=BOTH)
        de_f=Label(delowerbody,text="",bg="orchid1")# show label to create space
        de_f.pack()
        # submit button
        de_submit=Button(delowerbody,text="Submit",bg="brown1",fg="white",font=("poppins",14,"bold"),padx=15,pady=8,command=decode_text)
        de_submit.pack(anchor="s")
        # label
        de_f1=Label(delowerbody,text="\n Output:\n",bg="orchid1",font=("poppins",18,'bold'),justify="left")
        de_f1.pack(anchor="w",side="left")
        # frame 4
        delowerbody_res=Frame(decode_panel,bg="orchid1")
        delowerbody_res.pack(fill=BOTH) 
        de_scbar=Scrollbar(delowerbody_res) #scroll bar to scroll in text box
        de_scbar.pack(anchor="e",side="right",fill=Y)
        # text box
        de_text_output=Text(delowerbody_res,font=("poppins",12,"bold"),width=55,height=5,yscrollcommand=de_scbar.set)
        de_text_output.pack(anchor='center')
        # show label to create space
        de_f2=Label(delowerbody_res,text="\n\n\n\n",bg="orchid1")
        de_f2.pack()
        decode_panel.mainloop()# declaring mainloop() to execute the window
    # if no option is selected execute this 
    else:
        tmsg.showerror("Error!","You did not choose any option!")# showing the error message
# rmessage() to show thanks message after rating
def rmessage():
    tmsg.showinfo("Thank You!","Thank You! for your rating :)")# showing the message
# about_us() to show about us
def about_us():
    tmsg.showinfo("About Us","This GUI application is made by Soumyajeet Das.\nIt is created using tkinter module in Python.\nDate: 05/07/2024")
#rate_us() window
def rate_us():
    rate_window=Toplevel(root)# using Toplevel() to collecting the main window instance
    rate_window.title("Rate Us")# title
    rate_window.iconbitmap("c:\\Users\\user\\Downloads\\keyiconimg.ico") # icon for rate window
    rate_window.geometry("300x275")# declaring the size
    rate_window.maxsize(300,275)# fixing max size
    rate_window.minsize(300,275)# fixing min size
    uframe=Frame(rate_window,bg="seagreen1",pady=20,borderwidth=4,relief="groove")# frame 1
    uframe.pack(fill=X)
    # heading
    title=Label(uframe,text="Rate us here please",font=("poppins",15,"bold"),bg="white",fg="black")# label
    title.pack()
    lframe=Frame(rate_window,bg="aquamarine2",pady=20,borderwidth=4,relief="groove")# frame 2
    lframe.pack(fill=X)
    # scale for rating
    rate_scale=Scale(lframe,from_=0, to=100, orient="horizontal",sliderlength=5,sliderrelief="sunken",tickinterval=50,bg="aquamarine2",borderwidth=2,relief="solid",font=("poppins",10,"bold"))
    rate_scale.set(50)# setting scale to 50 position
    rate_scale.pack()
    f_label=Label(lframe,text="\n",bg='aquamarine2')# show label to create space
    f_label.pack()
    # submit button
    s_button=Button(lframe,text="Submit",borderwidth=2,relief="solid",font=("poppins",10,"bold"),padx=10,pady=10,bg="brown1",fg="white",command=rmessage)
    s_button.pack()
    rate_window.mainloop()# declaring mainloop() to execute the window
root.title("SECRET CODE CONVERTER") # title
root.geometry("450x475")# declaring size
root.maxsize(450,475)# fixing max size
root.minsize(450,475)# fixing min size
root.iconbitmap("c:\\Users\\user\\Downloads\\keyiconimg.ico")# icon
helpmenu=Menu(root)# help menu
hmenu=Menu(helpmenu,tearoff=0)# sub menu of help menu
hmenu.add_command(label="Rate Us!",command=rate_us)# options of help menu
hmenu.add_command(label="About Us",command=about_us)# options of help menu
root.config(menu=helpmenu)# config the help menu
upperframe=Frame(root,bg="cyan2",borderwidth=4,relief='groove',pady=20)# frame 1
upperframe.pack(anchor="n",side="top",fill=X)
# Heaind label
heading=Label(upperframe,text="SECRET CODE CONVERTER",font=("poppins",20,"bold","underline"),justify="center")
heading.pack()
# add_cascade the help menu here
helpmenu.add_cascade(label="Help",menu=hmenu)
# frame 2
bodyframe=Frame(root,bg="cadetblue1",borderwidth=2,relief='flat')#frame 2
bodyframe.pack(fill=BOTH)
# label
body=Label(bodyframe,text="\n\n\nChoose any option below:\n\n",bg="cadetblue1",fg="black",justify="left",font=("Times of roman",18,"bold"))
body.pack(anchor="nw")
var=StringVar() # declaring the variable as string type
var.set("Nothing") # setting as nothing
# radiobutton for encode option
r1=Radiobutton(bodyframe,text="Encode\t\t",variable=var,value="Encode",font=("poppins",20,"bold"),bg="cadetblue1",fg="blue1")
r1.pack(anchor="ne",side="left")
# radiobutton for decode option
r2=Radiobutton(bodyframe,text="Decode",variable=var,value="Decode",font=("poppins",20,"bold"),bg="cadetblue1",fg="blue1")
r2.pack(anchor="sw",side="bottom")
lowerbody=Frame(root,bg="cadetblue1")#frame 3
lowerbody.pack(fill=BOTH)
fake=Label(lowerbody,text="\n\n",bg="cadetblue1")# show label to create empty space
fake.pack()
# submit button
submit=Button(lowerbody,text="Submit",bg="brown1",fg="white",font=("poppins",14,"bold"),padx=15,pady=8,command=edcode)
submit.pack(anchor="s")
# show label to create empty space
show1=Label(lowerbody,text="\n\n\n",bg="cadetblue1")
show1.pack(fill=BOTH)
root.mainloop()# declaring mainloop() to execute the window