import time

def pausa(t = 2): 
    if(t == 0): input('Press ENTER to continue ')
    else: time.sleep(t)

def menu(title, items): return int(input(f'{title}\n{items}'))     
