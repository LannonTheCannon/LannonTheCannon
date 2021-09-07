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

# Creating the root window and dimensions 
root = Tk() 
root.title('Creative Core Expert Systems')
root.geometry('1150x600+0+0')
root.configure(background = 'grey')

# Start Creating your Frames (The home foundation)
# We first begin with the largest frame called the Main Frame 
################################################################
MASTER_FRAME = Frame(root, bd = 10, bg = 'grey', relief = SUNKEN, 
                  width = 1110, height = 500)
MASTER_FRAME.pack(side = TOP, padx = 8, pady = 8)
################################################################
# Then we create the second largest known as the DataFrame 
MAINFRAME = Frame(MASTER_FRAME, bd = 10, bg = 'grey', relief = SUNKEN, 
                  width = 870, height = 550, padx = 4, pady = 4)
MAINFRAME.pack(side = RIGHT, fill = BOTH, expand = True)

# And then the smaller frames that exist inside DataFrame 
MAINFRAME_ONE = Frame(MAINFRAME, bd = 10, bg = 'black', width = 575, 
	height = 60, padx = 0, relief = SUNKEN)
MAINFRAME_ONE.pack(side = TOP, fill = BOTH, expand = True)

HEAD_BOX = Label(MAINFRAME_ONE, bg = 'black', bd = 0, relief = RAISED, text = 'VIRTUAL STORE-FRONT',
              wraplength = 800, font = 'system 18 ', padx = 2, pady = 20, fg = 'green2', anchor = W,
              height = 0)
      
HEAD_BOX.pack(side = TOP)

MAINFRAME_TWO = LabelFrame(MAINFRAME, bd = 7, bg = 'grey', width = 400, height = 540,
                              padx = 5, relief = SUNKEN, pady = 10, text = 'TASK-MASTER',
                              font = 'system 10 bold', fg = 'grey30')

MAINFRAME_TWO.pack_propagate(0)
MAINFRAME_TWO.pack(side = LEFT, fill = BOTH, expand = True)

MAINFRAME_TWO_DISPLAY = Frame(MAINFRAME_TWO, bd = 4, bg = 'black', width = 10, height = 5,
                                   padx = 5, pady = 5, relief = RAISED)
MAINFRAME_TWO_DISPLAY.pack(side = TOP, fill = BOTH, expand = True)

MAINFRAME_THREE = LabelFrame(MAINFRAME, bd = 7, bg = 'grey',
                                     width = 310, height = 540,
                                      padx = 5, relief = SUNKEN,
                                       text = 'ELECTRICITY', font = 'System 10 bold', 
                                       fg = 'grey30', pady = 5)
MAINFRAME_THREE.pack_propagate(0)
MAINFRAME_THREE.pack(side = RIGHT)
################################################################
# The Outermost First Frame (Social Profile Frame)
PROFILE_FRAME = LabelFrame(MASTER_FRAME, bd = 7, bg = 'grey', width = 30, height = 280
                               , relief = SUNKEN, text = 'CREATIVE CORE', 
                               font = 'System 10 bold', fg = 'grey30') 
PROFILE_FRAME.pack_propagate(0)
PROFILE_FRAME.pack(side = TOP, fill = BOTH)


PROFILE_FRAME_ONE = Frame(PROFILE_FRAME, bd = 7, bg = 'black', width = 10, height = 215
                               , relief = SUNKEN, padx = 5)
PROFILE_FRAME_ONE.pack_propagate(0)
PROFILE_FRAME_ONE.pack(side = TOP, fill = BOTH)
################################################################
MID_FRAME = Frame(MASTER_FRAME, bd = 7, width = 400, height = 50, padx = 4, 
                        pady = 0, relief = RAISED, bg = 'black')

MID_FRAME.pack_propagate(0)

MID_FRAME.pack(side = TOP, expand = True, fill = BOTH)
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
#################################################################
# Then run the mainloop 
root.mainloop()