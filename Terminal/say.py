# say command for termcmd
import os 
import sys 
import main
saycmd = 0
def say(code, saycmd):
	if code > 0:
		if saycmd > 0:
			if code == 'say()':
				saycmd = input("say>>")
			elif code == 'SAY()':
				saycmd = input("say>>")
			else:
				print("Wrong Syntax. Error Code 0")
	return;
say(1, 1)