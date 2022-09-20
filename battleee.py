from game2dboard import *
from random import *
import time
import random
import heapq


#Implementation

#Stacks:
#When the player misses their shot, it stacks that slot (For example, if A5 is water, it takes it out of the game.
#(we cant shoot that same slot again) and stacks it)

#Queues:
#Every time the player clicks on a square, it gets queued and at the end of the game shows the path
#(every square hit by the player). Let's say the player wins the game after 47 tries, the output then shows
#every single attempt the player made.

#Library:
#Converts letters to numbers (For easier user input and understanding). Instead of writing [1,1],
#the user will give [A,1] as an input which is transformed into the matrix format with numbers.

#Heaps:
#Place ships for both players and computer as well as getting the randomness of the computer choices

LETTERS_NUMBERS = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10}
listercs=[1,2,3,4,5,6,7,8,9,10]
listeccs=[13,14,15,16,17,18,19,20,21,22,23]
listerps=[1,2,3,4,5,6,7,8,9,10]
listecps=[1,2,3,4,5,6,7,8,9,10]

b = Board(11, 24)


for i in range(1,11):# 3 rows, 4 columns, filled w/ None
    b[i][0] = i
for i in range(1,11):
    liste = ['' ,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    b[0][i]=liste[i]

for i in range(1,11):# 3 rows, 4 columns, filled w/ None
    b[i][13] = i
for i in range(1,11):
    listen = ['' ,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    b[0][i+13]= listen[i]

for x in range(11,13):
    for y in range(0,11):
        b[y][x]= "C:/Users/34629/PycharmProjects/battleship/img/middle.png"

board= [[0 for _ in range(24)]  for _ in range(11)]
#do 3 for columns
# the cols fill everything which means 11 columns by each side
# the rows fill just 10 and not 11 because there is a three already filled by the columns

for i in range(11):# 3 left top
    board[0][i]=3
for i in range(13,24):#3 right top
    board[0][i]=3
#do 3 for rows
for i in range(1,11):#3left column
    board[i][0]=3
for i in range(0,11):#3 in the middle
    board[i][11]=3
for i in range(0,11):#3 in the middle
    board[i][12]=3
for i in range(1,11):
    board[i][13]=3  #3 in the right column

list_5holes=[]
list_4holes=[]
list_3holes=[]
list_2holes=[]
liste=[list_5holes,list_4holes,list_3holes,list_2holes]
direction = ["vertical", "horizontal"]
checkliste=[]
# set boats of the computer part randomly
#set 5th boat randomly: it should be in 1 column and 5 rows ////  or 1 row and 5 columns:
ydist=18
xdist=5
length=5
for i in range(4):
    ydist+=1
    xdist+=1
    length-=1
    j = randrange(14, 24)
    print(j)
    k = randrange(1, 11)
    print(k)
    ch = choice(direction)
    print(ch)
    print("-----")
    if ch=="horizontal":
        while j>ydist or ([k,j] in checkliste) or ([k+length,j] in checkliste): # O((n)log(n)) two nested loops
            print("not pass")
            j = randrange(14, 24)
            print(j)
            k = randrange(1, 11)
            print(k)
            print("__")
        board[k][j] = 1
        liste[i].append([k, j]) # O(1)
        checkliste.append([k,j]) # O(1)
        for z in range(length): # O(n) where n is the length
            j+=1
            board[k][j]= 1
            liste[i].append([k,j]) # O(1)
            checkliste.append([k, j]) # O(1)
        print(liste[i])
    else:
        while k>xdist or ([k,j]  in checkliste) or ([k,j+length] in checkliste) : # O((n)log(n)) two nested loops
            j = randrange(14, 24)
            print(j)
            k = randrange(1, 11)
            print(k)
            print("---------")
        board[k][j] = 1
        liste[i].append([k, j]) # O(1)
        checkliste.append([k,j]) # O(1)
        for z in range(length): # O(n) where n is the length
            k+=1
            board[k][j]= 1
            liste[i].append([k,j]) # O(1)
            checkliste.append([k, j]) # O(1)
        print(liste[i])

list_5holesp=[]
list_4holesp=[]
list_3holesp=[]
list_2holesp=[]
listep=[list_5holesp,list_4holesp,list_3holesp,list_2holesp]
directionp = ["vertical", "horizontal"]
checklistep=[]
#set 5th boat randomly: it should be in 1 column and 5 rows ////  or 1 row and 5 columns:
ydist = 4
xdist = 4
length = 5
for i in range(4):
    choicep = input(
        "Enter (vertical) or (horizontal) for the direction you want to place this first boat with {} holes:".format(
            length))
    while choicep != "vertical" and choicep != "horizontal":
        choicep = input(
            "Re-enter (vertical) or (horizontal) for the direction you want to place this first boat with {} holes:".format(
                length))
    ydist += 1
    xdist += 1
    length -= 1
    k = int(input("Enter the row you would like to place the boat "))
    j = input("Enter the column you would like to place the boat ")
    j=j.upper()
    if j in 'ABCDEFGHIJ':
        j = LETTERS_NUMBERS[j]
    if choicep == "horizontal":
        while j > ydist or ([k, j] in checklistep) or ([k+length,j] in checklistep):
            k = int(input("Re-enter the row you would like to place the boat "))
            j = input("Re-enter the column you would like to place the boat ")
            j=j.upper()
            if j in 'ABCDEFGHIJ':
                j = LETTERS_NUMBERS[j]
        board[k][j] = 1
        listep[i].append([k, j]) # O(1)
        checklistep.append([k, j]) # O(1)
        for z in range(length): # O(n) where n is the length
            j += 1
            board[k][j] = 1
            listep[i].append([k, j]) # O(1)
            checklistep.append([k, j]) # O(1)
        print(listep[i])
    elif choicep == "vertical":
        while k > xdist or ([k, j] in checklistep) or ([k,j+length] in checklistep):
            k = int(input("Re-enter  the row you would like to place the boat "))
            j = input("Re-enter the column you would like to place the boat ")
            j=j.upper()
            if j in 'ABCDEFGHIJ':
                j = LETTERS_NUMBERS[j]
            print("---------")
        board[k][j] = 1
        listep[i].append([k, j]) # O(1)
        checklistep.append([k, j]) # O(1)
        for z in range(length): # O(n) where n is the length
            k += 1
            board[k][j] = 1
            listep[i].append([k, j]) # O(1)
            checklistep.append([k, j]) # O(1)
        print(listep[i])


H=[]
#O(N^2)
for i in range(10):
    for j in range(10):
        H.append([i+1,j+1])

heapq.heapify(H)
def computer_playing(stack,queuecomputer,H,countsteps ):
    countsteps+=1
    track=0
    print("this is stack at initiation:",stack)
    print("length of stack",len(stack))
    p=True
    while p:
        if len(stack)==0:
            k = random.randrange(0, len(H))
            [row,col]=H[k]
            H[k], H[0] = H[0], H[k]
            heapq.heappop(H) # O(1) Since it is at the beginning of the array
            queuecomputer.append([row,col])  # O(1) Pushing an element in the stack
        else:
            guess=stack.pop() # O(1)
            row=guess[0]
            col=guess[1]
            queuecomputer.append([row,col]) # O(1) Pushing an element in the stack


        if board[row][col]==1 and len(stack)==4:
            if b[row][col] == "gris":
                b[row][col] = "gris"
                while len(stack) > 0:  # O(n) where n is the number of elements inside the stack
                    stack.pop() # O(1)
                print("stack emptied because touched grey")
            b[row][col]="azull"
            while board[row][col]==1 and col!=0 and row!=0:
            # Average: O(log(n)) where n is a possible piece of a ship
            # Worst: O(n) where n is all the piece of the hit ship
                track+=1
                print("here for col +1")
                col+=1
                a=H.index([row,col])
                H[a], H[0] = H[0], H[a]
                heapq.heappop(H) # O(1) Since it is at the beginning of the array
                b[row][col]="azull"
                queuecomputer.append([row,col]) # O(1) Pushing an element in the stack
            print("done with this process and we did", track)
            if b[row][col] != 1:
                print("length of track", track)
                print("stack:",stack)
                print("lenstack",len(stack))
                print(track)
                print("col",col)
                print("row",row)
                print("heeeeeeeeeeeey")
                stack.append([row, col-track-2]) # O(1) Pushing an element in the stack


        if board[row][col]==1 and len(stack)==3:
            if b[row][col] == "gris":
                b[row][col] = "gris"
                while len(stack) > 0: # O(n) where n is the number of elements inside the stack
                    stack.pop() # O(1)
                print("stack emptied because touched grey")
            b[row][col]="azull"
            while board[row][col]==1 and col!=0 and row!=0:
            # Average: O(log(n)) where n is a possible piece of a ship
            # Worst: O(n) where n is all the piece of the hit ship
                track+=1
                print("here for col -1")
                col-=1
                a=H.index([row,col])
                H[a], H[0] = H[0], H[a]
                heapq.heappop(H) # O(1) Since it is at the beginning of the array
                b[row][col]="azull"
                queuecomputer.append([row, col]) # O(1) Pushing an element in the stack
            print("done with this process and we did", track)
            if b[row][col] != 1:
                print("stack:",stack)
                print("lenstack",len(stack))
                print(track)
                print("col",col)
                print("row",row)
                stack.append([row , col+track+2]) # O(1) Pushing an element in the stack

        if board[row][col]==1 and len(stack)==2:
            if b[row][col] == "gris":
                b[row][col] = "gris"
                while len(stack) > 0: # O(n) where n is the number of elements inside the stack
                    stack.pop() # O(1)
                print("stack emptied because touched grey")
            b[row][col]="azull"
            while board[row][col]==1 and col!=0 and row!=0:
            # Average: O(log(n)) where n is a possible piece of a ship
            # Worst: O(n) where n is all the piece of the hit ship
                print("here for row +1")
                row+=1
                a=H.index([row,col])
                H[a], H[0] = H[0], H[a]
                heapq.heappop(H) # O(1) Since it is at the beginning of the array
                track+=1
                b[row][col]="azull"
                queuecomputer.append([row, col]) # O(1) queue element
            print("done with this process and we did", track)
            if b[row][col] != 1:
                print("stack:",stack)
                print("lenstack",len(stack))
                print("track",track)
                print("col",col)
                print("row",row)
                stack.append([row-track-2, col]) # O(1) Pushing an element in the stack

        if board[row][col]==1 and len(stack)==1:
            if b[row][col] == "gris":
                b[row][col] = "gris"
                while len(stack) > 0: # O(n) where n is the number of elements inside the stack
                    stack.pop() # O(1)
                print("stack emptied because touched grey")
            b[row][col]="azull"
            while board[row][col]==1  and col!=0 and row!=0:
            #Average: O(log(n)) where n is a possible piece of a ship
            #Worst: O(n) where n is all the piece of the hit ship
                track+=1
                a=H.index([row,col])
                H[a], H[0] = H[0], H[a]
                heapq.heappop(H) # O(1) Since it is at the beginning of the array
                print("here for row -1")
                row-=1
                b[row][col]="azull"
                queuecomputer.append([row, col]) # O(1) queue element
            print("done with this process and we did", track)
            if b[row][col] != 1:
                print("stack:",stack)
                print("lenstack",len(stack))
                print(track)
                print("col",col)
                print("row",row)
                print("heeeeeeeey")
                stack.append([row + track + 2 , col]) # O(1) Pushing an element in the stack


        if board[row][col]==1 and len(stack)==0 and col!=0:
            if b[row][col] == "gris":
                b[row][col] = "gris"
                while len(stack) > 0: # O(n) where n is the number of elements inside the stack
                    stack.pop() # O(1)
                print("stack emptied because touched grey")
                p=True
            else:
                b[row][col]="azull"
                print("here we go to create a new stack")
                z=randrange(1,len(H))
                row1,col1=H[z]
                stack.append([row1,col1]) # O(1) Pushing an element in the stack
                a = H.index([row1, col1])
                H[a], H[0] = H[0], H[a]
                heapq.heappop(H) # O(1) Since it is at the beginning of the array
                if row==1:
                    z = randrange(1, len(H))
                    row1, col1 = H[z]
                    stack.append([row1, col1]) # O(1) Pushing an element in the stack
                    a = H.index([row1, col1])
                    H[a], H[0] = H[0], H[a]
                    heapq.heappop(H) # O(1) ""
                if row==10:
                    z = randrange(1, len(H))
                    row1, col1 = H[z]
                    stack.append([row1, col1]) # O(1) Pushing an element in the stack
                    a = H.index([row1, col1])
                    H[a], H[0] = H[0], H[a]
                    heapq.heappop(H) # O(1) ""
                if col==1:
                    z = randrange(1, len(H))
                    row1, col1 = H[z]
                    stack.append([row1, col1]) # O(1) Pushing an element in the stack
                    a = H.index([row1, col1])
                    H[a], H[0] = H[0], H[a]
                    heapq.heappop(H) # O(1) ""
                if col==10:
                    z = randrange(1, len(H))
                    row1, col1 = H[z]
                    stack.append([row1, col1]) # O(1) Pushing an element in the stack
                    a = H.index([row1, col1])
                    H[a], H[0] = H[0], H[a]
                    heapq.heappop(H) # O(1) ""
                if row!=1:
                    stack.append([row-1,col]) # O(1) Pushing an element in the stack
                    a = H.index([row-1, col])
                    H[a], H[0] = H[0], H[a]
                    heapq.heappop(H) # O(1) ""
                if row!=10:
                    stack.append([row+1, col]) # O(1) Pushing an element in the stack
                    a = H.index([row+1, col])
                    H[a], H[0] = H[0], H[a]
                    heapq.heappop(H) # O(1) ""
                if col!=1:
                    stack.append([row, col-1]) # O(1) Pushing an element in the stack
                    a = H.index([row, col-1])
                    H[a], H[0] = H[0], H[a]
                    heapq.heappop(H) # O(1) ""
                if col!=10:
                    stack.append([row, col+1]) # O(1) Pushing an element in the stack
                    a = H.index([row, col+1])
                    H[a], H[0] = H[0], H[a]
                    heapq.heappop(H) # O(1) ""


        elif board[row][col]== 0:
            b[row][col]= "cross"
            a = H.index([row, col])
            H[a], H[0] = H[0], H[a]
            heapq.heappop(H) # O(1)
            b.pause(2000)
            p=False

        b.pause(1000)

def prove_5hole(): #O(n) where n is the number of holes
    count=0
    for a, qq in list_5holes:

        if b[a][qq] == "azull" or b[a][qq] == "gris":
            count += 1

        else:
            return False
    if count > 4:
        return True

def prove_4hole(): #O(n) where n is the number of holes
    count=0
    for a, qq in list_4holes:
        if b[a][qq] == "azull" or b[a][qq] == "gris" :
            count += 1

        else:
            return False
    if count > 3:
        return True

def prove_3hole(): #O(n) where n is the number of holes
    count=0
    for a, qq in list_3holes:
        if b[a][qq] == "azull" or b[a][qq] == "gris" :
            count += 1

        else:
            return False
    if count > 2:
        return True

def prove_2hole(): #O(n) where n is the number of holes
    count=0
    for a, qq in list_2holes:
        if b[a][qq] == "azull" or b[a][qq] == "gris" :
            count += 1

        else:
            return False
    if count > 1:
        return True

def prove_5holep(): #O(n) where n is the number of holes
    count=0
    for a, qq in list_5holesp:

        if b[a][qq] == "azull" or b[a][qq] == "gris":
            count += 1

        else:
            return False
    if count > 4:
        return True

def prove_4holep(): #O(n) where n is the number of holes
    count=0
    for a, qq in list_4holesp:
        if b[a][qq] == "azull" or b[a][qq] == "gris" :
            count += 1

        else:
            return False
    if count > 3:
        return True

def prove_3holep(): #O(n) where n is the number of holes
    count=0
    for a, qq in list_3holesp:
        if b[a][qq] == "azull" or b[a][qq] == "gris" :
            count += 1

        else:
            return False
    if count > 2:
        return True

def prove_2holep(): #O(n) where n is the number of holes
    count=0
    for a, qq in list_2holesp:
        if b[a][qq] == "azull" or b[a][qq] == "gris" :
            count += 1

        else:
            return False
    if count > 1:
        return True

def sink(list): #O(n) where n is the number of sunk spaces
    for a, qq in list:
        b[a][qq] = "gris"

def printpath(queue):
    while len(queue)>0:
        print(queue.pop(0))
stack=[]
queueplayer=[]
queuecomputer=[]
countsteps=0
def mouse_fn1(btn,row, col):
    queueplayer.append([row,col])
    sunkenp=0
    sunkenc=0
    count=-1
    # mouse callback function
    if board[row][col]==1:
        if row in listercs and col in listeccs:
            if b[row][col] == "gris":
                b[row][col] = "gris"
                count += 1
                b.pause(2000)

            else:
                b[row][col]="azull"
                count += 1
                b.pause(2000)


    elif board[row][col]== 0:
        if row in listercs and col in listeccs:
            b[row][col]= "cross"
            b.pause(2000)
            computer_playing(stack,queuecomputer,H,countsteps)

    if prove_5hole():
        sunkenc+=1
        sink(list_5holes)
    if prove_4hole():
        sunkenc += 1
        sink(list_4holes)
    if prove_3hole():
        sunkenc += 1
        sink(list_3holes)

    if prove_2hole():
        sunkenc += 1
        sink(list_2holes)

    if sunkenc==4:
        b.close()
        print("You won!")
        print("This is the amount of steps you needed to win:", len(queueplayer))
        print("This is the path you followed from the beggining to reach the computer:")
        printpath(queueplayer)


    if prove_5holep():
        sunkenp+=1
        sink(list_5holesp)
    if prove_4holep():
        sunkenp += 1
        sink(list_4holesp)
    if prove_3holep():
        sunkenp += 1
        sink(list_3holesp)

    if prove_2holep():
        sunkenp+= 1
        sink(list_2holesp)

    if sunkenp==4:
        b.close()
        print("The computer won!")
        print("This is the path the computer followed from the beggining to reach you:")
        printpath(queuecomputer)


b.grid_color = "blue"
b.title = "Click me!"
b.cell_size = 50
b.cell_color = "white"
b.on_mouse_click = mouse_fn1
b.show()