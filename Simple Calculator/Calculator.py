import tkinter as tk

root=tk.Tk()
root.geometry("390x250")
root.configure(bg='slate gray1')
root.title("Calculator")
eq=''
def write(x):
    if x=='':
        txt.delete("1.0",tk.END)
    else:
        txt.insert(tk.END,x)
      
def res():
    try:
        ans=eval(txt.get("1.0", "end-1c"))
        txt.delete("1.0",tk.END)
        txt.insert(tk.END,str(ans))
    except:
        txt.delete("1.0",tk.END)
        txt.insert(tk.END,"Error")
    
txt=tk.Text(root,height=1,width=32,font=("Helvetica",15))
txt.place(x=15,y=10)
fg='tomato'
fg_sign='khaki1'
b_bg='lemon chiffon'
tk.Button(root,text='1',width=10,height=2,activebackground=fg,command=lambda:write(1),bg=b_bg).place(x=20,y=50)
tk.Button(root,text='2',width=10,height=2,activebackground=fg,bg=b_bg,command=lambda:write(2)).place(x=115,y=50)
tk.Button(root,text='3',width=10,height=2,activebackground=fg,bg=b_bg,command=lambda:write(3)).place(x=205,y=50)
tk.Button(root,text='+',width=10,height=2,activebackground=fg_sign,bg=b_bg,command=lambda:write('+')).place(x=295,y=50)
tk.Button(root,text='4',width=10,height=2,activebackground=fg,bg=b_bg,command=lambda:write(4)).place(x=20,y=100)
tk.Button(root,text='5',width=10,height=2,activebackground=fg,bg=b_bg,command=lambda:write(5)).place(x=115,y=100)
tk.Button(root,text='6',width=10,height=2,activebackground=fg,bg=b_bg,command=lambda:write(6)).place(x=205,y=100)
tk.Button(root,text='-',width=10,height=2,activebackground=fg_sign,bg=b_bg,command=lambda:write('-')).place(x=295,y=100)
tk.Button(root,text='7',width=10,height=2,activebackground=fg,bg=b_bg,command=lambda:write(7)).place(x=20,y=150)
tk.Button(root,text='8',width=10,height=2,activebackground=fg,bg=b_bg,command=lambda:write(8)).place(x=115,y=150)
tk.Button(root,text='9',width=10,height=2,activebackground=fg,bg=b_bg,command=lambda:write(9)).place(x=205,y=150)
tk.Button(root,text='*',width=10,height=2,activebackground=fg_sign,bg=b_bg,command=lambda:write('*')).place(x=295,y=150)
tk.Button(root,text='0',width=10,height=2,activebackground=fg,bg=b_bg,command=lambda:write(0)).place(x=115,y=200)
tk.Button(root,text='clear',width=10,height=2,activebackground='black',activeforeground='white',bg=b_bg,command=lambda:write("")).place(x=20,y=200)
tk.Button(root,text='=',width=10,height=2,activebackground='medium sea green',bg=b_bg,command=res).place(x=205,y=200)
tk.Button(root,text='/',width=10,height=2,activebackground=fg_sign,bg=b_bg,command=lambda:write('/')).place(x=295,y=200)
tk.mainloop()

