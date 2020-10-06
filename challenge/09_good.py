#9
import requests
from requests.auth import HTTPBasicAuth
import turtle

def list_str_to_int(lst):
    '''Turns list of strings into list of integers'''
    lst_int = []
    for el in lst:
        lst_int.append(int(el))
    return lst_int

def clear_list(lst, prt, splt):
    '''Clears data from useless symbols'''
    clr_lst = list(lst[1].split(splt)[prt].replace('\n','').replace('-->','').split(','))
    return clr_lst

def list_of_tuples(lst):
    '''Turns each 2 elemants of the list into tuple and returns list of tuples'''
    lst_tpl = []
    for i in range(0, len(lst)-1, 2):
        lst_tpl.append((lst[i],lst[i+1]))
    return lst_tpl


class TurtleCanvas():
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(500,500)
        self.screen.bgcolor('white')
        self.trtl = turtle.Turtle()
        self.trtl.pencolor('black')
        self.trtl.pensize(1)
        self.trtl.penup()

    def hide_turtle(self):
        self.trtl.ht()
    
    def exit_turtle(self):
        self.screen.exitonclick()
    
    def write_line(self, frm, t, adj:int = 0):
        x_from = adj - frm[0] if adj != 0 else frm[0]
        y_from = adj - frm[1] if adj != 0 else frm[1]
        x_to = adj - t[0] if adj != 0 else t[0]
        y_to = adj - t[1] if adj != 0 else t[1]

        self.trtl.setpos(x_from, y_from)
        self.trtl.pendown()
        self.trtl.setpos(x_to, y_to)
        self.trtl.penup()
    

url = 'http://www.pythonchallenge.com/pc/return/good.html'
page_contents = requests.get(url, auth = HTTPBasicAuth('huge', 'file')).text[:]
contents = page_contents.split('first:')

dots_one = list_of_tuples(list_str_to_int(clear_list(contents, 0, 'second:')))
dots_two = list_of_tuples(list_str_to_int(clear_list(contents, 1, 'second:')))

adj = 200 # adjustment for coordinates
trt = TurtleCanvas()

for i in range(len(dots_one)-1):
    fr = dots_one[i]
    wh = dots_one[i+1]
    trt.write_line(fr, wh, adj)

for i in range(len(dots_two)-1):
    fr = dots_two[i]
    wh = dots_two[i+1]
    trt.write_line(fr, wh, adj)

trt.hide_turtle()
trt.exit_turtle()
