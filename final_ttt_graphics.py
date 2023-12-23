import tkinter as tk
import tkinter.messagebox as msg
class Game:
    def __init__(self):
        self.grid=[[" "," "," "],[" "," "," "],[" "," "," "]]
        self.over=False
        self.winner=None
        self.turn=1
        self.score={"X":-1,"O":1,"tie":0}
    def minmax(self,turn):
        self.win()
        if self.over:
            return self.score[self.winner]
        if turn==1:
            best=-1*1e9
            for i in range(3):
                for j in range(3):
                    if self.grid[i][j]!=" ": continue
                    self.grid[i][j]="O"
                    curr=self.minmax(0)
                    self.grid[i][j]=" "
                    best=max(curr,best)
            self.over=False
            self.winner=None
            return best
        else:
            best=1e9
            for i in range(3):
                for j in range(3):
                    if self.grid[i][j]!=" ": continue
                    self.grid[i][j]="X"
                    curr=self.minmax(1)
                    self.grid[i][j]=" "
                    best=min(curr,best)
            self.over=False
            self.winner=None
            return best
    def check_over(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j]==" ": return False
        return True
    def win(self):
        ans=True
        if (["O","O","O"] in self.grid):
            self.winner="O"
            self.over=True
        elif (self.grid[0][0]=="O" and self.grid[1][0]=="O" and self.grid[2][0]=="O"):
            self.winner="O"
            self.over=True
        elif (self.grid[0][1]=="O" and self.grid[1][1]=="O" and self.grid[2][1]=="O"):
            self.winner="O"
            self.over=True
        elif (self.grid[0][2]=="O" and self.grid[1][2]=="O" and self.grid[2][2]=="O"):
            self.winner="O"
            self.over=True
        elif (self.grid[0][0]=="O" and self.grid[1][1]=="O" and self.grid[2][2]=="O"):
            self.winner="O"
            self.over=True
        elif (self.grid[0][2]=="O" and self.grid[1][1]=="O" and self.grid[2][0]=="O"):
            self.winner="O"
            self.over=True
        elif (["X","X","X"] in self.grid):
            self.winner="X"
            self.over=True
        elif (self.grid[0][0]=="X" and self.grid[1][0]=="X" and self.grid[2][0]=="X"):
            self.winner="X"
            self.over=True
        elif (self.grid[0][1]=="X" and self.grid[1][1]=="X" and self.grid[2][1]=="X"):
            self.winner="X"
            self.over=True
        elif (self.grid[0][2]=="X" and self.grid[1][2]=="X" and self.grid[2][2]=="X"):
            self.winner="X"
            self.over=True
        elif (self.grid[0][0]=="X" and self.grid[1][1]=="X" and self.grid[2][2]=="X"):
            self.winner="X"
            self.over=True
        elif (self.grid[0][2]=="X" and self.grid[1][1]=="X" and self.grid[2][0]=="X"):
            self.winner="X"
            self.over=True
        elif self.check_over():
            self.winner="tie"
            self.over=True
        else:
            self.over=False
            ans=False
        return ans
    def show_grid(self):
        for i in range(3):
            for j in range(3):
                print(self.grid[i][j],end="")
                if j!=2: print("|",end="")
            print()
        print()
class Gui:
    def __init__(self,game):
        self.root=tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.configure(background="#75C2F6")
        self.grid=game.grid
    def paint(self):
        for i in range(3):
            for j in range(3):
                label=tk.Label(self.root,text=self.grid[i][j],bg="#1D5D9B",fg="#75C2F6",font=('Verdana', 30, 'bold'),justify=tk.CENTER,width=8,height=4)
                label.grid(row=i,column=j,padx=5,pady=5)
class Flow:
    def __init__(self,gui,game):
        self.gui=gui
        self.game=game
        self.grid=self.game.grid
        self.start=None
    def play(self):
        self.gui.paint()
        mess="1 2 3\n4 5 6\n7 8 9\nTyping numbers from 1 to 9 will place X on the following positions.\nAll the best!!"
        msg.showinfo(title="Welcome to the game of tic-tac-toe", message=mess)
        self.start=msg.askyesno(message="Do you want to start the game?")
        if not self.start: self.AI_start()
        self.gui.root.bind('<Key>',self.move)
        self.gui.root.mainloop()
    def AI_start(self):
        best=-1*1e9
        row,col=0,0
        for i in range(3):
            for j in range(3):
                if self.grid[i][j]!=" ": continue
                self.grid[i][j]="O"
                curr=self.game.minmax(0)
                self.grid[i][j]=" "
                if curr>best:
                    best=curr
                    row,col=i,j
        self.grid[row][col]="O"
        self.gui.paint()
        self.game.win()
        if self.game.over: 
            winner=self.game.winner
            if winner=="tie": msg.showinfo(title="Game Over",message="The game is a tie !!")
            elif winner=="X": msg.showinfo(title="Game Over",message=f"Congratulation,You win the Game!!")
            else: msg.showinfo(title="Game Over",message="Hard luck, You lose!!")
            self.gui.root.destroy()
    def move(self,event):
        pos=int(event.char)-1
        row,col=pos//3,pos%3
        if self.grid[row][col]!=" ":
            msg.showerror(title="Error",message="This position is already filled, please choose another position.")
            return
        self.grid[row][col]="X"
        self.gui.paint()
        self.game.win()
        if self.game.over: 
            winner=self.game.winner
            if winner=="tie": msg.showinfo(title="Game Over",message="The game is a tie !!")
            elif winner=="X": msg.showinfo(title="Game Over",message=f"Congratulation,You win the Game!!")
            else: msg.showinfo(title="Game Over",message="Hard luck, You lose!!")
            self.gui.root.destroy()
        best=-1*1e9
        row,col=0,0
        for i in range(3):
            for j in range(3):
                if self.grid[i][j]!=" ": continue
                self.grid[i][j]="O"
                curr=self.game.minmax(0)
                self.grid[i][j]=" "
                if curr>=best:
                    best=curr
                    row,col=i,j
        self.grid[row][col]="O"
        self.gui.paint()
        self.game.win()
        if self.game.over: 
            winner=self.game.winner
            if winner=="tie": msg.showinfo(title="Game Over",message="The game is a tie !!")
            elif winner=="X": msg.showinfo(title="Game Over",message=f"Congratulation,You win the Game!!")
            else: msg.showinfo(title="Game Over",message="Hard luck, You lose!!")
            self.gui.root.destroy()
game=Game()
gui=Gui(game)
flow=Flow(gui,game)
flow.play()


        