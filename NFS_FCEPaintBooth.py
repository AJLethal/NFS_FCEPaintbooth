#!/usr/bin/env python3

##    MIT License
##
##    Copyright (c) 2025 and later AJ_Lethal
##
##    Permission is hereby granted, free of charge, to any person obtaining a copy
##    of this software and associated documentation files (the "Software"), to deal
##    in the Software without restriction, including without limitation the rights
##    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##    copies of the Software, and to permit persons to whom the Software is
##    furnished to do so, subject to the following conditions:
##
##    The above copyright notice and this permission notice shall be included in all
##    copies or substantial portions of the Software.
##
##    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
##    SOFTWARE.

import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import IntVar
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
import colorsys
import io
import struct
import copy
import csv
import random
import ast

sIconData = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAC4jAAAuIwF4pT92AAAAB3RJTUUH6QMGFhUzD5qdJgAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAJ6SURBVDjLjZPBaxx1FMc/772ZycxsJrupTVN3S5NLa0wKgRQs9eAhCwXxHIie9Sh4EPQPkCLk6kWvHnIzoL20lGDx0JPNQehBtCqlpGmjIWazG2Z+M8+Dq4gezLu8B1/eF77w+cLpJtna2jq7vr7+BbAP7K+srOxubGy8F53SoFxcXLw0GAxuAC2A1dXV3X6//+VpDajr+od+v//dwcHBtSRJ6qWlpa/m5uYeyyn/5cqNK8XaG2s3e0Vvtvdi73a32721vLz8VBDABBFAgQmYeX3GNNNYM5XR7mgqDEM3PZ++68GfzDfzdx9sP7gH4CNH7KwRT8dYahoV0awV9ppmel0mpCuJTGPkwJ7XXoXj8E1cxNcHPw7e6VztDIc/DzGNFRHJVeRtjI8QpnRKX6mresdSq8rfyk810VkxiaI8Srxxscwe5hfz/XAcMHFJvPEPEZZF5IO6rDdt2h6F4/C1pTaHcwFlGH4P9zTSy974AXCUtJNH1WHlAlxD2RSTbU11T3N1ywzN1OyMLYrKMD4f9zx4Iiopwk5URJfjdnxHYvnEgDdx1mgocO7TcNEbXwCEiude87KPPKFmx9pWUNPx4B1RXsXlcQTsAc+ATa/8rTrU5+RE1E/8Y2/5quZqXuqEnuhDL31SUy2sY1fDUZ1byTkDngBngBngEPiFhp+88rbXPvLGn9HwHOcFnAZn6KX/SiDz2m/+BVIMJOO7+pueWLDMkEyw3ECIEC5Zy963lt3X1D77J4ltYB6YHsfaH5sJMImwoKn2oyK6oJP6uU3adnVYVf9G2YACWABeGkcrxtpTMfnWWva9tvSoKRua0PxvB2wcz/7bjj/XH7Xm6hWCkmUpAAAAAElFTkSuQmCC'
lIconData = b'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'

## check for unsaved changes upon being called on opening
def unsavedChanges():
    if dirtyFlag == 1:
        confirmChanges = messagebox.askyesnocancel("Confirm exit", "You have unsaved changes, do you want to save before exiting?")
        if confirmChanges is None:
            return
        elif confirmChanges:
            saveFce()
            root.destroy()
        else:
            root.destroy()
    else:
        root.destroy() 

## defining main window
root = tk.Tk()
root.title("NFS FCE Paint Booth")
root.protocol('WM_DELETE_WINDOW', unsavedChanges)
root.resizable(False, False)
smallIcon = tk.PhotoImage(data=sIconData)
largeIcon = tk.PhotoImage(data=lIconData)
root.iconphoto(False, largeIcon, smallIcon)

## "About" dialog
def aboutDlg():
    aboutMsg = messagebox.showinfo("About NFS FCE Paint Booth",
                                   "NFS FCE Paint Booth v1.0 \n"
                                    "(c) 2025 and later AJ_Lethal\n\n"
                                    "Licensed under the MIT License")
    
## initializing general variables
colors = [[0,0,0,0],[]]
for i in range(16):
    colors[1].append(list())
    colors[1][i].append(list())
    colors[1][i].append(list())
    colors[1][i].append(list())
    colors[1][i].append(list())

colorList=[]
colorAmount = 0
colorListVar = tk.StringVar()
selectedColor = 0

fceType = tk.StringVar()
fceTypeStr = tk.StringVar()
fcePath = tk.StringVar()
fcePathStr = tk.StringVar()

hueFieldsVars = [0,0,0,0]
hueFieldsVars[0] = tk.IntVar()
hueFieldsVars[1] = tk.IntVar()
hueFieldsVars[2] = tk.IntVar()
hueFieldsVars[3] = tk.IntVar()

satFieldsVars = [0,0,0,0]
satFieldsVars[0] = tk.IntVar()
satFieldsVars[1] = tk.IntVar()
satFieldsVars[2] = tk.IntVar()
satFieldsVars[3] = tk.IntVar()

briFieldsVars = [0,0,0,0]
briFieldsVars[0] = tk.IntVar()
briFieldsVars[1] = tk.IntVar()
briFieldsVars[2] = tk.IntVar()
briFieldsVars[3] = tk.IntVar()

tolFieldsVars = [0,0,0,0]
tolFieldsVars[0] = tk.IntVar()
tolFieldsVars[1] = tk.IntVar()
tolFieldsVars[2] = tk.IntVar()
tolFieldsVars[3] = tk.IntVar()

htmlFieldsVars = ['','','','']
htmlFieldsVars[0] = tk.StringVar()
htmlFieldsVars[1] = tk.StringVar()
htmlFieldsVars[2] = tk.StringVar()
htmlFieldsVars[3] = tk.StringVar()

buttonColors = ['','','','']
buttonColors[0] = ''
buttonColors[1] = ''
buttonColors[2] = ''
buttonColors[3] = ''

