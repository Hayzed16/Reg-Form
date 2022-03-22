from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('Registration Window')
        self.root.geometry('1366x768+0+0')
        self.root.config(bg='light grey')
        image_icon=PhotoImage(file='Pictures/icons8-whatsapp-480.png')
        self.root.iconphoto(False,image_icon)
        #=======bg Image
        self.bg=PhotoImage(file='Pictures/Screenshot (39).png')
        bg=Label(self.root,image=self.bg)
        bg.place(x=200, y=0, relwidth=1, relheight=1)

        #============LEFT IMAGE
        self.left=PhotoImage(file='Pictures/Screenshot (48).png')
        left=Label(self.root,image=self.left).place(x=80, y=100, width=400, height=500)


        #=====Reg frame
        frame1=Frame(self.root, bg='white')
        frame1.place(x=480, y=100, width=700, height=500 )

        #==========
        title=Label(frame1, text='REGISTER HERE', font=('Times new Roman',20,'bold'),fg='red', bg='white').place(x=40, y=20)

        #================First Row
        self.var_fname=StringVar()
        fn=Label(frame1, text='First Name', font=('Times new Roman',15,'bold'),bg='white', fg='grey').place(x=40, y=80)
        self.txt_fn=Entry(frame1, font=('Times new Roman',15,'bold'), bg='light grey')
        self.txt_fn.place(x=40, y=110, width=250)

        Last_Name=Label(frame1,text='Last Name', font=('Times new Roman',15,'bold'),bg='white', fg='grey').place(x=400, y=80)
        self.txt_Last_Name=Entry(frame1, font=('Times new Roman',15,'bold'), bg='light grey')
        self.txt_Last_Name.place(x=400, y=110, width=250)
        
        #================Second Row
        Contact=Label(frame1, text='Contact No', font=('Times new Roman',15,'bold'),bg='white', fg='grey').place(x=40, y=160)
        self.txt_Contact=Entry(frame1, font=('Times new Roman',15,'bold'), bg='light grey')
        self.txt_Contact.place(x=40, y=190, width=250)

        email=Label(frame1,text='Email', font=('Times new Roman',15,'bold'),bg='white', fg='grey').place(x=400, y=160)
        self.txt_email=Entry(frame1, font=('Times new Roman',15,'bold'), bg='light grey')
        self.txt_email.place(x=400, y=190, width=250)

        #================Third Row
        security_question=Label(frame1, text='Select Security Question', font=('Times new Roman',15,'bold'),bg='white',fg='grey').place(x=40, y=240)
        self.security_question=ttk.Combobox(frame1, font=('Times new Roman',13,'bold'), state='readonly', justify=CENTER )
        self.security_question['values']=['Select',
                                     'Your First Name',
                                     'Your Birthdate',
                                     'Your Pet Name']
        self.security_question.place(x=40, y=270, width=250)
        self.security_question.current(0)
              
        security_answer=Label(frame1, text=' Select Security Question', font=('Times new Roman',15,'bold'),bg='white',
                 fg='grey').place(x=400, y=240)
        self.txt_security_answer=Entry(frame1, font=('Times new Roman',15,'bold'), bg='light grey')
        self.txt_security_answer.place(x=400, y=270, width=250)
        
        #===============Fourth Row
        Password=Label(frame1, text='Password', font=('Times new Roman',15,'bold'),bg='white', fg='grey').place(x=40, y=320)
        self.txt_Password=Entry(frame1, font=('Times new Roman',15,'bold'), bg='light grey', show='*')
        self.txt_Password.place(x=40, y=350, width=250)

        Con_Password=Label(frame1, text='Confirm Password', font=('Times new Roman',15,'bold'),bg='white',fg='grey').place(x=400, y=320)
        self.txt_cPassword=Entry(frame1, font=('Times new Roman',15,'bold'), bg='light grey', show='*')
        self.txt_cPassword.place(x=400, y=350, width=250)

        #==========Terms and Condition
        self.var_chk=IntVar()
        chk= Checkbutton(frame1, text = 'I Agree With The Terms and Condition', variable=self.var_chk, onvalue=1, offvalue=0, bg='white', font=('Times new Roman',10))
        chk.place(x=40, y=390)

        #==========Clickable Button
        self.btn_img=PhotoImage(file='Pictures/Screenshot (45).png')
        btn_register=Button(frame1, image=self.btn_img, bd=0, cursor='hand2', command=self.register_data).place(x=40, y=430)

        self.label=PhotoImage(file='Pictures/Screenshot (49).png')
        btn=Label(frame1, image=self.label, bd=0 ).place(x=520, y=400)

        
        btn_Login=Button(self.root, text='Sign In', font=('Times new Roman',15),bd=0, cursor='hand2').place(x=185, y=500, width=180)

    def register_data(self):
        if self.txt_fn.get()=='' or self.txt_Last_Name.get()=='' or self.txt_Contact.get()=='' or self.security_question.get()=='Select' or self.txt_security_answer.get()=='' or self.txt_Password.get()=='' or self.txt_cPassword.get()=='':
            messagebox.showerror('Error', 'All fields are required', parent=self.root)
        elif self.txt_Password.get()!=self.txt_cPassword.get():
            messagebox.showerror('Error', 'Password do not match', parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror('Error', 'Please, kindly Agree our terms & condition', parent=self.root)
        
        else:
            try:
                con=pymysql.connect(host='localhost', user='root', password='', database='employee2')
                cur=con.cursor()
                cur.execute('insert into employee (f_name, l_name, contact, email, question, answer, password) values(%s,%s,%s,%s,%s,%s)'
                                (self.txt_fn.get(),
                                 self.txt_Last_Name.get(),
                                 self.txt_Contact.get(),
                                 self.txt_email.get(),
                                 self.security_question.get(),
                                 self.txt_security_answer.get(),
                                 self.txt_Password.get(),
                                 self.txt_cPassword.get()
                                 
                                ))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Registration Successful', parent=self.root)
                
            except Exception as es:                    
                messagebox.showerror('Error', f'Error due to: {str(es)}', parent=self.root)
root=Tk()
obj=Register(root)
root.mainloop()
