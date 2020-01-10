from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.key_binding import KeyBindings
from pygments.lexers.python import Python3Lexer
from prompt_toolkit.lexers import PygmentsLexer
import os
import time
import sys
from prompt_toolkit.shortcuts import button_dialog
from prompt_toolkit.shortcuts import input_dialog,message_dialog
from prompt_toolkit import print_formatted_text as printf

command_line=True

break_dance=''

def clear(): # from https://repl.it/talk/share/pyIDE/24797?order=new (examples/clrScrnEx.py)
	if os.name == 'nt':
		os.system("cls")
	else:
		os.system("clear")

clear()

print(os.getcwd())

if command_line:
  filename=sys.argv[1]
else:
  printf(HTML('<pink><b>Choose a filename/filepath to create/edit</b></pink>'))
  filename=input('')
  if filename.startswith('/'):
    filename=os.getcwd()+filename
  else:
    filaname=os.getcwd()+'/'+filename

clear()

quit_it=False

current=''

if os.path.isfile(filename):
  fp=open(filename)
  current=fp.read()
  fp.close()


def saveas():
  global filename,current
  filename=input_dialog(title="choose a filepath & name:",text='')
  save(current,filename)

def save(contents,filepath):
  try:
    fp=open(filepath,'w')
    fp.write(contents)
    fp.close()
  except FileNotFoundError:
    message_dialog(title='ERROR',text='Could not write to file:\n'+os.getcwd()+filename)
    break_dance=True

def menu():
  return button_dialog(
    title='Menu',
    text='',
    buttons=[
        ('Close Menu', False),
        ('Save', 1),
        ("Save As",3),
        ('Quit',2)
    ],
  )

binds=KeyBindings()

@binds.add('c-x')
def _(event):
    quit_it=True
    event.app.exit()
    #sys.exit()


@binds.add('c-s')
def _(event):
  pass

def bottom_toolbar():
    return HTML(' Menu: <b><style bg="ansired">ESC then ENTER</style></b>')

#current=''

while True:
  try:
    current = prompt(
      '', 
      bottom_toolbar=bottom_toolbar,
      multiline=True,
      key_bindings=binds,
      mouse_support=True,
      '''lexer=PygmentsLexer(Python3Lexer),''' # uncomment out for py syntax highlighting
      default=current,
    )
  except AssertionError:
    pass

  menu_result=menu()
  break_dance=False
  if menu_result==2:
    break_dance=True
  elif menu_result==1:
    save(current,filename)
  elif menu_result==3:
    saveas()

  if break_dance:
    break

  clear()

clear()
