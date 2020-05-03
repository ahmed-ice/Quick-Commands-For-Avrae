from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pyperclip

window = Tk()
window.title("Avrae text input")
window.geometry('290x350')
window.lift()

# Frame created outside all functions
# so it can be accessed inside all
frame = Frame(window)


#String master join all strings
currentstring = []
def copystring():
    cstring = (' '.join(currentstring))
    v.set(cstring + '\n-line copied-') #set text variable
    pyperclip.copy(cstring)

#Show string master at bottom
v = StringVar()
copiedtext = Label(window, textvariable=v, justify=CENTER, font=("Helvetica", 8))
copiedtext.grid(column=0, row=15, padx=10, columnspan=4)

empty = Label(window, text='GO!')
empty.grid(column=1, row=0, padx=10)


#Open files
def error():
    messagebox.showinfo('Setting up!', '''Seems like some files are missing,
Please refer to newly created readme file, and run again!''') #shows info

try:
    att = open('attacks.txt','r')
    skl = open('skills.txt','r')
    spl = open('spells.txt','r')
except:
    att = open('attacks.txt','w')
    skl = open('skills.txt','w')
    spl = open('spells.txt','w')
    readme = open('readme.txt','w')
    readme.write('''Write down your attacks/skills/spells in their respective files.
Write each command on a new line.
Each new line will create a new button.
If you are running from a python IDE, you might need to close the IDE.
''')
    readme.close()
    error()
    window.destroy


#Create empty lists
weapons = []
skills = []
spells = []

#strip and write the words to the lists
for word in att.readlines():
    weapons.append(word.strip())
for word in skl.readlines():
    skills.append(word.strip())
for word in spl.readlines():
    spells.append(word.strip())

#clear whole string
def cleanstring():
    currentstring.clear()

#function of the button
def buttonfunction(name):
    if name not in currentstring:
        currentstring.append(name)
        copystring()

def createbutton(name,position):
    crt = Button(frame, text=name[:7] , command= lambda: buttonfunction(name))
    crt.grid(column=0, row=position)

##############################
def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()
    frame.grid_forget()

def dropdown(name, col):
    clear_frame()
    currentstring.clear()
    add_command(name)
    
    pos = main_commands.index(name)
    items = subcommands[pos]
        
    for i in range(len(items)):
        create_subcommand_button(items[i],i)
    
    frame.grid(column=col,row=2)

def create_main_btn(text, col):
    btn = Button(window, text=text, command=lambda: dropdown(text,col))
    btn.grid(column=col, row=1, padx=10)
    
for i in range(len(main_commands)):
    create_main_btn(main_commands[i],i)
#window loop
window.mainloop()
