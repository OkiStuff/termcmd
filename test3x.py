
import sys

testname = input("Enter the number 2 in here")

if testname == 2:
	print("Test 1 complete!")
else:
	print("Test 1 complete with major warnings. We will now send you back.")
	pause = input("Press Enter to restart")
	sys.system('python main.py')
