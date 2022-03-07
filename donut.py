import os
from math import sin, cos

def main():
    a=0
    b=0

    height=24
    width=80
    #height=int(input("Enter Screen Height : "))
    #width=int(input("Enter Screen Width : "))
    
	# for clearing console (windows and unix systems)
    clear = "cls"
    if os.name == "posix":
        clear = "clear"

    os.system(clear)
    while True:
        z = [0 for _ in range(4*height*width)]
        screen = [' ' for _ in range(height*width)]

        j=0
        
    
	
