"""
Main file for chess game run with tkinter

Naming convention for pieces:

'w' as first letter = white
'b' as first letter = black

'p' as second letter = pawn
'n' as second letter = knight
'b' as second letter = bishop
'r' as second letter = rook
'q' as second letter = queen
'k' as second letter = king
"""

from tkinter import *
from tkinter import ttk

"""
Check if the entered move is valid and if so updates the game

move is valid if it is a string in standard chess notation that
corresponds to a legal move for the current chess board
"""
def process_move(move):
	pass

#Set up window and frame for game to take place
window = Tk()
window.title('Chess')
window.state('zoomed')
mainframe = ttk.Frame(window, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

#Load in image files for the chess pieces
blank_img = PhotoImage(file = 'images\\blank.png')
wp_img = PhotoImage(file = 'images\wpawn.png')
wn_img = PhotoImage(file = 'images\wknight.png')
wb_img = PhotoImage(file = 'images\wbishop.png')
wr_img = PhotoImage(file = 'images\wrook.png')
wq_img = PhotoImage(file = 'images\wqueen.png')
wk_img = PhotoImage(file = 'images\wking.png')
bp_img = PhotoImage(file = 'images\\bpawn.png')
bn_img = PhotoImage(file = 'images\\bknight.png')
bb_img = PhotoImage(file = 'images\\bbishop.png')
br_img = PhotoImage(file = 'images\\brook.png')
bq_img = PhotoImage(file = 'images\\bqueen.png')
bk_img = PhotoImage(file = 'images\\bking.png')

#Create board labels
board_0_0 = ttk.Label(mainframe, image=br_img, background='black').grid(column=1, row=0)
board_0_1 = ttk.Label(mainframe, image=bp_img, background='black').grid(column=1, row=1)
board_0_2 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=1, row=2)
board_0_3 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=1, row=3)
board_0_4 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=1, row=4)
board_0_5 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=1, row=5)
board_0_6 = ttk.Label(mainframe, image=wp_img, background='black').grid(column=1, row=6)
board_0_7 = ttk.Label(mainframe, image=wr_img, background='black').grid(column=1, row=7)
board_1_0 = ttk.Label(mainframe, image=bn_img, background='black').grid(column=2, row=0)
board_1_1 = ttk.Label(mainframe, image=bp_img, background='black').grid(column=2, row=1)
board_1_2 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=2, row=2)
board_1_3 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=2, row=3)
board_1_4 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=2, row=4)
board_1_5 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=2, row=5)
board_1_6 = ttk.Label(mainframe, image=wp_img, background='black').grid(column=2, row=6)
board_1_7 = ttk.Label(mainframe, image=wn_img, background='black').grid(column=2, row=7)
board_2_0 = ttk.Label(mainframe, image=bb_img, background='black').grid(column=3, row=0)
board_2_1 = ttk.Label(mainframe, image=bp_img, background='black').grid(column=3, row=1)
board_2_2 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=3, row=2)
board_2_3 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=3, row=3)
board_2_4 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=3, row=4)
board_2_5 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=3, row=5)
board_2_6 = ttk.Label(mainframe, image=wp_img, background='black').grid(column=3, row=6)
board_2_7 = ttk.Label(mainframe, image=wb_img, background='black').grid(column=3, row=7)
board_3_0 = ttk.Label(mainframe, image=bq_img, background='black').grid(column=4, row=0)
board_3_1 = ttk.Label(mainframe, image=bp_img, background='black').grid(column=4, row=1)
board_3_2 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=4, row=2)
board_3_3 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=4, row=3)
board_3_4 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=4, row=4)
board_3_5 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=4, row=5)
board_3_6 = ttk.Label(mainframe, image=wp_img, background='black').grid(column=4, row=6)
board_3_7 = ttk.Label(mainframe, image=wq_img, background='black').grid(column=4, row=7)
board_4_0 = ttk.Label(mainframe, image=bk_img, background='black').grid(column=5, row=0)
board_4_1 = ttk.Label(mainframe, image=bp_img, background='black').grid(column=5, row=1)
board_4_2 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=5, row=2)
board_4_3 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=5, row=3)
board_4_4 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=5, row=4)
board_4_5 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=5, row=5)
board_4_6 = ttk.Label(mainframe, image=wp_img, background='black').grid(column=5, row=6)
board_4_7 = ttk.Label(mainframe, image=wk_img, background='black').grid(column=5, row=7)
board_5_0 = ttk.Label(mainframe, image=bb_img, background='black').grid(column=6, row=0)
board_5_1 = ttk.Label(mainframe, image=bp_img, background='black').grid(column=6, row=1)
board_5_2 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=6, row=2)
board_5_3 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=6, row=3)
board_5_4 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=6, row=4)
board_5_5 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=6, row=5)
board_5_6 = ttk.Label(mainframe, image=wp_img, background='black').grid(column=6, row=6)
board_5_7 = ttk.Label(mainframe, image=wb_img, background='black').grid(column=6, row=7)
board_6_0 = ttk.Label(mainframe, image=bn_img, background='black').grid(column=7, row=0)
board_6_1 = ttk.Label(mainframe, image=bp_img, background='black').grid(column=7, row=1)
board_6_2 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=7, row=2)
board_6_3 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=7, row=3)
board_6_4 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=7, row=4)
board_6_5 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=7, row=5)
board_6_6 = ttk.Label(mainframe, image=wp_img, background='black').grid(column=7, row=6)
board_6_7 = ttk.Label(mainframe, image=wn_img, background='black').grid(column=7, row=7)
board_7_0 = ttk.Label(mainframe, image=br_img, background='black').grid(column=8, row=0)
board_7_1 = ttk.Label(mainframe, image=bp_img, background='black').grid(column=8, row=1)
board_7_2 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=8, row=2)
board_7_3 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=8, row=3)
board_7_4 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=8, row=4)
board_7_5 = ttk.Label(mainframe, image=blank_img, background='black').grid(column=8, row=5)
board_7_6 = ttk.Label(mainframe, image=wp_img, background='black').grid(column=8, row=6)
board_7_7 = ttk.Label(mainframe, image=wr_img, background='black').grid(column=8, row=7)

