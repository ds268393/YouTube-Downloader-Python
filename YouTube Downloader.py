import os
os.system('cmd /c "pip3.12 install moviepy"')
os.system('cmd /c "pip3.12 install gmail"')
os.system('cmd /c "pip3.12 install pytube"')
os.system('cmd /c "pip3.12 install pillow"')

#####The complete code: Assembly
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox
pass1=0
import re
def check_mail():
    id=email_input.get()
    pattern=re.compile("\w+\.?\w+@gmail.com")
    match=re.findall(pattern,id)
    if match:
        messagebox.showinfo('Valid ID','checking for app password')
        return login_handle()
    else:
        messagebox.showerror("Invalid Mail","Please Enter a valid gmail id")

def login_handle():
    global pass1
    import gmail
    id=email_input.get()
    password=apppass_input.get()
    try:
        connection=gmail.GMail(id,password)
        msg=gmail.Message(to=id,subject="Testt mail")
        connection.send(msg)
    except Exception as var:
        messagebox.showerror("Invalid Password","Please Enter a valid app password or check your internet connection")
    else:
        messagebox.showinfo("Login Successful","Sucessful Login!!")
        pass1=1
        root.destroy()
    
root=Tk()

root.title("Youtube Downloader")
root.iconbitmap('youtube.ico')
root.geometry('700x500')
root.configure(background='#FF0000') 

img=Image.open("yt_bg.png") 
resized_img=img.resize((280,80)) 

img=ImageTk.PhotoImage(resized_img)
img_label=Label(root,image=img)
img_label.pack(pady=(10,10))


text_label=Label(root,text="YouTube Downloader",fg="white",bg='#FF0000')
text_label.pack()
text_label.config(font=('verdana',24))

email_label=Label(root,text='Enter Your Gmail ID',fg='white',bg='#FF0000')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',14))


email_input=Entry(root,width=50)  
email_input.pack(ipady=4,pady=(1,15))  


apppass_label=Label(root,text='Enter Your App password',fg='white',bg='#FF0000')
apppass_label.pack(pady=(20,5))
apppass_label.config(font=('verdana',14))

apppass_input=Entry(root,width=50)
apppass_input.pack(ipady=4,pady=(1,15))


login_btn=Button(root,text='Login your Gmail account with App password',bg='white',fg='black',height=2,command=check_mail)
login_btn.pack(pady=(10,20))
login_btn.config(font=('Calibri',12))  

root.mainloop()
################################################################################################################

import gmail
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import moviepy.editor as mpe
import os

main_window=Tk()
main_window.title('Youtube Downloader')
main_window.iconbitmap('youtube.ico')
main_window.geometry('900x400')
main_window.resizable(0,0)
file=''

def threading():
    from threading import Thread
    t1=Thread(target=down_code)
    t2=Thread(target=bar)
    t1.start()
    t2.start()
def bar():
    progress.start()
    progress.update_idletasks()
    main_window.update_idletasks()
def down_code():
    try:
        status.config(text="Downloading...")
        main_window.update_idletasks()
        index=int(com.get()[0:2:1])
    except Exception as var:
        print(var)
        progress.stop()
        status.config(text="Download Failed")
        messagebox.showerror('Try again','Download Failed!!')
    else:
        try:
            import pytube
            vname = "clip.mp4"
            aname = "audio.mp3"
            main_window.update_idletasks()
            video=st[index].download()
            os.rename(video,vname)
            audio = pytube.YouTube(url).streams.filter(only_audio=True).first().download()
            os.rename(audio, aname)
            video = mpe.VideoFileClip(vname)
            audio = mpe.AudioFileClip(aname)
            final = video.set_audio(audio)
            final.write_videofile(f"{file}video.mp4")
            os.remove(vname)
            os.remove(aname)
        except Exception as var:
            print(var)
            progress.stop()
            status.config(text="Download Failed")
            messagebox.showerror('Try again','Download Failed!!')
        else:
            messagebox.showinfo('Completed','Download Completed!!')
            progress.stop()
            status.config(text="idle")
def savefile():
    global file
    file=filedialog.askdirectory()
    if file=='':
        pass
    elif file!='':
        file=file+'/'
    down_loc.config(text=file)
    print(file)
    
def streams():
    global st,sj,url
    url=url_input.get()
    print(url)
    import pytube
    try:
        status.config(text="Please wait...")
        main_window.update_idletasks()
        connection=pytube.YouTube(url)
        st=connection.streams
        print(st)
        kj=[]
        for j in range(len(st)):
            kj.append(f"{st[j]}")
        sj=[]
        x1=-1
        for i in kj:
            import re
            pattern=re.compile(r"res=[\"A-Za-z0-9\"]+ fps=[\"A-Za-z0-9\"]+",re.I)
            match_list=re.findall(pattern,i)
            x1=x1+1
            if match_list!=[]:
                sj.append(f"{x1}  ). "+match_list[0])
                
        print(sj)
        com.config(values=tuple(sj))
        com.current(2)
    except Exception as var:
        print(var)
        progress.stop()
        status.config(text="idle")
        messagebox.showerror('Internet Error','Please enter a valid URL or Check your Internet connection.')
    else:
        progress.stop()
        status.config(text="idle")
        messagebox.showinfo('Stream Selection','Select which stream you want to download')
    
    
progress=ttk.Progressbar(main_window,length=500,mode='indeterminate')
progress.grid(row=0,column=20,pady=(15,50))

#url and folder location to be display
btn=Button(main_window,text='Start Download',command=threading)
btn.grid(row=1,column=20,pady=(70,50),ipady=5)
btn.config(font=('verdana',10,'bold'))

note=Label(main_window,text='Note: If download loc. not provided, the file will be downloaded in CWD')
note.grid(row=1,column=20,pady=(100,5),ipady=5)

status=Label(main_window,text='idle')
status.grid(row=0,column=21,pady=(15,50))
status.config(font=('verdana',10,'bold'))


url_label=Label(main_window,text="   Enter YT video URL:")
url_label.grid(row=1,column=19,pady=(0,400))
url_label.config(font=('verdana',12))

url_input=Entry(main_window,text='',width=80)  
url_input.grid(row=1,column=20,ipady=4,pady=(0,400))

url_label=Label(main_window,text="   Set Download location:")
url_label.grid(row=1,column=19,pady=(0,300))
url_label.config(font=('verdana',12))

stream_label=Label(main_window,text="   Select Stream to download:")
stream_label.grid(row=1,column=19,pady=(100,300))
stream_label.config(font=('verdana',12))

down_loc=Label(main_window,text='',width=68,bg='white')  
down_loc.grid(row=1,column=20,ipady=4,pady=(0,300))
down_loc.config(anchor='w')

browse_btn=Button(main_window, text="Browse Folder", font =("verdana", 10),command=savefile)
browse_btn.grid(row=1,column=21,ipady=0,pady=(0,300))


com=ttk.Combobox(main_window,width=78,state='readonly')
com.grid(row=1,column=20,ipady=4,pady=(100,300))



stream_btn=Button(main_window, text="Get Streams", font =("verdana", 10),command=streams)
stream_btn.grid(row=1,column=21,ipady=0,pady=(100,300))

if pass1==0:
    main_window.destroy()
main_window.mainloop()





