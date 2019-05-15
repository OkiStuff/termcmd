# Main UI
import os
import sys
from scripts import say
input0 = 0
code = input(">>")

def say_syntax():
	if code == 'say()':
		say()

sys.path.insert(0, '/scripts/')

def mainloop_loop():
	mainloop()

def mainloop():
	code = input(">>")
	command(0)
	say()
	mainloop_loop()
def command(input0):
	if input0 == 0:
		input0 = code

command(0)
mainloop()
