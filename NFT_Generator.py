from tkinter import *
import random
gui = Tk(className='NFT Generator')
# set window size
gui.geometry("506x508")

c = random.randint(100000000,999999999)
cc = random.randint(100000000,999999999)
cccc = random.randint(100000000,999999999)
for i in range (23):
    ccc = random.randint(1,3)
    for j in range(21):
        ccc = random.randint(1,3)
        if(ccc == 1):
            color = "#" + str(c)
        elif(ccc == 2):
            color = "#" + str(cc)
        else:
            color = "#" + str(cccc)
        example1 = Label(text="     ")
        example1.grid(row=i, column=j)
        example1.configure(bg = color)
    
#set window color
gui.mainloop()
