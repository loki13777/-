import tkinter
import random
import time




class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.state = [None] * 9
        self.bind('<Button-1>', self.click)

    def get_winner(self):
        variants = []
        for i, j in enumerate(range(0, 9, 3)):
            variants.append(self.state[j:j + 3])
            variants.append(self.state[i::3])
            variants.append(self.state[::4])
            variants.append(self.state[2:7:2])
        print('get_winner')
        if ['x', ] * 3 in variants:
            return 'КРЕСТИКИ ПОБЕДИЛИ'
        elif ['o', ] * 3 in variants:
            return 'НОЛИКИ ПОБИДИЛИ'
        elif None not in self.state:
            return 'НИЧЬЯ'
        else:
            return None

    def bot_move(self):
        a = []
        i = 0
        for el in self.state:
            if el == None:
                a.append(i)
            i = i + 1
        if a != []:
            b = random.choice(a)
            self.state[b] = 'o'
            if b >= 0 and b <= 2:
                colum = b
                row = 0
            elif b >= 3 and b <= 5:
                colum = b - 3
                row = 1
            elif b >= 6 and b <= 8:
                colum = b - 6
                row = 2
        print('bot_move')
        self.add_o(colum, row)


    def click(self, event):
        x = event.x
        y = event.y
        if y > 0 and y < 100:
            if x > 0 and x <= 100:
                i = 0
                b, c = 0, 0
            elif x > 100 and x <= 200:
                i = 1
                b, c = 1, 0
            elif x > 200 and x <= 300:
                i = 2
                b, c = 2, 0
        elif y >= 100 and y < 200:
            if x > 0 and x <= 100:
                i = 3
                b, c = 0, 1
            elif x > 100 and x <= 200:
                i = 4
                b, c = 1, 1
            elif x > 200 and x <= 300:
                i = 5
                b, c = 2, 1
        elif y >= 200 and y < 300:
            if x > 0 and x <= 100:
                i = 6
                b, c = 0, 2
            elif x > 100 and x <= 200:
                i = 7
                b, c = 1, 2
            elif x > 200 and x <= 300:
                i = 8
                b, c = 2, 2
        if self.state[i] == None:
            self.state[i] = 'x'
            self.add_x(b, c)

            self.get_winner()
            if self.get_winner() == None:
                self.bot_move()
                self.get_winner()
                if self.get_winner() != None:
                    self.create_text(150, 150, font="Times 10 italic bold", text=self.get_winner())
                    time.sleep(2)
                    self.end_game()
                    self.restart_game()
                pass
            else:
                self.create_text(150, 150, font="Times 10 italic bold", text=self.get_winner())
                time.sleep(2)
                self.end_game()
                self.restart_game()
        else:
            print('aaaa')

    def end_game(self):
        self.state = [1] * 9
        time.sleep(0)
        print('end_game')

    def restart_game(self):
        self.delete("all")
        self.create_text(150, 150, font="Times 10 italic bold", text='Новая игра')

        self.delete("text")
        self.state = [None] * 9
        self.draw_lines()
        print('restart_game')

    def add_x(self, column, row):
        if column == 0:
            x1 = 30
            x2 = 70
        if row == 0:
            y1 = 30
            y2 = 70
        if column == 1:
            x1 = 130
            x2 = 170
        if row == 1:
            y1 = 130
            y2 = 170
        if column == 2:
            x1 = 230
            x2 = 270
        if row == 2:
            y1 = 230
            y2 = 270
        self.create_line(x1, y1, x2, y2, width=5, fill='blue')
        self.create_line(x1 + 40, y1, x2 - 40, y2, width=5, fill='blue')
        print('add_x')

    def add_o(self, column, row):
        if column == 0:
            x1 = 30
            x2 = 70
        if row == 0:
            y1 = 30
            y2 = 70
        if column == 1:
            x1 = 130
            x2 = 170
        if row == 1:
            y1 = 130
            y2 = 170
        if column == 2:
            x1 = 230
            x2 = 270
        if row == 2:
            y1 = 230
            y2 = 270
        self.create_oval(x1, y1, x2, y2, width=5, outline='red')
        print('add_0')

    def draw_lines(self):
        self.create_line(100, 0, 100, 300, fill='grey')
        self.create_line(200, 0, 200, 300, fill='grey')
        self.create_line(0, 100, 300, 100, fill='grey')
        self.create_line(0, 200, 300, 200, fill='grey')


window = tkinter.Tk()
game = TicTacToe(window)
game.pack()
game.draw_lines()
window.mainloop()
