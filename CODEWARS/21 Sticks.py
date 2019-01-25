#Time: 648ms Passed: 16 Failed: 0 Exit Code: 1

def makeMove(sticks):
    if sticks > 4:
        return random.randrange(1,3)
    elif sticks == 3:
        return 3
    elif sticks == 2:
        return 2
    elif sticks == 1:
        return 1

    
    # Varient 2
    
def makeMove(sticks):
    if sticks % 4 == 0:
        return 1 
    else:
        return sticks % 4
