""" 
A simple tic-tac-toe game built using tkinter.
"""
import tkinter as tk 
from tkinter import font


class Board(tk.Tk):
    
    def __init__(self):
        super().__init__()
        # Title of the window
        self.title("P24-E07 Tic-Tac-Toe")
        # Cells to display boxes on the board
        self._cells = {}
        self._create_board_display()
        self._create_board_grids()
        
    def _create_board_display(self):
        # Attach frame to the window that is opened
        display_frame = tk.Frame(master=self)
        # aligning the frame to the x-axis
        display_frame.pack(fill=tk.X)
        # Create a label
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()
        
    def _create_board_grids(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    # fg="red",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )


def main():
    """ 
    Create the games board and run the main loop
    """
    board = Board()
    board.mainloop()
    

if __name__ == "__main__":
    main()