buttonColorsDisp = ['','','','']
buttonColorsDisp[0] = ''
buttonColorsDisp[1] = ''
buttonColorsDisp[2] = ''
buttonColorsDisp[3] = ''

randHue = 0
randSat = 0
randBri = 0

rndAllColAmount = tk.IntVar()
rndAllColAmount.set(10)

dirtyFlag = 0
           

## functions to validate characters inputted in text boxes
def inputCallback(input):
    if len(input) > 3:
        return False
    if input.isdigit() and input != "" and int(input) <= 255 and int(input) >= 0:
        return True
    elif input == "":
        return True
    else:
        return False
      
def inputCallbackHue(input):
    if len(input) > 3:
        return False
    if input.isdigit() and input != "" and int(input) <= 360 and int(input) >= 0:
        return True
    elif input == "":
        return True
    else:
        return False
 
def inputCallbackHtml(string, newString):
    acceptedChars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F','#','']
    for i in str(newString):
        if len(newString) > 7:
            return False
        if i not in acceptedChars:
            return False
        else:
            return True
    for i in str(string):
        if len(string) > 7:
            return False
        if i not in acceptedChars:
            return False
        else:
            return True
    
## function to open FCE file and load color data, also enables disabled UI elements and selects first color
def openFce():
    global dirtyFlag
    if dirtyFlag == 1:
        confirmChanges = messagebox.askyesnocancel("Confirm changes", "You have unsaved changes, do you want to save?")
        if confirmChanges is None:
            return
        elif confirmChanges:
            saveFce()
    global fcePath
    global fcePathPrev
    global fceType
    global colorAmount
    global colorsPrev
    if fcePath != "":
        fcePathPrev = fcePath
    fcePath = filedialog.askopenfilename(title="Open NFS3/HS .fce file", filetypes=[("NFS3/HS car mesh", "*.fce *.FCE")])
    if fcePath == "":
        fcePath = fcePathPrev
        return
    with open (fcePath, 'rb') as file:
        hueFieldSbox1.state(['!disabled'])
        satFieldSbox1.state(['!disabled'])
        briFieldSbox1.state(['!disabled'])
        tolFieldSbox1.state(['!disabled'])
        htmlField1.state(['!disabled'])
        
        hueFieldSbox2.state(['!disabled'])
        satFieldSbox2.state(['!disabled'])
        briFieldSbox2.state(['!disabled'])
        tolFieldSbox2.state(['!disabled'])
        htmlField2.state(['!disabled'])

        hueFieldSbox3.state(['!disabled'])
        satFieldSbox3.state(['!disabled'])
        briFieldSbox3.state(['!disabled'])
        tolFieldSbox3.state(['!disabled'])
        htmlField3.state(['!disabled'])

        hueFieldSbox4.state(['!disabled'])
        satFieldSbox4.state(['!disabled'])
        briFieldSbox4.state(['!disabled'])
        tolFieldSbox4.state(['!disabled'])
        htmlField4.state(['!disabled'])
        
        file.seek(0)
        if file.read(4) == b'\x14\x10\x10\x00':
            fceType = 'NFSHS'
            colorPos = file.seek(2080)
            colors[0] = list(struct.unpack('I', file.read(4)))
            for i in range(3):
                colors[0].append(0)
            colorAmount = colors[0][0]
            colorPos = file.seek(2084)
            for i in range(colorAmount):
                colorPos = file.tell()
                for x in range(4):
                    colors[1][i][x] = list(struct.unpack('>4B', file.read(4)))
                    colors[1][i][x][0] = round(colors[1][i][x][0] * 1.411764705882353)
                    if x < 3:
                        colorPos = colorPos + 64
                    file.seek(colorPos)
                colorPos = colorPos-188
                file.seek(colorPos)                
        else:
            fceType = 'NFS3'
            colorPos = file.seek(2044)
            colors[0] = list(struct.unpack('I', file.read(4)))
            for i in range(3):
                colors[0].append(i)
            colorAmount = colors[0][0]
            colorPos = file.seek(2048)
            for i in range(colorAmount):
                colorPos = file.tell()
                for x in range(4):
                    colors[1][i][x] = list(struct.unpack('4I', file.read(16)))
                    colors[1][i][x][0] = round(colors[1][i][x][0] * 1.411764705882353)
                    if x == 1:
                        colorPos = colorPos + 260
                    file.seek(colorPos)
                    if x == 1 or x == 3:
                        colors[1][i][x] = [0,0,0,0]
                colorPos = colorPos - 244
                file.seek(colorPos)

    for i in range(16-colorAmount):
        colors[1][i+colorAmount][0:4] = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    colorsPrev = []
    if colorsPrev:
        colorsPrev.clear()
    colorsPrev = copy.deepcopy(colors)
    
    if fcePath != "":
        saveFCEBtn.state(['!disabled'])
        saveAsFCEBtn.state(['!disabled'])

    openFileLabel()    
    typeLabel['textvariable'] = fceTypeStr
    fceTypeStr.set(f'Type: {fceType}')
    
    colorListUI['state']=tk.NORMAL
    if colorAmount < 16:
        addColorBtn.state(['!disabled'])
        addRndColorBtn.state(['!disabled'])
        dupColorBtn.state(['!disabled'])
    if colorAmount > 0:
        remColorBtn.state(['!disabled'])
    rndAllColorsBtn.state(['!disabled'])
    rndColorsLbl.state(['!disabled'])
    rndColorsSbox.state(['!disabled'])
    importColorsBtn.state(['!disabled'])
    exportColorsBtn.state(['!disabled'])
    colorListBoxPopulate()
    colorListUI.selection_clear(0, tk.END)
    colorListUI.selection_set(0)
    loadColorUI()
    
    if fceType == 'NFSHS':
        hueLabel.state(['!disabled'])
        satLabel.state(['!disabled'])
        briLabel.state(['!disabled'])
        tolLabel.state(['!disabled'])
        
        colorLabel1.state(['!disabled'])
        colorLabel2.state(['!disabled'])
        colorLabel3.state(['!disabled'])
        colorLabel4.state(['!disabled'])
        htmlLabel1.state(['!disabled'])
        htmlLabel2.state(['!disabled'])
        htmlLabel3.state(['!disabled'])
        htmlLabel4.state(['!disabled'])
        colorButton1['state']=tk.NORMAL
        colorButton2['state']=tk.NORMAL
        colorButton3['state']=tk.NORMAL
        colorButton4['state']=tk.NORMAL
    else:
        hueLabel.state(['!disabled'])
        satLabel.state(['!disabled'])
        briLabel.state(['!disabled'])
        tolLabel.state(['!disabled'])
        
        hueFieldSbox1.state(['!disabled'])
        satFieldSbox1.state(['!disabled'])
        briFieldSbox1.state(['!disabled'])
        tolFieldSbox1.state(['!disabled'])
        
        colorLabel1.state(['!disabled'])
        colorLabel2.state(['disabled'])
        colorLabel3.state(['!disabled'])
        colorLabel4.state(['disabled'])
        htmlLabel1.state(['!disabled'])
        htmlLabel2.state(['disabled'])
        htmlLabel3.state(['!disabled'])
        htmlLabel4.state(['disabled'])
        colorButton1['state']=tk.NORMAL
        colorButton2['state']=tk.DISABLED
        colorButton3['state']=tk.NORMAL
        colorButton4['state']=tk.DISABLED

        hueFieldSbox1.state(['!disabled'])
        satFieldSbox1.state(['!disabled'])
        briFieldSbox1.state(['!disabled'])
        tolFieldSbox1.state(['!disabled'])
        htmlField1.state(['!disabled'])

        hueFieldSbox2.state(['disabled'])
        satFieldSbox2.state(['disabled'])
        briFieldSbox2.state(['disabled'])
        tolFieldSbox2.state(['disabled'])
        htmlField2.state(['disabled'])

        hueFieldSbox3.state(['!disabled'])
        satFieldSbox3.state(['!disabled'])
        briFieldSbox3.state(['!disabled'])
        tolFieldSbox3.state(['!disabled'])
        htmlField3.state(['!disabled'])

        hueFieldSbox4.state(['disabled'])
        satFieldSbox4.state(['disabled'])
        briFieldSbox4.state(['disabled'])
        tolFieldSbox4.state(['disabled'])
        htmlField4.state(['disabled'])
    file.close()
    dirtyFlag = 0

