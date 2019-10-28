import time
'''for i in range(0,10):
    print('\033[F{}'.format('.'*i))
    time.sleep(1)'''

def loading_screen(t,a=['.','..','...'],slp=1):
    for i in range(0,t):
        for j in a:
            print("\033[F\33[2K{}".format(j))
            time.sleep(slp)

loading_screen(10,['.','..','...'],0.5)

#['A','AK','AKS','AKSH','AKSHA','AKSHAY']
#['|','/','_','\\']
#['.','..','...']
