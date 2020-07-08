from tkinter import messagebox, filedialog, colorchooser

messagebox.showinfo(title= 'A friendly message', message='Hello, Tkinter!')

answer = messagebox.askyesno(title='Hungry?', message='Do you want SPAM?')
print(answer)

filename = filedialog.askopenfile() 
print(filename.name)

colorchooser.askcolor(initialcolor='#FFFFFF') # returns RGB and HEX representation