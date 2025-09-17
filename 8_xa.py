import tkinter as tk
import random
from PIL import Image, ImageTk
from collections import deque

class eight_xa:
    def __init__(self, root):
        self.root = root
        self.root.title("8 xa")
        self.root.config(bg="lightgray")
        self.n = 8

        self.frame_left = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        self.frame_left.grid(row=0, column=0, padx=10, pady=10)

        self.frame_right = tk.Frame(self.root, bg="lightgray", relief="solid", borderwidth=1)
        self.frame_right.grid(row=0, column=1, padx=10, pady=10)
        
        white_xa = Image.open("./whiteX.png").resize((60, 60))
        black_xa = Image.open("./blackX.png").resize((60, 60))
        self.whiteX = ImageTk.PhotoImage(white_xa)
        self.blackX = ImageTk.PhotoImage(black_xa)
        
        self.img_null = tk.PhotoImage(width=1, height=1)

        self.xa_pos = [[0] * self.n for _ in range(self.n)]
        self.set_xa(self.xa_pos)
        
        self.buttons_left = self.create_widget(self.frame_left, False)
        self.buttons_right = self.create_widget(self.frame_right, True)

    def create_widget(self, frame, draw_xa):
        buttons = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                color = "white" if (i + j) % 2 == 0 else "black"
                
                if draw_xa and self.xa_pos[i][j] == 1:
                    img = self.whiteX if color == "black" else self.blackX
                else:
                    img = self.img_null
                
                btn = tk.Button(frame, image=img, width=60, height=60, bg=color,
                                relief="flat", borderwidth=0, highlightthickness=0)
                    
                btn.grid(row = i, column = j, padx=1, pady=1)
                row.append(btn)
            buttons.append(row)
        
        return buttons
    
    def x_is_safe(self, row, col):
        if row < 0 or row >= self.n or col < 0 or col >= self.n:
            return False
        
        for i in range(self.n):
            if self.xa_pos[row][i] == 1:
                return False
            if self.xa_pos[i][col] == 1:
                return False
        return True
    
    def set_xa(self, xa_pos):
        x_start = random.randint(0, self.n - 1)
        y_start = random.randint(0, self.n - 1)
        xa_pos[x_start][y_start] = 1
        
        q = deque([(x_start, y_start)])
        near = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
        setted = 1
        
        while q and setted < 8:
            x, y = q.popleft()
            for move in near:
                x_next, y_next = x + move[0], y + move[1]
                q.append((x_next, y_next))
                if self.x_is_safe(x_next, y_next):
                    xa_pos[x_next][y_next] = 1
                    setted += 1
                    if setted == 8:
                        break
    
if __name__ == "__main__":
    root = tk.Tk()
    game = eight_queen(root)
    root.mainloop()
