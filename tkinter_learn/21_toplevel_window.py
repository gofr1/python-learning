from tkinter import Tk, Toplevel

# create a form 
root = Tk()
window = Toplevel(root)
window.title('New Window')

# to put window under main
window.lower()
window.lift(root)

# we can control windows state
window.attributes('-zoomed', True) # maximized
window.state('withdrawn') # not visible
window.state('iconic') # minimized
window.state('normal') # back to normal (before withdrawn)
window.state()

# minimize, maximize
window.iconify()
window.deiconify()

# move and resize window
# from top-left corner
window.geometry('640x480+50+100') # widthxheight+x+y

# make window resizable
window.resizable(False, False)

# set max and min size of window
window.maxsize(640,480)
window.minsize(200,200)
window.resizable(True, True)

# to destroy root window with all childs and widgets 
root.destroy()
