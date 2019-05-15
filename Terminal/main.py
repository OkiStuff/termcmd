# Main UI
import os 
input0 = 0
code = input(">>")

def mainloop_loop():
	mainloop()

def mainloop():
	code = input(">>")
	command(0)
	mainloop_loop()
def command(input0):
	if input0 == 0:
		input0 = code

command(0)
mainloop()
