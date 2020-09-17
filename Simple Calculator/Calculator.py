import tkinter as tk

root=tk.Tk()
root.geometry("500x540")
root.configure(bg='gray75')
root.title("Calculator")
#slate gray1

def write(x):
    if x=='':
        txt.delete("1.0",tk.END)  
    else:
        if "=" in txt.get("1.0", "end-1c"):
            txt.delete("1.0",tk.END)       
        txt.insert(tk.END,x)
   
def delete():
    if "="  not in txt.get("1.0", "end-1c"):
        txt.delete("end-2c",tk.END)
       
    
def res():
    try:
        ans=eval(txt.get("1.0", "end-1c"))
        #txt.delete("1.0",tk.END)
        txt.insert(tk.END,' = '+str(ans))
    except:
        txt.delete("1.0",tk.END)
        txt.insert(tk.END,"Error")
    

txt=tk.Text(root,height=2,width=29,font=("Helvetica",20,'bold'),borderwidth=10,bg="slate gray1")
txt.place(x=20,y=30)
#fg='tomato'
fg="gold4"
fg_sign='khaki'
b_bg='khaki3'

x=14
y=180

tk.Button(root,text='1',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg,bg=b_bg,command=lambda:write(1)).place(x=x,y=y)
tk.Button(root,text='2',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg,bg=b_bg,command=lambda:write(2)).place(x=x+120,y=y)
tk.Button(root,text='3',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg,bg=b_bg,command=lambda:write(3)).place(x=x+240,y=y)
tk.Button(root,text='+',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg_sign,bg=b_bg,command=lambda:write('+')).place(x=x+360,y=y)
tk.Button(root,text='4',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg,bg=b_bg,command=lambda:write(4)).place(x=x,y=y+70)
tk.Button(root,text='5',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg,bg=b_bg,command=lambda:write(5)).place(x=x+120,y=y+70)
tk.Button(root,text='6',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg,bg=b_bg,command=lambda:write(6)).place(x=x+240,y=y+70)
tk.Button(root,text='-',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg_sign,bg=b_bg,command=lambda:write('-')).place(x=x+360,y=y+70)
tk.Button(root,text='7',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg,bg=b_bg,command=lambda:write(7)).place(x=x,y=y+140)
tk.Button(root,text='8',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg,bg=b_bg,command=lambda:write(8)).place(x=x+120,y=y+140)
tk.Button(root,text='9',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg,bg=b_bg,command=lambda:write(9)).place(x=x+240,y=y+140)
tk.Button(root,text='x',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg_sign,bg=b_bg,command=lambda:write('*')).place(x=x+360,y=y+140)
tk.Button(root,text='0',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg,bg=b_bg,command=lambda:write(0)).place(x=x+120,y=y+210)
tk.Button(root,text='clear',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground='black',activeforeground='white',bg=b_bg,command=lambda:write("")).place(x=x+120,y=y+280)
tk.Button(root,text='=',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground='medium sea green',bg=b_bg,command=res).place(x=x+360,y=y+280)
tk.Button(root,text='/',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg_sign,bg=b_bg,command=lambda:write('/')).place(x=x+360,y=y+210)
tk.Button(root,text='(',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg,command=lambda:write('('),bg=b_bg).place(x=x,y=y+280)
tk.Button(root,text='.',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg,bg=b_bg,command=lambda:write('.')).place(x=x+240,y=y+210)
tk.Button(root,text=')',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg,bg=b_bg,command=lambda:write(')')).place(x=x+240,y=y+280)
tk.Button(root,text='mod',width=9,height=2,font=("Helvetica",13,'bold'),borderwidth=8,activebackground=fg_sign,bg=b_bg,command=lambda:write('%')).place(x=x,y=y+210)
tk.Button(root,text='back',width=7,height=1,font=("Helvetica",10,'bold'),borderwidth=8,activebackground='tomato',bg=b_bg,command=delete).place(x=x,y=130)
tk.mainloop()

