x = True
y = True

def logic():
    global x
    global y
    if x == True and y == True:
        x = False
        y = False
    elif x == True and y == False:
        x = False
        y = True
    elif x == False and y == True:
        x = True
        y = True
    elif x == False and y == False:
        x = True
        y = False