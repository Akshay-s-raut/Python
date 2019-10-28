import time

dot = 0.3
dash = dot*3
space = dot*5

print("Text to Morse code converter")
code= {'a': '._', 'b':'_...' , 'c':'_._.', 'd':'_..', 'e':'.' , 'f':'.._.' , 'g':'__.' , 'h':'....' , 'i':'..' , 'j':'.___' ,
        'k':'_._', 'l':'._..' , 'm':'__' , 'n':'_.' , 'o':'___' , 'p':'.__.' , 'q':'__._' , 'r':'._.' , 's':'...' ,
        't':'_' , 'u':'.._' , 'v':'..._' , 'w':'.__' , 'x':'_.._' , 'y':'_.__' , 'z':'__..',
        '0':'_____' , '1':'.____' , '2':'..___' , '3':'...__' , '4':'...._' , '5':'.....' , '6':'_....' , '7':'__...', '8':'___..' , '9':'____.'
        }

text = input("Enter text: ")

def converter(text):
    text = text.lower()
    morse_sentence = []
    for i in text.split():
        temp = []
        for j in i:
            temp.append(code[j])
        morse_sentence.append(temp)
    return morse_sentence

def presenter(text):
    morse_text = converter(text)
    for i in morse_text:
        for j in i:
            for k in j:
                print("\033[F\33[2K{}".format('tap'))
                if(k=='.'):
                    time.sleep(dot)
                if(k=='_'):
                    time.sleep(dash)
                print("\033[F\33[2K")
                time.sleep(dot)
            time.sleep(dash)
        time.sleep(space)
print()
presenter(text)
