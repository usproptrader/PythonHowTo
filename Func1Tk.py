# how to redirect stdout to a windows
# widget or frame
# we declare the stdout redirector
# then run Func1 in a thread
# we can now import standard functions
# available in python
# Tkinter to generate a widget
# sys to get the standard redirector
# os for windows specific functions
# time for the sleep functions
# threading to create the thread
# for our function to run.
# and finally import our Func1
# into this code

import tkinter as Tk
import sys
import os

import threading
from  Func1 import *

root = Tk.Tk()
root.title("Strings Function")
text = Tk.Text(root,width=60,height=50)
text.pack()
exit_thread= False
exit_success = False

class Std_redirector(object):
    def __init__(self,widget):
        self.widget = widget
    def write(self,string):
        if not exit_thread:
            self.widget.insert(Tk.END,string)
            self.widget.see(Tk.END)
sys.stdout = Std_redirector(text)
thread1 = threading.Thread(target=Func1)
thread1.start()
root.mainloop()


os._exit(0)
