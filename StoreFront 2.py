# import libraries 
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random
import tkinter.messagebox
import csv
import pygame 
from tkinter import Tk, Canvas
from datetime import date, datetime

def send(): 
    virus_status = random.choice((True,False))
    if virus_status:
         OUT_BOX.configure(text = 'VIRUS STATUS : NOT FOUND', wraplength = 400, fg = 'green2')
         pixelChange1(pixelList15)
         message1 = 'Hi, Welcome to Creative Core. I\'m WATSON, a data science chatter bot. How can I help you?'
         print_general(message1, 10, 12, 200, 'system', green_col, OUTPUT_BOX)

    else:
         OUT_BOX.configure(text = 'VIRUS STATUS : FOUND', wraplength = 400, fg = 'green2', anchor = CENTER)
         pixelChange1(pixelListTalk)

         message1 = 'What is the meaning of the universe !?'
         print_general(message1, 10, 12, 200, 'system', green_col, OUTPUT_BOX)

def send_A1(): 
      lblProfilePicture.config(image = item0, bd = 7)
      message_A1 = '''Item A1: One Piece Keycap
Price: 6000 Coins
      ''' 
      print_general(message_A1, 25, 10, 180, 'system','green2', lblProfileText)
      Watson_A1 = '''That's one of the most rare and expensive items in our shop.'''
      pixelChange1(pixelListTalk)
      print_general(Watson_A1, 10, 12, 200, 'system', green_col, OUTPUT_BOX)

def send_A2(): 
      lblProfilePicture.config(image = item14_a, bd = 7)
      message_A1 = '''Item A2: D.Va Overwatch Keycap
Price: 3500 Coins
      ''' 
      print_general(message_A1, 25, 10, 180, 'system','green2', lblProfileText)
      Watson_A1 = '''You'\'re definitely not going to let any opponent get away with this type of badge.'''
      pixelChange1(pixelList15)
      print_general(Watson_A1, 10, 12, 200, 'system', green_col, OUTPUT_BOX)

def send_A3(): 
      lblProfilePicture.config(image = item13_a, bd = 7)
      message_A1 = '''Item A3: Spider-Man Keycap
Price: 3500 Coins
      ''' 
      print_general(message_A1, 25, 10, 180, 'system','green2', lblProfileText)
      Watson_A1 = '''Oh great choice! Spider Man is one of my favorite super heroes. '''
      pixelChange1(pixelList15)
      print_general(Watson_A1, 10, 12, 200, 'system', green_col, OUTPUT_BOX)

def send_A4(): 
      lblProfilePicture.config(image = item11_a, bd = 7)
      message_A1 = '''Item A4: Agents of Shield
Price: 3200 Coins
      ''' 
      print_general(message_A1, 25, 10, 180, 'system','green2', lblProfileText)
      Watson_A1 = '''Agents of Shield badge will grant you safety and security when defeating your 
greatest opponents.'''
      pixelChange1(pixelList15)
      print_general(Watson_A1, 10, 12, 200, 'system', green_col, OUTPUT_BOX)

def send_B1(): 
      lblProfilePicture.config(image = item9_a, bd = 7)
      message_A1 = '''Item B1: Dark Knight Keycap
Price: 3200 Coins
      ''' 
      print_general(message_A1, 25, 10, 180, 'system','green2', lblProfileText)
      Watson_A1 = '''This badge will give you the strength and stealth of the Dark Knight.'''
      pixelChange1(pixelList15)
      print_general(Watson_A1, 10, 12, 200, 'system', green_col, OUTPUT_BOX)

def send_B3(): 
      lblProfilePicture.config(image = item7_a, bd = 7)
      message_A1 = '''Item B3: Attack on Titan Keycap
Price: 3200 Coins
      ''' 
      print_general(message_A1, 25, 10, 180, 'system','green2', lblProfileText)
      Watson_A1 = '''This badge carries the willpower of Levi. Never give up!'''
      pixelChange1(pixelList15)
      print_general(Watson_A1, 10, 12, 200, 'system', green_col, OUTPUT_BOX)