#Create board coordinate labels
ttk.Label(mainframe, text='8', padding='3 3 3 3').grid(column=0, row=0)
ttk.Label(mainframe, text='7').grid(column=0, row=1)
ttk.Label(mainframe, text='6').grid(column=0, row=2)
ttk.Label(mainframe, text='5').grid(column=0, row=3)
ttk.Label(mainframe, text='4').grid(column=0, row=4)
ttk.Label(mainframe, text='3').grid(column=0, row=5)
ttk.Label(mainframe, text='2').grid(column=0, row=6)
ttk.Label(mainframe, text='1').grid(column=0, row=7)
ttk.Label(mainframe, text='a', padding='3 3 3 3').grid(column=1, row=8)
ttk.Label(mainframe, text='b').grid(column=2, row=8)
ttk.Label(mainframe, text='c').grid(column=3, row=8)
ttk.Label(mainframe, text='d').grid(column=4, row=8)
ttk.Label(mainframe, text='e').grid(column=5, row=8)
ttk.Label(mainframe, text='f').grid(column=6, row=8)
ttk.Label(mainframe, text='g').grid(column=7, row=8)
ttk.Label(mainframe, text='h').grid(column=8, row=8)

#Create move entry box and instruction text
whose_move = StringVar()
whose_move.set('white, enter your move')
move_text = ttk.Label(mainframe, width=21, textvariable=whose_move, padding='20 20 20 20')
move_text.grid(column=9, row=0)
move = StringVar()
move_entry = ttk.Entry(mainframe, width=21, textvariable=move)
move_entry.grid(column=9, row=1)

#Initialize game board 2d array
board = [['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
         ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
		 ['', '', '', '', '', '', '', ''],
		 ['', '', '', '', '', '', '', ''],
		 ['', '', '', '', '', '', '', ''],
		 ['', '', '', '', '', '', '', ''],
		 ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
		 ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']]

#Begin running the chess game
move_entry.focus()
window.bind('<Return>', process_move)
print(board[0][1])
window.mainloop()
	

