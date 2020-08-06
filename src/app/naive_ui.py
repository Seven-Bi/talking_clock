import time
from .talking import num_to_word


count = 60

def run():
	global count
	while 1:
		t = time.strftime('%H:%M:%S')
		print('> ' + num_to_word(t))

		time.sleep(1)
		count -= 1
		if count <= 0:
			break


def start():
	print('''
	   ==========================================================
	                    Naive UI ver 0.1
	                    
	   There below is about to telling the time in English words
	   according to your current system time.

	   ===========================================================

		''')
	input('Hit the Enter key to start ...')
	run()