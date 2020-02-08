import random
f = open(r"D:\Programs\Python programs\Fun\matrix rain 2\unicode_characters.txt",encoding='UTF-8').read()
f = f.split()

def getrandomUnicode():
    return random.choice(f)

def print_in_color(color,text):
    color = color.lower()
    colors = {"black":"30","red":"31","green":"32","yellow":"33","blue":"34","magenta":"35","cyan":"36","white":"37"}
    str = "\033["+colors[color]+"m"+text+"\033[0m"
    print(str)

print_in_color("green",getrandomUnicode())
