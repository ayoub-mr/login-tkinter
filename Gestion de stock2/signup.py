from tkinter import *
from PIL import ImageTk 
def login_page():
    singnup_window.destroy()
    import login
singnup_window=Tk()
singnup_window.title('Signup Page')
singnup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='bg.jpg')
bglabel=Label(singnup_window,image=background)
bglabel.grid()
heading=Label(singnup_window,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',23,'bold'),bg='#C7B7D2',fg='#6F448E')
heading.place(x=550,y=50)
emaillabel=Label(singnup_window,text='Email',font=('Microsoft Yahei UI Light',15,'bold'),bd=0,fg='#6F448E',bg='#C3C3C3')
emaillabel.place(x=550,y=160)
emailentry=Entry(singnup_window,width=25,font=('Microsoft Yahei UI Light',15,'bold'),bd=0,fg='#6F448E',bg='#C3C3C3')
emailentry.place(x=550,y=190)
Usernamelabel=Label(singnup_window,text='Username',font=('Microsoft Yahei UI Light',15,'bold'),bd=0,fg='#6F448E',bg='#C3C3C3')
Usernamelabel.place(x=550,y=230)
Usernameentry=Entry(singnup_window,width=25,font=('Microsoft Yahei UI Light',15,'bold'),bd=0,fg='#6F448E',bg='#C3C3C3')
Usernameentry.place(x=550,y=260)
Passwordlabel=Label(singnup_window,text='Password',font=('Microsoft Yahei UI Light',15,'bold'),bd=0,fg='#6F448E',bg='#C3C3C3')
Passwordlabel.place(x=550,y=300)
Passwordentry=Entry(singnup_window,width=25,font=('Microsoft Yahei UI Light',15,'bold'),bd=0,fg='#6F448E',bg='#C3C3C3')
Passwordentry.place(x=550,y=330)
Cpasswordlabel=Label(singnup_window,text='Confirme Password',font=('Microsoft Yahei UI Light',15,'bold'),bd=0,fg='#6F448E',bg='#C3C3C3')
Cpasswordlabel.place(x=550,y=370)
Cpasswordentry=Entry(singnup_window,width=25,font=('Microsoft Yahei UI Light',15,'bold'),bd=0,fg='#6F448E',bg='#C3C3C3')
Cpasswordentry.place(x=550,y=400)
check=Checkbutton(singnup_window,text='I agree to the terms & conditions',font=('Microsoft Yahei UI Light',7,'bold'),bd=0,fg='#6F448E',bg='#C3C3C3',cursor='hand2')
check.place(x=650,y=440)
singupbutton=Button(singnup_window,text='Login',font=( 'Onen Sans',16,'bold') ,fg='white',bg='#864893',activebackground='#C3C2C3',cursor='hand2',bd=0,width=23)
singupbutton.place(x=550,y=480)
signupLabel=Label(singnup_window,text='Dont have an account?',font=( 'Onen Sans',7,'bold') ,fg='#6F448E',bg='#D0DAE2')
signupLabel.place(x=710,y=532) 
singupbutton=Button(singnup_window,text='Creat New One',font=( 'Onen Sans',7,'bold underline') ,fg='blue',bg='#D0DAE2',activeforeground='blue',cursor='hand2',bd=0,width=23,command=login_page)
singupbutton.place(x=710,y=550)
singnup_window.mainloop()