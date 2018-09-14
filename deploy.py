#!/usr/bin/env python
import subprocess as sp
import re
import shlex
import time
import sys

folderPath = '/home/ijash/Documents/Projects/nodejs/express-demo'
fileName =  '/index.js'
windowName = fileName.replace('/',"")

def call (arg):
    # make the command one liner
    sp.check_call(shlex.split(arg))

def getOutput(arg):
    return sp.Popen(arg,stdout=sp.PIPE)

# get the Window ID
def captureWindowID(searchName):
    if (sys.version_info > (3, 0)):
        # Python 3 code in this block: Python 3 made the default strings unicode and a process outputs bytes
        output = sp.check_output('xdotool search \"'+ searchName +'\" | head -1',shell=True)
        output = "".join(map(chr,output))
        idString = re.findall(r'(\b[0-9]+)',output)
        return idString[0]
    else:
        # Python 2 code in this block
        output = sp.check_output('xdotool search \"'+ searchName +'\" | head -1',shell=True)
        idString = re.findall(r'(\b[0-9]+)',output)
        return idString[0]

def openVSCode(filePath, folderPath):
    sp.call(['code','-n','--verbose',filePath,folderPath], shell=False)

def loadWindow(windowName):
    i=0
    sec = 0.0
    #check window is opened
    if (sys.version_info > (3, 0)):
        #loading animation
        while (sp.check_output('wmctrl -l | grep \"'+windowName+'\" 2>&1 | wc -l',shell=True) == b'0\n'):   
            i=i+1
            sys.stdout.write("\r{0}>".format("="*i))
            sys.stdout.flush()
            time.sleep(0.1)
            sec = sec + 0.1
    else:
        #loading animation
        while (sp.check_output('wmctrl -l | grep \"'+windowName+'\" 2>&1 | wc -l',shell=True) == b'0\n'):
            i=i+1
            sys.stdout.write("\r{0}>".format("="*i))
            sys.stdout.flush()
            time.sleep(0.1)
            sec = sec + 0.1
    print('\nwindow "'+windowName+'" loaded in '+ str(sec) +' seconds')


#launch VS Code
openVSCode((folderPath+fileName),folderPath)
#check window is opened
loadWindow(windowName)
winID = captureWindowID(windowName)
call('xdotool windowfocus '+winID)
hexWinID = hex(int(winID))
call('wmctrl -ir '+hexWinID+' -b remove,maximized_vert,maximized_horz')
call('xdotool getactivewindow windowmove 0 800')
call('xdotool windowfocus '+winID)
call('xdotool windowsize  '+winID+' 1009 1050 ')

#launch browser 1
call('chromium-browser')
windowName = 'New Tab'
loadWindow(windowName)
winID = captureWindowID(windowName)
call('xdotool windowfocus '+winID)
hexWinID = hex(int(winID))
call('wmctrl -ir '+hexWinID+' -b remove,maximized_vert,maximized_horz')
# call('xdotool key super+Down super+Down')
call('xdotool windowfocus '+winID)
call('xdotool windowsize --sync '+winID+' 911 735 ')
call('xdotool getactivewindow windowmove 1009 736')
call('xdotool type --delay 5 "localhost:3000"')
call('xdotool key Return')

#launch terminal
call('gnome-terminal')
windowName = ': ~/'
loadWindow(windowName)
winID = captureWindowID(windowName)
call('xdotool windowfocus '+winID)
call('xdotool windowsize --sync '+winID+' 911 265 ')
call('xdotool getactivewindow windowmove 1009 1583')
call('xdotool type --delay 5 "cd '+ folderPath+'" && clear')
call('xdotool key Return')
call('xdotool type --delay 5 "nodemon '+fileName.replace('/',"")+'"')
call('xdotool key Return')
#launch browser 2
call('chromium-browser')
windowName = 'New Tab'
loadWindow(windowName)
winID = captureWindowID(windowName)
call('xdotool windowfocus '+winID)
hexWinID = hex(int(winID))
# call('xdotool key super+Down super+Down')
call('xdotool windowfocus '+winID)
call('xdotool windowsize --sync '+winID+' 911 500 ')
call('xdotool getactivewindow windowmove 33 33')
call('wmctrl -ir '+hexWinID+' -b add,maximized_vert,maximized_horz')
call('xdotool type --delay 5 "https://nodejs.org/dist/latest-v8.x/docs/api/"')
call('xdotool key Return ctrl+t')
call('xdotool type --delay 5 "https://www.w3schools.com/nodejs/default.asp"')
call('xdotool key Return')