## sets fileLabel to active file
def openFileLabel():
    fileLabel['textvariable'] = fcePathStr
    fcePathStr.set(f'File: {fcePath}')

## copies colors list and adjusts hue for saving
def colorsListForSave():
    global colorsWrite
    colorsWrite = copy.deepcopy(colors)
    for i in range(colorAmount):
        for x in range(4):
            colorsWrite[1][i][x][0] = round(colorsWrite[1][i][x][0] / 1.411764705882353)

## saves file
def saveFce():
    global dirtyFlag
    global fcePath
    fceSavePath = fcePath
    colorsListForSave()
    if fceType == 'NFSHS':
        with open (fceSavePath, 'r+b') as fileSave:
            colorPos = fileSave.seek(2080)
            fileSave.write(struct.pack('B',colorsWrite[0][0]))
            colorPos = fileSave.seek(2084)
            for i in range(colorAmount):
                colorPos = fileSave.tell()
                for x in range(4):
                    fileSave.write(struct.pack('>4B',
                                                colorsWrite[1][i][x][0],
                                                colorsWrite[1][i][x][1],
                                                colorsWrite[1][i][x][2],
                                                colorsWrite[1][i][x][3])
                                    )
                    if x < 3:
                        colorPos = colorPos + 64
                    fileSave.seek(colorPos)
                colorPos = colorPos - 188
                fileSave.seek(colorPos)
        fileSave.close()
        
    else:
        with open (fceSavePath, 'r+b') as fileSave:
            colorPos = fileSave.seek(2044)
            fileSave.write(struct.pack('B',colorsWrite[0][0]))
            colorPos = fileSave.seek(2304)
            fileSave.write(struct.pack('B',colorsWrite[0][0]))
            colorPos = fileSave.seek(2048)
            for i in range(colorAmount):
                colorPos = fileSave.tell()
                fileSave.write(struct.pack('4I',
                                            colorsWrite[1][i][0][0],
                                            colorsWrite[1][i][0][1],
                                            colorsWrite[1][i][0][2],
                                            colorsWrite[1][i][0][3])
                                )
                colorPos = colorPos + 260
                fileSave.seek(colorPos)
                fileSave.write(struct.pack('4I',
                                            colorsWrite[1][i][2][0],
                                            colorsWrite[1][i][2][1],
                                            colorsWrite[1][i][2][2],
                                            colorsWrite[1][i][2][3])
                                )
                colorPos = colorPos - 244
                fileSave.seek(colorPos)
        fileSave.close()
        
    fileLabel['textvariable'] = fcePathStr
    fcePathStr.set(f'File saved to: {fcePath}')
    loadColorUI()
    fileLabel.after(5000, openFileLabel)
    dirtyFlag = 0