def send_B4(): 
      lblProfilePicture.config(image = item6_a, bd = 7)
      message_A1 = '''Item B4: Pika Pika Keycap
Price: 3200 Coins
      ''' 
      print_general(message_A1, 25, 10, 180, 'system','green2', lblProfileText)
      Watson_A1 = '''Go, Pikachiu! Use Thunderbolt!!'''
      pixelChange1(pixelList15)
      print_general(Watson_A1, 10, 12, 200, 'system', green_col, OUTPUT_BOX)

def send_C1(): 
      lblProfilePicture.config(image = item2_a, bd = 7)
      message_A1 = '''Item C1: Black Kitty Paw Keycap
Price: 3200 Coins
      ''' 
      print_general(message_A1, 25, 10, 180, 'system','green2', lblProfileText)
      Watson_A1 = '''This badge will increase the chances of sun grazing by 15%.'''
      pixelChange1(pixelList15)
      print_general(Watson_A1, 10, 12, 200, 'system', green_col, OUTPUT_BOX)

def send_C2(): 
      lblProfilePicture.config(image = item10_a, bd = 7)
      message_A1 = '''Item C2: STEAM Keycap
Price: 3200 Coins
      ''' 
      print_general(message_A1, 25, 10, 180, 'system','green2', lblProfileText)
      Watson_A1 = '''The STEAM Badge...'''
      pixelChange1(pixelList15)
      print_general(Watson_A1, 10, 12, 200, 'system', green_col, OUTPUT_BOX)

def send_C3(): 
      lblProfilePicture.config(image = item4_a, bd = 7)
      message_A1 = '''Item C3: Brown Kitty Paw Keycap
Price: 3400 Coins
      ''' 
      print_general(message_A1, 25, 10, 180, 'system','green2', lblProfileText)
      Watson_A1 = '''This badge will increase the chances of random things falling from shelves by 15%.'''
      pixelChange1(pixelList15)
      print_general(Watson_A1, 10, 12, 200, 'system', green_col, OUTPUT_BOX)

def send_C4(): 
      lblProfilePicture.config(image = item5_a, bd = 7)
      message_A1 = '''Item C4: Joker's Keycap
Price: 3600 Coins
      ''' 
      print_general(message_A1, 25, 10, 180, 'system','green2', lblProfileText)
      Watson_A1 = '''When this badge is placed next to the Dark Knight badge, prepare yourself for epic battles.'''
      pixelChange1(pixelList15)
      print_general(Watson_A1, 10, 12, 200, 'system', green_col, OUTPUT_BOX)

def waithere(duration):
    var = IntVar()
    root.after(duration, var.set, 1)
    root.wait_variable(var)

def print_general(message, duration, size, wraplen, font_n, col, loc):
      string_output = ''
      for char in message: 
            string_output += char 
            loc.config(text = string_output, font = f'{font_n} {size}',
                  wraplength = wraplen, justify = LEFT, fg = col, pady = 2) 

            waithere(duration)

def pixelChange1(pixel_list):
    pixelNum = 0
    for column in range(9, canvasSize + 5, pixelSize):
        for row in range(5, canvasSize + 5, pixelSize ):
            CANV_1.create_rectangle(row, column, row + pixelSize, column  + pixelSize,
                                       fill = pixel_list[pixelNum])
            pixelNum = pixelNum + 1
            waithere(1)

def back():
      pass 

def forward(): 
      pass 


# Creating the root window and dimensions 
root = Tk() 
root.title('Creative Core Expert Systems')
root.geometry('1150x600+0+0')
root.configure(background = 'grey')

query = StringVar() 
green_col = 'green2'

pixelSize = 7
canvasSize = 7 * 16 

Picture1 = PhotoImage(file = 'Profile.gif')

