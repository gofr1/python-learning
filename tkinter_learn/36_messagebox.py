from tkinter import messagebox, filedialog, colorchooser

messagebox.showinfo(title= 'A friendly message', message='Hello, Tkinter!')

answer = messagebox.askyesno(title='Hungry?', message='Do you want SPAM?')
print(answer)

filename = filedialog.askopenfile() 
print(filename.name)

colorchooser.askcolor(initialcolor='#FFFFFF') # returns RGB and HEX representation

# Other types of message boxes
messagebox.showwarning(title='showwarning', message='Warning')
messagebox.showerror(title='showerror', message='Error')
messagebox.askquestion(title='askquestion', message='Are you sure?')
messagebox.askokcancel(title='askokcancel', message='Want to continue?')
messagebox.askretrycancel(title='askretrycancel', message='Try again?')   