## saves file as another file
def saveFceAs():
    global dirtyFlag
    global fcePath
    global fcePathPrev
    colorsListForSave()
    fcePathPrev = fcePath
    with open (fcePath, 'rb') as file:
        fceFile = file.read()
        file.seek(0)       
        if fceType == 'NFSHS':
            fceSavePath = filedialog.asksaveasfilename(title="Save NFSHS FCE file as...", filetypes=[("NFSHS FCE mesh file", "*.fce")], defaultextension=[".fce"])
            if fceSavePath == "":
                fcePath = fcePathPrev
                return
            with open (fceSavePath, 'wb') as fileSave:
                fileSave.write(fceFile)
                colorPos = fileSave.seek(2080)
                fileSave.write(struct.pack('B',colorsWrite[0][0]))
                colorPos = fileSave.seek(2084)
                for i in range(colorAmount):
                    colorPos = fileSave.tell()
                    for x in range(4):
                        fileSave.write(struct.pack('>4B',
                                                    colorsWrite[1][i][x][0],
                                                    colorsWrite[1][i][x][1],
                                                    colorsWrite[1][i][x][2],
                                                    colorsWrite[1][i][x][3])
                                        )
                        if x < 3:
                            colorPos = colorPos + 64
                        fileSave.seek(colorPos)
                    colorPos = colorPos - 188
                    fileSave.seek(colorPos)
            fileSave.close()
            
        else:
            fceSavePath = filedialog.asksaveasfilename(title="Save NFS3 FCE file as...", filetypes=[("NFS3 FCE mesh file", "*.fce *.FCE")], defaultextension=[".fce"])
            if fceSavePath == "":
                fcePath = fcePathPrev
                return
            with open (fceSavePath, 'wb') as fileSave:
                fileSave.write(fceFile)
                colorPos = fileSave.seek(2044)
                fileSave.write(struct.pack('B',colorsWrite[0][0]))
                colorPos = fileSave.seek(2304)
                fileSave.write(struct.pack('B',colorsWrite[0][0]))
                colorPos = fileSave.seek(2048)
                for i in range(colorAmount):
                    colorPos = fileSave.tell()
                    fileSave.write(struct.pack('4I',
                                                colorsWrite[1][i][0][0],
                                                colorsWrite[1][i][0][1],
                                                colorsWrite[1][i][0][2],
                                                colorsWrite[1][i][0][3])
                                    )
                    colorPos = colorPos + 260
                    fileSave.seek(colorPos)
                    fileSave.write(struct.pack('4I',
                                                colorsWrite[1][i][2][0],
                                                colorsWrite[1][i][2][1],
                                                colorsWrite[1][i][2][2],
                                                colorsWrite[1][i][2][3])
                                    )
                    colorPos = colorPos - 244
                    fileSave.seek(colorPos)
            fileSave.close()
            
        fcePath = fceSavePath
        fileLabel['textvariable'] = fcePathStr
        fcePathStr.set(f'File saved to: {fceSavePath}')
        loadColorUI()
        fileLabel.after(5000, openFileLabel)
    dirtyFlag = 0

## function to load color into color fields upon selecting it in the listbox
def loadColorUI(*args):
    global selectedColor
    selectedColorInput = colorListUI.curselection()
    if len(selectedColorInput)==1:
        selectedColor = int(selectedColorInput[0])

        if fceType == 'NFSHS':
            for i in range(4):
                hueFieldsVars[i].set(colors[1][selectedColor][i][0])
                satFieldsVars[i].set(colors[1][selectedColor][i][1])
                briFieldsVars[i].set(colors[1][selectedColor][i][2])
                tolFieldsVars[i].set(colors[1][selectedColor][i][3])

        else:
            for i in range(4):
                if i == 1 or i == 3:
                    hueFieldsVars[i].set(0)
                    satFieldsVars[i].set(0)
                    briFieldsVars[i].set(0)
                    tolFieldsVars[i].set(0)
                else:
                    hueFieldsVars[i].set(colors[1][selectedColor][i][0])
                    satFieldsVars[i].set(colors[1][selectedColor][i][1])
                    briFieldsVars[i].set(colors[1][selectedColor][i][2])
                    tolFieldsVars[i].set(colors[1][selectedColor][i][3])
        updateColorButtons()
                
## convert rgb values to html codes    
def rgb2hex(r, g, b):
  return ('{:02X}' * 3).format(r, g, b)

## convert hex codes to rgb values
def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    
## updates colors when called and updates colors list
def updateColor(*args):
    global dirtyFlag
    global colorsPrev
    global fceType
    if fceType == 'NFSHS':
        for i in range(4):
            colors[1][selectedColor][i][0] = hueFieldsVars[i].get()
            colors[1][selectedColor][i][1] = satFieldsVars[i].get()
            colors[1][selectedColor][i][2] = briFieldsVars[i].get()
            colors[1][selectedColor][i][3] = tolFieldsVars[i].get()
            
    else:
        for i in range(4):
            if i == 1:
                colors[1][selectedColor][i] = [0,0,0,0]
            elif i == 3:
                colors[1][selectedColor][i] = [0,0,0,0]
            else:
                colors[1][selectedColor][i][0] = hueFieldsVars[i].get()
                colors[1][selectedColor][i][1] = satFieldsVars[i].get()
                colors[1][selectedColor][i][2] = briFieldsVars[i].get()
                colors[1][selectedColor][i][3] = tolFieldsVars[i].get()

    if colorsPrev == colors:
        dirtyFlag = 0
    elif colorsPrev != colors:
        dirtyFlag = 1
        
    updateColorButtons()

## updates HSV color fields based on the html fields input
def updateColorHtml(*args):
    global dirtyFlag
    global colorsPrev
    for i in range(4):
        htmlColorRaw = htmlFieldsVars[i].get()
        htmlColorRaw = htmlColorRaw.strip('#')
        rgbColor = hex_to_rgb(htmlColorRaw)
        hsvColorTemp = colorsys.rgb_to_hsv(rgbColor[0]/255,
                                         rgbColor[1]/255,
                                         rgbColor[2]/255)
        hueFieldsVars[i].set(round((hsvColorTemp[0]*255)*1.411764705882353))
        satFieldsVars[i].set(round((hsvColorTemp[1]*255)))
        briFieldsVars[i].set(round((hsvColorTemp[2]*255)))

    if htmlFieldsVars[3].get() == '#463612':
        satFieldsVars[3].set(190)

    updateColor()

