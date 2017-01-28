import pyautogui
import time
def counter():
    count = 0
    while count < input:
        count += 1
        time.sleep(1)
        print ("#",count)
    if count == input:
        pyautogui.click(button='right')
        print("Right click!")

run = 0
while run == 0:
    print("Enter the amount of seconds you want to wait until a right click.")
    try:
        input = int(input())
        run = 1
    except:
        print("Your input is not valid. Only numbers with no decimals are valid.")
repeat = 0
while run == 1:
    repeat += 1
    print("Loop:",repeat)
    counter()
	