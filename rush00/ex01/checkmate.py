notKing = ["P","Q","B","R"]
withKing =["P","B","R","Q","K"]

def pawn(pawnPos:tuple,boardList:list):
    inCheck = False
    pawnLeftPos = (pawnPos[0]-1,pawnPos[1]-1)
    pawnRightPos = (pawnPos[0]+1,pawnPos[1]-1)
    if pawnLeftPos[0] >= 0 and pawnLeftPos[1] >= 0:
        if boardList[pawnLeftPos[1]][pawnLeftPos[0]] == "K":
            inCheck = True
    if pawnRightPos[0] < len(boardList) and pawnRightPos[1] >= 0:
        if boardList[pawnRightPos[1]][pawnRightPos[0]] == "K":
            inCheck = True

    return inCheck

def rook(rookPos:tuple,boardList:list):
    inCheck = False
    widthAndHeight = len(boardList)

    #Left
    finding = (rookPos[0]-1,rookPos[1])
    while finding[0] >= 0:
        found = boardList[finding[1]][finding[0]]
        if found in notKing:
            break
        if found == "K":
            inCheck = True
            break
        finding = (finding[0]-1,finding[1])
    
    if inCheck:
        return inCheck

    #Right
    finding = (rookPos[0]+1,rookPos[1])
    while finding[0] < widthAndHeight:
        found = boardList[finding[1]][finding[0]]
        if found in notKing:
            break
        if found == "K":
            inCheck = True
            break
        finding = (finding[0]+1,finding[1])

    if inCheck:
        return inCheck

    #Down
    finding = (rookPos[0],rookPos[1]+1)
    while finding[1] < widthAndHeight:
        found = boardList[finding[1]][finding[0]]
        if found in notKing:
            break
        if found == "K":
            inCheck = True
            break
        finding = (finding[0],finding[1]+1)

    if inCheck:
        return inCheck
    
    #Up
    finding = (rookPos[0],rookPos[1]-1)
    while finding[1] >= 0:
        found = boardList[finding[1]][finding[0]]
        if found in notKing:
            break
        if found == "K":
            inCheck = True
            break
        finding = (finding[0],finding[1]-1)

    return inCheck

def bishop(bishopPos:tuple, boardList:list):
    list1 = [[],[],[],[]]
    firstIn = bishopPos[0] - bishopPos[1]
    lastIn = bishopPos[0] + bishopPos[1]

    for lnIndex, line in enumerate(boardList):
        first = ""
        second = ""

        #check if index that bishop can go is on board
        if 0 <= firstIn <= len(boardList) - 1 and 0 <= lastIn <= len(boardList) - 1 :
            first = line[firstIn]
            second = line[lastIn]
        elif 0 <= firstIn <= len(boardList) - 1:
            first = line[firstIn]
        elif 0 <= lastIn <= len(boardList) - 1:
            second = line[lastIn]

        if lnIndex  < bishopPos[1]:
            #upperleft
            if first in withKing:
                list1[0].append(first)
            #upperright
            if second in withKing:
                list1[1].append(second)
        elif lnIndex  > bishopPos[1]:
            #lowerleft
            if second in withKing:
                list1[2].append(second)
            #lowerright
            if first in withKing:
                list1[3].append(first)
        else:
            pass

        firstIn += 1
        lastIn -= 1

    for index, value in enumerate(list1):
        if value.count("K"):
            if index < 2:
                if value.index("K") == len(value)-1:
                    return True
            else:
                if value.index("K") == 0:
                    return True

def checkmate(board:str):

    if not board:
        print("There is no board.")
    
    board = board.upper()
    boardList = board.split()
    height = len(boardList)
    kingCount = 0
    width = -1
    inCheck = False

    for i in boardList:
        localLength = len(i)
        if width == -1:
            width = localLength
        elif width != localLength:
            print("The board is invalid.")
            return
        kingCount += i.count("K")

    if height != width:
        print("The board is not a square.")
        return
    elif kingCount != 1:
        if not kingCount:
            print("No king is found on the board.")
        else:
            print("There is multiple king on the board.")
        return

    for lnIndex, line in enumerate(boardList):
        for colIndex, col in enumerate(line):
            if inCheck:
                break
            if col == "P":
                if pawn((colIndex,lnIndex),boardList):
                    inCheck = True
            elif col == "R":
                if rook((colIndex,lnIndex),boardList):
                    inCheck = True
            elif col == "B":
                if bishop((colIndex,lnIndex),boardList):
                    inCheck = True
            elif col == "Q":
                if bishop((colIndex,lnIndex),boardList) or rook((colIndex,lnIndex),boardList):
                    inCheck = True

    if inCheck:
        print("Success")
    else:
        print("Fail")