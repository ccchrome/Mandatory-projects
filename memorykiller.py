import tkinter as tk
from tkinter import messagebox as mb

string = 'x'
root = tk.Tk()
root.withdraw()

try:
      while True:
            string = string + string
            if mb.askyesno(message='Stop already at this size ' + str(len(string)/1024/1024) + ' MB ?'):
                  raise MemoryError

except MemoryError:
      mb.showerror(message = "Stopped at "+ str(len(string)/1024/1024) + ' MB' )
      root.destroy()

