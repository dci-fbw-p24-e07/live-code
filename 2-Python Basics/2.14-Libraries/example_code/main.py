from game.level import start

start.select_difficulty(15)

import turtle
import tkinter as tk
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Raw Turtle")
        self.canvas = tk.Canvas(master)
        self.canvas.config(width=600, height=200)
        self.canvas.pack(side=tk.LEFT)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("cyan")
        self.button = tk.Button(self.master, text="Press me", command=self.press)
        self.button.pack()
        self.my_lovely_turtle = turtle.RawTurtle(self.screen, shape="turtle")
        self.my_lovely_turtle.color("green")
        
    def do_stuff(self):
        for color in ["red", "yellow", "green"]:
            self.my_lovely_turtle.color(color)
            self.my_lovely_turtle.right(120)
            
    def press(self):
        self.do_stuff()
        
        
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
