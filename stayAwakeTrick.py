import os
import pyautogui as m
import random as rand
import time
import keyboard

m.FAILSAFE = False

t0 = time.time()

os.system("clear")

while(1):
	if keyboard.is_pressed("esc"):
		print("Loop Stoped")
		break
	r = rand.randrange(0, 900)
	m.moveTo(r, r)
	time.sleep(1)
	print(r, r, " Mouse coordinates. Long Press ESC for exit.")
	t1 = time.time()
	print("total TIme: ", t1-t0)

