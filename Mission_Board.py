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

Picture1 = PhotoImage(file = 'tree of life.png')

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

MAINFRAME_2 = LabelFrame(MAINFRAME_0, bd = 7, bg = 'grey', width = 400, height = 540,
                              padx = 5, relief = SUNKEN, pady = 10, text = 'TASK-MASTER',
                              font = 'system 10 bold', fg = 'grey30')

MAINFRAME_2.pack_propagate(0)
MAINFRAME_2.pack(side = LEFT, fill = BOTH, expand = True)

MAINFRAME_2_DISPLAY = Frame(MAINFRAME_2, bd = 4, bg = 'black', width = 10, height = 5,
                                   padx = 5, pady = 5, relief = RAISED)
MAINFRAME_2_DISPLAY.pack(side = TOP, fill = BOTH, expand = True)

MAINFRAME_3 = LabelFrame(MAINFRAME_0, bd = 7, bg = 'grey',
                                     width = 310, height = 540,
                                      padx = 5, relief = SUNKEN,
                                       text = 'ELECTRICITY', font = 'System 10 bold', 
                                       fg = 'grey30', pady = 5)
MAINFRAME_3.pack_propagate(0)
MAINFRAME_3.pack(side = RIGHT)

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

PROFILE_FRAME_2 = Frame(PROFILE_FRAME_1, bd = 2, bg = 'white', 
                               relief = FLAT)
PROFILE_FRAME_2.pack_propagate(0)
PROFILE_FRAME_2.pack(side = LEFT, padx = 2, pady = 8)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# 

lblProfilePicture = Label(PROFILE_FRAME_2, image = Picture1,
                        width = 140, height = 180, relief = RAISED,
                        bg = 'white', bd = 1)
lblProfilePicture.pack_propagate(0)
lblProfilePicture.pack(fill = BOTH, expand = True)

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