item0 = PhotoImage(file = 'one2.png')
item1 = PhotoImage(file = 'AOC Keyboard (2).png')
item2 = PhotoImage(file = 'cowpaw.png')
item2_a = PhotoImage(file = 'pawpaw.png')
item3 = PhotoImage(file = 'twinkoi.png')
item4 = PhotoImage(file = 'mush_15.png')
item4_a = PhotoImage(file = 'paw1.png')
item5 = PhotoImage(file = 'whyser_15.png')
item5_a = PhotoImage(file = 'jokes.png')
item6 = PhotoImage(file = 'pika.png')
item6_a = PhotoImage(file = 'pika2.png')
item7 = PhotoImage(file = 'eye.png')
item7_a = PhotoImage(file = 'aot.png')
item8 = PhotoImage(file = 'cap.png')
item9 = PhotoImage(file = 'bat.png')
item9_a = PhotoImage(file = 'bat2.png')
item10 = PhotoImage(file = 'gengi.png')
item10_a = PhotoImage(file = 'steam.png')
item11 = PhotoImage(file = 'noface.png')
item11_a = PhotoImage(file = 'shield.png')
item12 = PhotoImage(file = 'koi.png')
item13 = PhotoImage(file = 'sider.png')
item13_a = PhotoImage(file = 'spider.png')
item14 = PhotoImage(file = 'ball.png')
item14_a = PhotoImage(file = 'ball2.png')
item15 = PhotoImage(file = 'one.png')

item_x = PhotoImage(file = 'door.png')