## updates color buttons
def updateColorButtons(*args):
    global hue, sat, bri, tol
    for i in range(4):
        hue = hueFieldsVars[i].get()
        sat = satFieldsVars[i].get()
        bri = briFieldsVars[i].get()
        tol = tolFieldsVars[i].get()
        
        hueNFS = (hue/1.411764705882353)/255
        satNFS = sat/255
        briNFS = bri/255
        tolNFS = tol/255
        briTol = briNFS
        if tolNFS == 0:
            tolNFS = 0.001
        else:
            briTol = (briNFS+(briNFS/(0.94/tolNFS)))
        if briTol > 1:
            briTol = 1
        else:
            briTol

        rgbRaw = list(colorsys.hsv_to_rgb(hueNFS, satNFS, briNFS))
        rgbRawDisp = list(colorsys.hsv_to_rgb(hueNFS, satNFS, briTol))

        hexRaw=rgb2hex(round(rgbRaw[0]*255)
                      ,round(rgbRaw[1]*255)
                      ,round(rgbRaw[2]*255))
        
        hexRawDisp=rgb2hex(round(rgbRawDisp[0]*255)
                          ,round(rgbRawDisp[1]*255)
                          ,round(rgbRawDisp[2]*255))
        
        buttonColors[i] = f'#{hexRaw}'
        buttonColorsDisp[i] = f'#{hexRawDisp}'
        htmlFieldsVars[i].set(f'#{hexRaw}')
        
    colorButton1.config(background=buttonColorsDisp[0])
    colorButton2.config(background=buttonColorsDisp[1])
    colorButton3.config(background=buttonColorsDisp[2])
    colorButton4.config(background=buttonColorsDisp[3])

## function to populate color listbox
def colorListBoxPopulate():
    colorList.clear()
    for i in range(colorAmount):
        i=i+1
        colorList.append(f"Color {i}")
    colorListVar.set(colorList)

## color chooser function
def chooseColor(i):
    chosenColor = colorchooser.askcolor(buttonColors[i], title="Select color")
    if chosenColor != (None, None):
        chosenColorHsvRaw = (colorsys.rgb_to_hsv(chosenColor[0][0]/255.0,
                                              chosenColor[0][1]/255.0,
                                              chosenColor[0][2]/255.0))
        chosenColorHsvNfsHue = hueFieldsVars[i].set(round((chosenColorHsvRaw[0]*255) * 1.411764705882353))
        chosenColorHsvNfsSat = satFieldsVars[i].set(round(chosenColorHsvRaw[1]*255))
        chosenColorHsvNfsBri = briFieldsVars[i].set(round(chosenColorHsvRaw[2]*255))
    else:
        return
    updateColor()
        
## adds a color entry when called
def addColor():
    global dirtyFlag
    global colorAmount
    colorAmount = colorAmount + 1
    colorAmountIndex = colorAmount - 1
    colors[0][0] = colorAmount
    if fceType == 'NFSHS':
        colors[1][colorAmountIndex][0] = [180,192,127,127]
        colors[1][colorAmountIndex][1] = [0,0,64,127]
        colors[1][colorAmountIndex][2] = [0,0,127,127]
        colors[1][colorAmountIndex][3] = [42,190,70,127]
    else:
        colors[1][colorAmountIndex][0] = [180,192,127,127]
        colors[1][colorAmountIndex][2] = [0,0,128,127]
    colorListBoxPopulate()
    if colorAmount == 16:
        dupColorBtn.state(['disabled'])
        addColorBtn.state(['disabled'])
        addRndColorBtn.state(['disabled'])
    else:
        remColorBtn.state(['!disabled'])
    dirtyFlag = 1

## removes selected color entry when called        
def remColor():
    global dirtyFlag
    global colorAmount
    colorAmount = colorAmount - 1
    colors[0][0] = colorAmount
    colors[1].pop(selectedColor)
    colors[1].append(list())
    colors[1][15].append([0,0,0,0])
    colors[1][15].append([0,0,0,0])
    colors[1][15].append([0,0,0,0])
    colors[1][15].append([0,0,0,0])
    colorListBoxPopulate()
    loadColorUI()    
    if colorAmount == 0:
        remColorBtn.state(['disabled'])
    else:
        dupColorBtn.state(['!disabled'])
        addColorBtn.state(['!disabled'])
        addRndColorBtn.state(['!disabled'])
    dirtyFlag = 1

## duplicates selected color when called
def dupColor():
    global dirtyFlag
    global colorAmount
    colorAmount = colorAmount + 1
    colorAmountIndex = colorAmount - 1
    colors[0][0] = colorAmount
    if fceType == 'NFSHS':
        for i in range(4):
            colors[1][colorAmountIndex][i] = list(colors[1][selectedColor][i])
    else:
        colors[1][colorAmountIndex][0] = list(colors[1][selectedColor][0])
        colors[1][colorAmountIndex][2] = list(colors[1][selectedColor][2])
    colorListBoxPopulate()
    if colorAmount == 16:
        dupColorBtn.state(['disabled'])
        addColorBtn.state(['disabled'])
        addRndColorBtn.state(['disabled'])
    else:
        remColorBtn.state(['!disabled'])
    dirtyFlag = 1

## random color function
def randNfsColor():
    global randHue, randSat, randBri
    randHue = random.randrange(0, 360)
    randSat = random.randrange(0, 255)
    if randSat <= 64:
        randBri = random.randrange(8, 180)
    else:
        randBri = random.randrange(8, 160)

## adds a color entry with randomized colors when called
def addRndColor():
    global dirtyFlag
    global colorAmount
    colorAmount = colorAmount + 1
    colorAmountIndex = colorAmount - 1
    colors[0][0] = colorAmount
    if fceType == 'NFSHS':
        for i in range(3):
            randNfsColor()
            colors[1][colorAmountIndex][i] = [randHue,randSat,randBri,127]
        colors[1][colorAmountIndex][3] = [42,190,70,127]
    else:
        for i in range(3):
            randNfsColor()
            colors[1][colorAmountIndex][i] = [randHue,randSat,randBri,127]
    colorListBoxPopulate()
    if colorAmount == 16:
        dupColorBtn.state(['disabled'])
        addColorBtn.state(['disabled'])
        addRndColorBtn.state(['disabled'])
    else:
        remColorBtn.state(['!disabled'])
    dirtyFlag = 1

