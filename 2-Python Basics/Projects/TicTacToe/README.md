# Building a Tic-Tac-Toe Game using Tkinter

## Docs

- [https://tkdocs.com/](https://tkdocs.com/)

## Installation

```bash
sudo apt-get install python3-tk
```

## Steps

1. Set up the Tic-Tac-Toe Game Board

    1. Create a file called `tic_tac_toe.py`
    2. Create a class to represent the Game Board

        ```python
        import tkinter as tk 
        from tkinter import font


        class Board(tk.Tk):
            
            def __init__(self):
                super().__init__()
                # Title of the window
                self.title("P24-E07 Tic-Tac-Toe")
                # Cells to display boxes on the board
                self._cells = {}
        ```

        - Create methods to display and outline the game board

            ```python
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
            ```

        - Create a method the creates the grid of cells for the board

            ```python
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
                            fg="black",
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
            ```

2. Set up the game logic:
    - Define classes for players and their moves
    - Create a class to represent the Game Logic
    - Outline the winning combinations

3. Process the players' moves on the games logic:
    - Validate a players moves
    - Process player moves to find a winner
    - Check for tied games
    - Toggle between player turns

4. Process the players moves on the Game Board:
    - Handle a players move event
    - Update the Game Board to reflect the moves

5. Provide options to play again and exit the game
    - Build the games main menu
    - Implement the play again option