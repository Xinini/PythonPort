from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import game_bot

import random


#GLOBAL Constants
WINDOW_X = 900
WINDOW_Y = 1000
WINDOW_START_X = 0
WINDOW_START_Y = 0
BUTTON_SIZE = int(WINDOW_X / 3)


#Object for the game/window

class tictac_win(QMainWindow):
    def __init__(self):
        super(tictac_win, self).__init__() #Give access to methods from parent

        self.player = "1"
        self.winner = False

        self.setGeometry(0,0,WINDOW_X,WINDOW_Y)
        self.setWindowTitle("Lesgo")

        self.init_win()
        #Game Board
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        
        self.label.setText("Player " + str(self.player) + "'s Turn")
    def init_win(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Player " + str(self.player) + "'s Turn")
        self.label.move(int(WINDOW_X/2),WINDOW_Y-75)
        self.label.adjustSize()
        
        self.b00 = QtWidgets.QPushButton(self)
        self.b00.setGeometry(0,0,BUTTON_SIZE,BUTTON_SIZE)
        self.b00.clicked.connect(lambda: self.update_board(0,0))

        self.b01 = QtWidgets.QPushButton(self)
        self.b01.setGeometry(BUTTON_SIZE,0,BUTTON_SIZE,BUTTON_SIZE)
        self.b01.clicked.connect(lambda: self.update_board(0,1))

        self.b02 = QtWidgets.QPushButton(self)
        self.b02.setGeometry(2*BUTTON_SIZE,0,BUTTON_SIZE,BUTTON_SIZE)
        self.b02.clicked.connect(lambda: self.update_board(0,2))

        self.b10 = QtWidgets.QPushButton(self)
        self.b10.setGeometry(0,BUTTON_SIZE,BUTTON_SIZE,BUTTON_SIZE)
        self.b10.clicked.connect(lambda: self.update_board(1,0))

        self.b11 = QtWidgets.QPushButton(self)
        self.b11.setGeometry(BUTTON_SIZE,BUTTON_SIZE,BUTTON_SIZE,BUTTON_SIZE)
        self.b11.clicked.connect(lambda: self.update_board(1,1))

        self.b12 = QtWidgets.QPushButton(self)
        self.b12.setGeometry(2*BUTTON_SIZE,BUTTON_SIZE,BUTTON_SIZE,BUTTON_SIZE)
        self.b12.clicked.connect(lambda: self.update_board(1,2))

        self.b20 = QtWidgets.QPushButton(self)
        self.b20.setGeometry(0,2*BUTTON_SIZE,BUTTON_SIZE,BUTTON_SIZE)
        self.b20.clicked.connect(lambda: self.update_board(2,0))

        self.b21 = QtWidgets.QPushButton(self)
        self.b21.setGeometry(BUTTON_SIZE,2*BUTTON_SIZE,BUTTON_SIZE,BUTTON_SIZE)
        self.b21.clicked.connect(lambda: self.update_board(2,1))

        self.b22 = QtWidgets.QPushButton(self)
        self.b22.setGeometry(2*BUTTON_SIZE,2*BUTTON_SIZE,BUTTON_SIZE,BUTTON_SIZE)
        self.b22.clicked.connect(lambda: self.update_board(2,2))

        self.reset_button = QtWidgets.QPushButton(self)
        self.reset_button.setGeometry(int(WINDOW_X/2),WINDOW_Y-50, 150,50)
        self.reset_button.setText("Reset")
        self.reset_button.clicked.connect(self.reset_board)

    def update_board(self, col, row):
        if self.winner is False:
        
            self.board[col][row] = str(self.player)

            ai_move = game_bot.bot_move(self.board, "2", False)
            #print(ai_move)
            self.board[ai_move[0]][ai_move[1]] = "2"

            self.b00.setText(self.board[0][0])
            self.b01.setText(self.board[0][1])
            self.b02.setText(self.board[0][2])
            self.b10.setText(self.board[1][0])
            self.b11.setText(self.board[1][1])
            self.b12.setText(self.board[1][2])
            self.b20.setText(self.board[2][0])
            self.b21.setText(self.board[2][1])
            self.b22.setText(self.board[2][2])

            print("--------")
            print(self.board[0])
            print(self.board[1])
            print(self.board[2])


            #if self.player == 1: #Change player
            #    self.player = 2
            #else:
            #    self.player = 1


            self.label.setText("Player " + str(self.player) + "'s Turn")

        if self.check_game_state():
            self.label.setText("Player " + str(self.check_game_state()) + " wins!!!")
            self.label.adjustSize()
            self.winner = True

    def check_game_state(self):
        for i in self.board: #Horizontal Check
            if i[0] == i[1] == i[2] and i[0] !=" ":
                return i[0]
        
        for i, r in enumerate(self.board): #Vertical Check
            column = [x[i] for x in self.board]
            if column[0] == column[1] == column[2] and column[0] !=" ":
                return column[0]
        
        diag1 = [r[i] for i, r in enumerate(self.board)] #Return diagonals
        diag2 = [r[-i-1] for i, r in enumerate(self.board)]

        if diag1[0] == diag1[1] == diag1[2] and diag1[0] != " ": #Diagonal check
            return diag1[0]
        if diag2[0] == diag2[1] == diag2[2] and diag2[0] != " ":
            return diag2[0]
        return False

    def reset_board(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        
        self.b00.setText(self.board[0][0])
        self.b01.setText(self.board[0][1])
        self.b02.setText(self.board[0][2])
        self.b10.setText(self.board[1][0])
        self.b11.setText(self.board[1][1])
        self.b12.setText(self.board[1][2])
        self.b20.setText(self.board[2][0])
        self.b21.setText(self.board[2][1])
        self.b22.setText(self.board[2][2])

        self.winner = False
        self.label.setText("Player " + str(self.player) + "'s Turn")


def main_window():
    app = QApplication(sys.argv)
    win = tictac_win()

    win.show()
    sys.exit(app.exec_())

main_window()