## makes a whole new color table, amount of colors specfied in associated spinbox
def rndAllColors():
    global dirtyFlag
    global colorAmount
    colorAmount = rndAllColAmount.get()
    colors[0][0] = colorAmount
    colorAmountIndex = colorAmount - 1           
    if fceType == 'NFSHS':
        for i in range(colorAmount):
            colors[1][i][3] = [42,190,70,127]
            for x in range(3):
                randNfsColor()
                colors[1][i][x] = [randHue,randSat,randBri,127]
    else:
        for i in range(colorAmount):
            for x in range(2):
                if x == 1:
                    x = 2
                randNfsColor()
                colors[1][i][x] = [randHue,randSat,randBri,127]             
    colorListBoxPopulate()
    colorListUI.selection_clear(0, tk.END)
    colorListUI.selection_set(0)
    loadColorUI()
    if colorAmount == 16:
        dupColorBtn.state(['disabled'])
        addColorBtn.state(['disabled'])
        addRndColorBtn.state(['disabled'])
    else:
        remColorBtn.state(['!disabled'])
    dirtyFlag = 1

## imports color table from a CSV file
def csvImport():
    global dirtyFlag
    global colorAmount
    csvFilePath = filedialog.askopenfilename(title="Import .csv file", filetypes=[("Comma-separated values", "*.csv")])
    with open(csvFilePath, 'r', newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        colors[0].clear()
        colors[1].clear()
        colors[0] = next(reader) 
        for row in reader:
            colors[1].append(row)
    csvFile.close() 
    for i in range(4):
        colors[0][i]=ast.literal_eval(colors[0][i])

    for i in range(16):
        for x in range(4):
            colors[1][i][x]=ast.literal_eval(colors[1][i][x])
    colorAmount = colors[0][0]
    colorListBoxPopulate()
    colorListUI.selection_clear(0, tk.END)
    colorListUI.selection_set(0)
    loadColorUI()
    dirtyFlag = 1
    

## exports current color table to a CSV file
def csvExport():
    csvFileSavePath = filedialog.asksaveasfilename(title="Export colors to .csv file", filetypes=[("Comma-separated values", ".csv")], defaultextension=".csv")
    with open(csvFileSavePath, 'w', newline='') as csvSaveFile:
        if fceType == 'NFS3':
            for i in range(colorAmount):
                colors[1][i][1] = [0,0,64,128]
                colors[1][i][3] = [30,190,70,128]
        writer = csv.writer(csvSaveFile)
        writer.writerow(colors[0])
        writer.writerows(colors[1])
    csvSaveFile.close()

## defining window frames
mainFrame = ttk.Frame(root, padding=(5,5,10,10))
mainFrame.grid(row = 0, column = 0)
topFrame = ttk.Frame(mainFrame)
topFrame.grid(row = 0, column = 0, padx = '5', pady = '2', columnspan=6, sticky='NSEW')
leftFrame = ttk.Frame(mainFrame)
leftFrame.grid(row = 1, column = 0, padx = '5', pady = '5', sticky='NSEW')
rightFrame = ttk.Frame(mainFrame)
rightFrame.grid(row = 1, column = 1, padx = '5', pady = '5')
bottomFrame = ttk.Frame(mainFrame)
bottomFrame.grid(row = 2, column = 0, padx = '5', pady = '5', columnspan=7, sticky='NSEW')

mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)
topFrame.columnconfigure(0, weight=0)
topFrame.columnconfigure(1, weight=0)
topFrame.columnconfigure(2, weight=0)
topFrame.columnconfigure(3, weight=1)
leftFrame.columnconfigure(0, weight=1)
rightFrame.columnconfigure(0, weight=3)
rightFrame.columnconfigure(1, weight=3)
rightFrame.columnconfigure(2, weight=3)
rightFrame.columnconfigure(3, weight=3)
rightFrame.columnconfigure(4, weight=3)
rightFrame.columnconfigure(5, weight=3)
rightFrame.columnconfigure(6, weight=3)
bottomFrame.columnconfigure(0, weight=1)
bottomFrame.columnconfigure(1, weight=1)

## defining UI elements
openFCEBtn = ttk.Button(topFrame, text='Open FCE File', command=openFce)
openFCEBtn.grid(row = 0, column=0, sticky="W")
saveFCEBtn = ttk.Button(topFrame, text='Save FCE File', command=saveFce, state='disabled')
saveFCEBtn.grid(row = 0, column=1, sticky="W")
saveAsFCEBtn = ttk.Button(topFrame, text='Save FCE File As...', command=saveFceAs, state='disabled')
saveAsFCEBtn.grid(row = 0, column=2, sticky="W")
aboutBtn = ttk.Button(topFrame, text='About', command=aboutDlg)
aboutBtn.grid(row = 0, column=3, sticky="E")

colorListUI = tk.Listbox(leftFrame, height = 10, listvariable=colorListVar, exportselection = 'False', state='disabled')
colorListUI.grid(row=0, column=0, columnspan=2, sticky="NSEW")
colorListUI.bind('<<ListboxSelect>>', loadColorUI)
colorListUI.selection_set(0)
colorListUISBar = ttk.Scrollbar(leftFrame, orient=tk.VERTICAL, command = colorListUI.yview)
colorListUISBar.grid(row=0, column=3, sticky="NSEW")
colorListUI.configure(yscrollcommand = colorListUISBar.set)