pixelList15 = ["#555555", "#8E8E8E", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#00FF00", "#00FF00", "#00FF00", "#000000", "#000000", "#00FF00", "#00FF00", "#00FF00", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#00FF00", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#00FF00", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#00FF00", "#00FF00", "#000000", "#000000", "#00FF00", "#00FF00", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#00FF00", "#00FF00", "#000000", "#000000", "#00FF00", "#00FF00", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#00FF00", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#00FF00", "#00FF00", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#00FF00", "#00FF00", "#00FF00", "#00FF00", "#00FF00", "#00FF00", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", ]
pixelListTalk = ["#555555", "#8E8E8E", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#00FF00", "#00FF00", "#00FF00", "#000000", "#000000", "#00FF00", "#00FF00", "#00FF00", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#00FF00", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#00FF00", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#00FF00", "#00FF00", "#000000", "#000000", "#00FF00", "#00FF00", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#00FF00", "#00FF00", "#000000", "#000000", "#00FF00", "#00FF00", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#00FF00", "#00FF00", "#00FF00", "#00FF00", "#00FF00", "#00FF00", "#00FF00", "#00FF00", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#00FF00", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#00FF00", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#00FF00", "#00FF00", "#00FF00", "#00FF00", "#00FF00", "#00FF00", "#00FF00", "#00FF00", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000", "#C7C7C7", "#555555", "#8E8E8E", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", "#C7C7C7", ]

# Start Creating your Frames (The home foundation)
# We first begin with the largest frame called the Main Frame 
################################################################
MASTER_FRAME = Frame(root, bd = 10, bg = 'grey', relief = SUNKEN, 
                  width = 1110, height = 500)
MASTER_FRAME.pack(side = TOP, padx = 8, pady = 8)
################################################################
# Then we create the second largest known as the DataFrame 
MAINFRAME_0 = Frame(MASTER_FRAME, bd = 10, bg = 'grey', relief = SUNKEN, 
                  width = 870, height = 550, padx = 4, pady = 4)
MAINFRAME_0.pack(side = RIGHT, fill = BOTH, expand = True)

# And then the smaller frames that exist inside DataFrame 
MAINFRAME_1 = Frame(MAINFRAME_0, bd = 10, bg = 'black', width = 575, 
                    height = 60, padx = 0, relief = SUNKEN)
MAINFRAME_1.pack(side = TOP, fill = BOTH, expand = True)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

HEAD_BOX = Label(MAINFRAME_1, bg = 'black', bd = 0, relief = RAISED, 
               text = 'VIRTUAL STORE-FRONT', wraplength = 800, font = 'system 18', 
               padx = 2, pady = 20, fg = 'green2', anchor = W, height = 0)
      
HEAD_BOX.pack(side = TOP)
####################################################################

MAINFRAME_2 = LabelFrame(MAINFRAME_0, bd = 7, bg = 'grey', width = 368, height = 540,
                              padx = 5, relief = SUNKEN, pady = 10, text = 'TASK-MASTER',
                              font = 'system 10 bold', fg = 'grey30')

MAINFRAME_2.pack_propagate(0)
MAINFRAME_2.pack(side = LEFT)

MAINFRAME_2_DISPLAY = Frame(MAINFRAME_2, bd = 4, bg = 'black', width = 10, height = 5,
                                   padx = 5, pady = 5, relief = RAISED)
MAINFRAME_2_DISPLAY.pack(side = TOP, fill = BOTH, expand = True)

MAINFRAME_3 = LabelFrame(MAINFRAME_0, bd = 7, bg = 'grey',
                                     width = 410, height = 540,
                                      padx = 5, relief = SUNKEN,
                                       text = 'ELECTRICITY', font = 'System 10 bold', 
                                       fg = 'grey30', pady = 5)
MAINFRAME_3.pack_propagate(0)
MAINFRAME_3.pack(side = RIGHT, expand = True, fill = BOTH)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# Placing shelves on a concrete wall 
BtnItem_1 = Button(MAINFRAME_3, bd = 2, width = 69, height = 75, image = item15,
      bg = 'grey', command = send_A1)
BtnItem_1.grid(row = 0, column = 0, sticky = W, padx = 1)

BtnItem_2 = Button(MAINFRAME_3, bd = 2, width = 69, height = 75, image = item14,
      bg = 'grey', command = send_A2)
BtnItem_2.grid(row = 0, column = 1, sticky = W, padx = 1)

BtnItem_3 = Button(MAINFRAME_3, bd = 2, width = 69, height = 75, image = item13,
      bg = 'grey', command = send_A3)
BtnItem_3.grid(row = 0, column = 2, sticky = W, padx = 1)

BtnItem_4 = Button(MAINFRAME_3, bd = 2, width = 69, height = 75, image = item11,
      bg = 'grey', command = send_A4)
BtnItem_4.grid(row = 0, column = 3, sticky = W, padx = 1)

PremiumShelf = Canvas(MAINFRAME_3, bd = 6, width = 300, height = 0, 
      relief = RAISED, bg = 'grey', highlightbackground = 'grey') 
PremiumShelf.grid(row = 1, column = 0, columnspan = 4)

blank = Canvas(MAINFRAME_3, bd = 0, width = 300, height = 4, 
      relief = RAISED, bg = 'grey', highlightbackground = 'grey') 
blank.grid(row = 2, column = 0, columnspan = 4)

# Placing shelves on a concrete wall 
BtnItem_1 = Button(MAINFRAME_3, bd = 2, width = 69, height = 75, image = item9, 
      bg = 'grey', command = send_B1)
BtnItem_1.grid(row = 3, column = 0, sticky = W, padx = 1)

BtnItem_2 = Button(MAINFRAME_3, bd = 2, width = 69, height = 75, image = item8,
      bg = 'grey')
BtnItem_2.grid(row = 3, column = 1, sticky = W, padx = 1)

BtnItem_3 = Button(MAINFRAME_3, bd = 2, width = 69, height = 75, image = item7,
      bg = 'grey', command = send_B3)
BtnItem_3.grid(row = 3, column = 2, sticky = W, padx = 1)

BtnItem_4 = Button(MAINFRAME_3, bd = 2, width = 69, height = 75, image = item6,
      bg = 'grey', command = send_B4)
BtnItem_4.grid(row = 3, column = 3, sticky = W, padx = 1)

TopShelf = Canvas(MAINFRAME_3, bd = 6, width = 300, height = 0, 
      relief = RAISED, bg = 'grey', highlightbackground = 'grey') 
TopShelf.grid(row = 4, column = 0, columnspan = 4)

blank = Canvas(MAINFRAME_3, bd = 0, width = 300, height = 4, 
      relief = RAISED, bg = 'grey', highlightbackground = 'grey') 
blank.grid(row = 5, column = 0, columnspan = 4)

# Placing shelves on a concrete wall 
BtnItem_1 = Button(MAINFRAME_3, bd = 2, width = 69, height = 75, image = item2,
      bg = 'grey', command = send_C1)
BtnItem_1.grid(row = 6, column = 0, sticky = W, padx = 1)

BtnItem_2 = Button(MAINFRAME_3, bd = 2, width = 69, height = 75, image = item10,
      bg = 'grey', command = send_C2)
BtnItem_2.grid(row = 6, column = 1, sticky = W, padx = 1)

BtnItem_3 = Button(MAINFRAME_3, bd = 2, width = 69, height = 75, image = item4,
      bg = 'grey', command = send_C3)
BtnItem_3.grid(row = 6, column = 2, sticky = W, padx = 1)

BtnItem_4 = Button(MAINFRAME_3, bd = 2, width = 69, height = 75, image = item5,
      bg = 'grey', command = send_C4) 
BtnItem_4.grid(row = 6, column = 3, sticky = W, padx = 1)

MidShelf = Canvas(MAINFRAME_3, bd = 6, width = 300, height = 0, 
      relief = RAISED, bg = 'grey', highlightbackground = 'grey') 
MidShelf.grid(row = 7, column = 0, columnspan = 4)

blank = Canvas(MAINFRAME_3, bd = 0, width = 300, height = 4, 
      relief = RAISED, bg = 'grey', highlightbackground = 'grey') 
blank.grid(row = 8, column = 0, columnspan = 4)

# Placing shelves on a concrete wall 
BtnItem_1 = Button(MAINFRAME_3, bd = 4, width = 307, height = 79, bg = 'grey',
     image = item1)
BtnItem_1.grid(row = 9, column = 0, columnspan = 4)


BottomShelf = Canvas(MAINFRAME_3, bd = 6, width = 300, height = 0, 
      relief = RAISED, bg = 'grey', highlightbackground = 'grey') 
BottomShelf.grid(row = 10, column = 0, columnspan = 4)

################################################################   
# The Outermost First Frame (Social Profile Frame)
PROFILE_FRAME_0 = LabelFrame(MASTER_FRAME, bd = 7, bg = 'grey', width = 30, height = 280
                               , relief = SUNKEN, text = 'CREATIVE CORE',  
                               font = 'System 10 bold', fg = 'grey30') 
PROFILE_FRAME_0.pack_propagate(0)
PROFILE_FRAME_0.pack(side = TOP, fill = BOTH)

PROFILE_FRAME_1 = Frame(PROFILE_FRAME_0, bd = 7, bg = 'black', width = 10, height = 215
                               , relief = SUNKEN, padx = 5)
PROFILE_FRAME_1.pack_propagate(0)
PROFILE_FRAME_1.pack(side = TOP, fill = BOTH)

# PROFILE_FRAME_2 = Frame(PROFILE_FRAME_1, bd = 2, bg = 'white', 
#                                relief = FLAT)
# PROFILE_FRAME_2.pack_propagate(0)
# PROFILE_FRAME_2.pack(side = LEFT, padx = 2, pady = 8)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# 

lblProfilePicture = Label(PROFILE_FRAME_1, image = item_x,
                        width = 148, height = 180, relief = RAISED,
                        bd = 7, padx = 10, bg = 'black')
lblProfilePicture.pack_propagate(0)
lblProfilePicture.pack(side = LEFT)

lblProfileText = Label(PROFILE_FRAME_1, padx = 5, pady = 5, font = 'System 12 bold',
                        text = '', fg = 'green2', bg = 'black')
lblProfileText.pack_propagate(0)
lblProfileText.pack(side = LEFT, anchor = W)

        # Add Back Button
btn_back = Button(PROFILE_FRAME_0, text = '<<', command = back, bg = 'black', padx = 15, height = 10,
    fg = 'green2', width = 10, bd = 5)
btn_back.pack(side = LEFT, anchor = W, padx = 3)

cent_back = Button(PROFILE_FRAME_0, text = '||', command = back, bg = 'black', padx = 15, height = 10,
    fg = 'green2', width = 11, bd = 5)
cent_back.pack(side = LEFT, anchor = CENTER, padx = 3)

        # Add Forward Button
btn_for = Button(PROFILE_FRAME_0, text = '>>', command = lambda : forward(1), fg = 'green2', height = 10, 
    bg = 'black', width = 18, bd = 5)
btn_for.pack(side = LEFT, anchor = E, padx = 3)

################################################################
MID_FRAME = Frame(MASTER_FRAME, bd = 7, width = 400, height = 50, padx = 4, 
                        pady = 0, relief = RAISED, bg = 'black')

MID_FRAME.pack_propagate(0)
MID_FRAME.pack(side = TOP, expand = True, fill = BOTH)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

OUT_BOX = Label(MID_FRAME, bg = 'black', bd = 0, relief = RAISED, text = 'VIRUS STATUS : NOT FOUND',
              wraplength = 400, font = 'system 12 ', padx = 2, pady = 20, fg = 'green2', anchor = CENTER,
              width = 100)
OUT_BOX.pack(side = TOP)

#################################################################

CHATBOT_FRAME = LabelFrame(MASTER_FRAME, bd = 7, bg = 'grey', width = 400, height = 375,
                          padx = 4, pady = 0, relief = SUNKEN, text = 'WATSON',
                               font = 'System 10 bold', fg = 'gray30')
CHATBOT_FRAME.pack(side = TOP, fill = BOTH, expand = True)

CHATBOT_FRAME_ONE = Frame(CHATBOT_FRAME, bd = 7, bg = 'black', width = 400, height = 150,
                              padx = 2, pady = 2, relief = SUNKEN)

CHATBOT_FRAME_ONE.pack_propagate(0)

CHATBOT_FRAME_ONE.pack(side = TOP)

CHATBOT_FRAME_TWO = Frame(CHATBOT_FRAME, bd = 7, bg = 'grey', width = 400, height = 50,
                              padx = 2, pady = 2, relief = SUNKEN)

CHATBOT_FRAME_TWO.pack_propagate(0)
CHATBOT_FRAME_TWO.pack(side = TOP)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

CANV_1 = Canvas(CHATBOT_FRAME_ONE, width = 120,  height = 130,
                           bd = 0, bg = 'black', 
                           highlightbackground = 'black')
CANV_1.pack(side = LEFT, anchor = NW)

OUTPUT_BOX = Label(CHATBOT_FRAME_ONE,
              text = '', bg = 'black', bd = 0, relief = RAISED,
              wraplength = 400, font = 'courier 6 bold', padx = 15, pady = 2)
      
OUTPUT_BOX.pack(side = LEFT)

BTN_SEND = Button(CHATBOT_FRAME_TWO, width = 5, height = 1, bd = 4,
                              font = 'system 12 bold', text = 'SEND', 
                              bg = 'black', command = send, fg = 'green2')
      
BTN_SEND.pack(side = RIGHT, anchor = E,expand = True)

INPUT_BOX = Entry(CHATBOT_FRAME_TWO, font = 'System 12 bold',
              text = '', bg = 'black', fg = 'green2', 
               width = 34, bd = 4, relief = SUNKEN, textvariable = query)
      
INPUT_BOX.pack(side = LEFT, expand = True)

#################################################################
# Then run the mainloop 
root.mainloop()
