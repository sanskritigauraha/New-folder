from pickle import TRUE
import random
from re import S

def gamewin(comp, you):
    if comp == you:
        return None
    
    elif comp == 'S':
        if you == 'p':
            return TRUE
        elif you == 'sc':
            return False
    
    elif comp == 'p':
        if you == 'sc':
            return True
        elif you == 's':
            return False
        
    elif comp == 'sc':
        if you == 's':
            return True
        elif you == 'p':
            return False

print ("comp turn : stone(s), paper(p), sciccors (sc)?")
randno = random.randint(1,3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 'sc'

you = input("your turn : stone(s), paper(p), sciccors (sc)")
a =  gamewin(comp , you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print ("it is a tie")
elif a:
    print ("you won")
else:
    print("you lost")