addColorBtn = ttk.Button(leftFrame, text="Add Color", state='disabled', command = addColor)
addColorBtn.grid(row = 4, column=0,sticky="NSEW")
remColorBtn = ttk.Button(leftFrame, text="Remove Color", state='disabled', command = remColor)
remColorBtn.grid(row = 4, column=1,sticky="NSEW")
dupColorBtn = ttk.Button(leftFrame, text="Duplicate Color", state='disabled', command = dupColor)
dupColorBtn.grid(row = 5, column=0,sticky="NSEW")
addRndColorBtn = ttk.Button(leftFrame, text="Add Random Color", state='disabled', command = addRndColor)
addRndColorBtn.grid(row = 5, column=1,sticky="NSEW")
rndAllColorsBtn = ttk.Button(leftFrame, text="Randomize All Colors", state='disabled', command = rndAllColors)
rndAllColorsBtn.grid(row = 6, column=0, sticky="NSEW", pady=5)
rndColorsLbl = ttk.Label(leftFrame, text="No. of colors:", state='disabled')
rndColorsLbl.grid(row = 6, column=1,sticky="W")
rndColorsSbox = ttk.Spinbox(leftFrame, from_=1, to=16, width=3, state='disabled', textvariable = rndAllColAmount)
rndColorsSbox.grid(row = 6, column=1,sticky="E")
importColorsBtn = ttk.Button(leftFrame, text="Import Colors", state='disabled', command = csvImport)
importColorsBtn.grid(row = 7, column=0,sticky="NSEW")
exportColorsBtn = ttk.Button(leftFrame, text="Export Colors", state='disabled', command = csvExport)
exportColorsBtn.grid(row = 7, column=1,sticky="NSEW")

hueLabel = ttk.Label(rightFrame, text="Hue", anchor="center", state='disabled')
hueLabel.grid(row = 0, column = 2, padx=2, pady=2, sticky='NSEW')
satLabel = ttk.Label(rightFrame, text="Sat", anchor="center", state='disabled')
satLabel.grid(row = 0, column = 3, padx=2, pady=2, sticky='NSEW')
briLabel = ttk.Label(rightFrame, text="Bri", anchor="center", state='disabled')
briLabel.grid(row = 0, column = 4, padx=2, pady=2, sticky='NSEW')
tolLabel = ttk.Label(rightFrame, text="Tol", anchor="center", state='disabled')
tolLabel.grid(row = 0, column = 5, padx=2, pady=2, sticky='NSEW')

colorLabel1 = ttk.Label(rightFrame, text="Primary color", state='disabled')
colorLabel1.grid(row = 1, column = 0, padx=2, pady=2, sticky='E')
colorButton1 = tk.Button(rightFrame, background='#000', relief='groove', width='2', command=lambda:chooseColor(0), state='disabled')
colorButton1.grid(row = 1, column = 1)
hueFieldSbox1 = ttk.Spinbox(rightFrame, from_=0, to=360, width=4, textvariable=hueFieldsVars[0], command=updateColor, state='disabled', justify='right')
hueFieldSbox1.grid(row = 1, column = 2, padx=2, pady=2)
hueFieldSbox1.bind('<Tab>', updateColor)
satFieldSbox1 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=satFieldsVars[0], command=updateColor, state='disabled', justify='right')
satFieldSbox1.grid(row = 1, column = 3, padx=2, pady=2)
satFieldSbox1.bind('<Tab>', updateColor)
briFieldSbox1 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=briFieldsVars[0], command=updateColor, state='disabled', justify='right')
briFieldSbox1.grid(row = 1, column = 4, padx=2, pady=2)
briFieldSbox1.bind('<Tab>', updateColor)
tolFieldSbox1 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=tolFieldsVars[0], command=updateColor, state='disabled', justify='right')
tolFieldSbox1.grid(row = 1, column = 5, padx=2, pady=2)
tolFieldSbox1.bind('<Tab>', updateColor)
htmlLabel1 = ttk.Label(rightFrame, text="Hex code:", state='disabled')
htmlLabel1.grid(row = 2, column = 2, sticky='E')
htmlField1 = ttk.Entry(rightFrame, textvariable=htmlFieldsVars[0], justify='right', width='15', state='disabled')
htmlField1.grid(row = 2, column = 3, columnspan=3, sticky="W")
htmlField1.bind('<Return>', updateColorHtml)

colorLabel2 = ttk.Label(rightFrame, text="Interior color", state='disabled')
colorLabel2.grid(row = 3, column = 0, padx=2, pady=2, sticky='E')
colorButton2 = tk.Button(rightFrame, background='#000', relief='groove', width='2', command=lambda:chooseColor(1), state='disabled')
colorButton2.grid(row = 3, column = 1)
hueFieldSbox2 = ttk.Spinbox(rightFrame, from_=0, to=360, width=4, textvariable=hueFieldsVars[1], command=updateColor, state='disabled', justify='right')
hueFieldSbox2.grid(row = 3, column = 2, padx=2, pady=2)
hueFieldSbox2.bind('<Tab>', updateColor)
satFieldSbox2 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=satFieldsVars[1], command=updateColor, state='disabled', justify='right')
satFieldSbox2.grid(row = 3, column = 3, padx=2, pady=2)
satFieldSbox2.bind('<Tab>', updateColor)
briFieldSbox2 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=briFieldsVars[1], command=updateColor, state='disabled', justify='right')
briFieldSbox2.grid(row = 3, column = 4, padx=2, pady=2)
briFieldSbox2.bind('<Tab>', updateColor)
tolFieldSbox2 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=tolFieldsVars[1], command=updateColor, state='disabled', justify='right')
tolFieldSbox2.grid(row = 3, column = 5, padx=2, pady=2)
tolFieldSbox2.bind('<Tab>', updateColor)
htmlLabel2 = ttk.Label(rightFrame, text="Hex code: ", state='disabled')
htmlLabel2.grid(row = 4, column = 2, sticky='E')
htmlField2 = ttk.Entry(rightFrame, textvariable=htmlFieldsVars[1], justify='right', width='15', state='disabled')
htmlField2.grid(row = 4, column = 3, columnspan=3, sticky="W")
htmlField2.bind('<Return>', updateColorHtml)

