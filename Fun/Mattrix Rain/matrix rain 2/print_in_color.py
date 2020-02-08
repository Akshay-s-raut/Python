import random
#print("\033[96m {}\033[00m" .format("Hey"))
#print("\033[44;32mAkshay")
#print("\033[0mHey")

'''def print_in_color(color,text,rand=False):
    colors = {"black":"30","red":"31","green":"32","yellow":"33","blue":"34","magenta":"35","cyan":"36","white":"37"}
    if(rand==False):
        str = "\033["+colors[color]+"m"+text+"\033[0m"
    else:
        x,y = random.choice(list(colors.items()))
        str = "\033["+y+"m"+text+"\033[0m"
    print(str)'''
def print_in_color(color,text):
    color = color.lower()
    colors = {"black":"30","red":"31","green":"32","yellow":"33","blue":"34","magenta":"35","cyan":"36","white":"37"}
    str = "\033["+colors[color]+"m"+text+"\033[0m"
    print(str)

print_in_color("blue","Akshay")