colorLabel3 = ttk.Label(rightFrame, text="Secondary color", state='disabled')
colorLabel3.grid(row = 5, column = 0, padx=2, pady=2, sticky='E')
colorButton3 = tk.Button(rightFrame, background='#000', relief='groove', width='2', command=lambda:chooseColor(2), state='disabled')
colorButton3.grid(row = 5, column = 1)
hueFieldSbox3 = ttk.Spinbox(rightFrame, from_=0, to=360, width=4, textvariable=hueFieldsVars[2], command=updateColor, state='disabled', justify='right')
hueFieldSbox3.grid(row = 5, column = 2, padx=2, pady=2)
hueFieldSbox3.bind('<Tab>', updateColor)
satFieldSbox3 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=satFieldsVars[2], command=updateColor, state='disabled', justify='right')
satFieldSbox3.grid(row = 5, column = 3, padx=2, pady=2)
satFieldSbox3.bind('<Tab>', updateColor)
briFieldSbox3 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=briFieldsVars[2], command=updateColor, state='disabled', justify='right')
briFieldSbox3.grid(row = 5, column = 4, padx=2, pady=2)
briFieldSbox3.bind('<Tab>', updateColor)
tolFieldSbox3 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=tolFieldsVars[2], command=updateColor, state='disabled', justify='right')
tolFieldSbox3.grid(row = 5, column = 5, padx=2, pady=2)
tolFieldSbox3.bind('<Tab>', updateColor)
htmlLabel3 = ttk.Label(rightFrame, text="Hex code: ", state='disabled')
htmlLabel3.grid(row = 6, column = 2, sticky='E')
htmlField3 = ttk.Entry(rightFrame, textvariable=htmlFieldsVars[2], justify='right', width='15', state='disabled')
htmlField3.grid(row = 6, column = 3, columnspan=3, sticky="W")
htmlField3.bind('<Return>', updateColorHtml)

colorLabel4 = ttk.Label(rightFrame, text="Driver hair color", state='disabled')
colorLabel4.grid(row = 7, column = 0, padx=2, pady=2, sticky='E')
colorButton4 = tk.Button(rightFrame, background='#000', relief='groove', width='2', command=lambda:chooseColor(3), state='disabled')
colorButton4.grid(row = 7, column = 1)
hueFieldSbox4 = ttk.Spinbox(rightFrame, from_=0, to=360, width=4, textvariable=hueFieldsVars[3], command=updateColor, state='disabled', justify='right')
hueFieldSbox4.grid(row = 7, column = 2, padx=2, pady=2)
hueFieldSbox4.bind('<Tab>', updateColor)
satFieldSbox4 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=satFieldsVars[3], command=updateColor, state='disabled', justify='right')
satFieldSbox4.grid(row = 7, column = 3, padx=2, pady=2)
satFieldSbox4.bind('<Tab>', updateColor)
briFieldSbox4 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=briFieldsVars[3], command=updateColor, state='disabled', justify='right')
briFieldSbox4.grid(row = 7, column = 4, padx=2, pady=2)
briFieldSbox4.bind('<Tab>', updateColor)
tolFieldSbox4 = ttk.Spinbox(rightFrame, from_=0, to=255, width=4, textvariable=tolFieldsVars[3], command=updateColor, state='disabled', justify='right')
tolFieldSbox4.grid(row = 7, column = 5, padx=2, pady=2)
tolFieldSbox4.bind('<Tab>', updateColor)
htmlLabel4 = ttk.Label(rightFrame, text="Hex code: ", state='disabled')
htmlLabel4.grid(row = 8, column = 2, sticky='E')
htmlField4 = ttk.Entry(rightFrame, textvariable=htmlFieldsVars[3], justify='right', width='15', state='disabled')
htmlField4.grid(row = 8, column = 3, columnspan=3, sticky="W")
htmlField4.bind('<Return>', updateColorHtml)

fileLabel = ttk.Label(bottomFrame, textvariable=fcePathStr, relief='sunken')
fileLabel.grid(row = 0, column = 0, columnspan=2, padx=5, pady=5, sticky='NSWE')
typeLabel = ttk.Label(bottomFrame, textvariable=fceTypeStr, relief='sunken')
typeLabel.grid(row = 0, column = 2, padx=5, pady=5, sticky='NSEW')

## color field validation
reg = rightFrame.register(inputCallback)
regHue = rightFrame.register(inputCallbackHue)
regHtml = rightFrame.register(inputCallbackHtml)
hueFieldSbox1.config(validate="key", validatecommand=(regHue, '%P'))
satFieldSbox1.config(validate="key", validatecommand=(reg, '%P'))
briFieldSbox1.config(validate="key", validatecommand=(reg, '%P'))
tolFieldSbox1.config(validate="key", validatecommand=(reg, '%P'))
htmlField1.config(validate="key", validatecommand=(regHtml, '%P', '%S'))

hueFieldSbox2.config(validate="key", validatecommand=(regHue, '%P'))
satFieldSbox2.config(validate="key", validatecommand=(reg, '%P'))
briFieldSbox2.config(validate="key", validatecommand=(reg, '%P'))
tolFieldSbox2.config(validate="key", validatecommand=(reg, '%P'))
htmlField2.config(validate="key", validatecommand=(regHtml, '%P', '%S'))

hueFieldSbox3.config(validate="key", validatecommand=(regHue, '%P'))
satFieldSbox3.config(validate="key", validatecommand=(reg, '%P'))
briFieldSbox3.config(validate="key", validatecommand=(reg, '%P'))
tolFieldSbox3.config(validate="key", validatecommand=(reg, '%P'))
htmlField3.config(validate="key", validatecommand=(regHtml, '%P', '%S'))

hueFieldSbox4.config(validate="key", validatecommand=(regHue, '%P'))
satFieldSbox4.config(validate="key", validatecommand=(reg, '%P'))
briFieldSbox4.config(validate="key", validatecommand=(reg, '%P'))
tolFieldSbox4.config(validate="key", validatecommand=(reg, '%P'))
htmlField4.config(validate="key", validatecommand=(regHtml, '%P', '%S'))

root.mainloop()
