def isDone(arrData):
    i = 0
    while (i < 4) :
        j = 0
        while (j < 4) :
            checkResult = i * 4 + j + 1
            if (arrData[i][j] != checkResult) :
                return False
            j += 1
        i += 1
    return True

def findEmpty(arrData):
    resultTemp = [-1, -1]
    i = 0
    while (i < 4) :
        j = 0
        while (j < 4) :
            if (arrData[i][j] == 16) :
                result = [i, j]
                return result
            j += 1
        i += 1
    return resultTemp

def findScore(arrData, level):
    finalResult = 0
    position = findEmpty(arrData)
    i = 0
    while (i < 4) :
        j = 0
        while (j < 4) :
            if (i != position[0] or j != position[1]) :
                if (arrData[i][j] != i * 4 + j + 1) :
                    finalResult += 1
            j += 1
        i += 1
    finalResult += level
    return finalResult

def moveLeftScore(arrData, level):
    arrData2 = [[0] * (4) for _ in range(4)]
    i = 0
    while (i < 4) :
        j = 0
        while (j < 4) :
            arrData2[i][j] = arrData[i][j]
            j += 1
        i += 1
    position = findEmpty(arrData2)
    if (position[1] > 0) :
        saveData = arrData2[position[0]][position[1]]
        arrData2[position[0]][position[1]] = arrData2[position[0]][position[1] - 1]
        arrData2[position[0]][position[1] - 1] = saveData
        score = findScore(arrData2, level)
        return score
    else :
        return 99999

def moveRightScore(arrData, level):
    arrData2 = [[0] * (4) for _ in range(4)]
    i = 0
    while (i < 4) :
        j = 0
        while (j < 4) :
            arrData2[i][j] = arrData[i][j]
            j += 1
        i += 1
    position = findEmpty(arrData2)
    if (position[1] < 3) :
        saveData = arrData2[position[0]][position[1]]
        arrData2[position[0]][position[1]] = arrData2[position[0]][position[1] + 1]
        arrData2[position[0]][position[1] + 1] = saveData
        score = findScore(arrData2, level)
        return score
    else :
        return 99999

def moveUpScore(arrData, level):
    arrData2 = [[0] * (4) for _ in range(4)]
    i = 0
    while (i < 4) :
        j = 0
        while (j < 4) :
            arrData2[i][j] = arrData[i][j]
            j += 1
        i += 1
    position = findEmpty(arrData2)
    if (position[0] > 0) :
        saveData = arrData2[position[0]][position[1]]
        arrData2[position[0]][position[1]] = arrData2[position[0] - 1][position[1]]
        arrData2[position[0] - 1][position[1]] = saveData
        score = findScore(arrData2, level)
        return score
    else :
        return 99999

def moveDownScore(arrData, level):
    arrData2 = [[0] * (4) for _ in range(4)]
    i = 0
    while (i < 4) :
        j = 0
        while (j < 4) :
            arrData2[i][j] = arrData[i][j]
            j += 1
        i += 1
    position = findEmpty(arrData2)
    if (position[0] < 3) :
        saveData = arrData2[position[0]][position[1]]
        arrData2[position[0]][position[1]] = arrData2[position[0] + 1][position[1]]
        arrData2[position[0] + 1][position[1]] = saveData
        score = findScore(arrData2, level)
        return score
    else :
        return 99999

def moveLeft(arrData):
    arrData2 = [[0] * (4) for _ in range(4)]
    i = 0
    while (i < 4) :
        j = 0
        while (j < 4) :
            arrData2[i][j] = arrData[i][j]
            j += 1
        i += 1
    position = findEmpty(arrData2)
    if (position[1] > 0) :
        saveData = arrData2[position[0]][position[1]]
        arrData2[position[0]][position[1]] = arrData2[position[0]][position[1] - 1]
        arrData2[position[0]][position[1] - 1] = saveData
    return arrData2

def moveRight(arrData):
    arrData2 = [[0] * (4) for _ in range(4)]
    i = 0
    while (i < 4) :
        j = 0
        while (j < 4) :
            arrData2[i][j] = arrData[i][j]
            j += 1
        i += 1
    position = findEmpty(arrData2)
    if (position[1] < 3) :
        saveData = arrData2[position[0]][position[1]]
        arrData2[position[0]][position[1]] = arrData2[position[0]][position[1] + 1]
        arrData2[position[0]][position[1] + 1] = saveData
    return arrData2

def moveUp(arrData):
    arrData2 = [[0] * (4) for _ in range(4)]
    i = 0
    while (i < 4) :
        j = 0
        while (j < 4) :
            arrData2[i][j] = arrData[i][j]
            j += 1
        i += 1
    position = findEmpty(arrData2)
    if (position[0] > 0) :
        saveData = arrData2[position[0]][position[1]]
        arrData2[position[0]][position[1]] = arrData2[position[0] - 1][position[1]]
        arrData2[position[0] - 1][position[1]] = saveData
    return arrData2

def moveDown(arrData):
    arrData2 = [[0] * (4) for _ in range(4)]
    i = 0
    while (i < 4) :
        j = 0
        while (j < 4) :
            arrData2[i][j] = arrData[i][j]
            j += 1
        i += 1
    position = findEmpty(arrData2)
    if (position[0] < 3) :
        saveData = arrData2[position[0]][position[1]]
        arrData2[position[0]][position[1]] = arrData2[position[0] + 1][position[1]]
        arrData2[position[0] + 1][position[1]] = saveData
    return arrData2

def readFileInput(filename) :
    arrData2 = [[0] * (4) for _ in range(4)]
    f = open(filename, "r")
    for i in range (0,4):
        line = f.readline()
        arrLine = line.split()
        for j in range (0,4):
            if (arrLine[j] == "-"):
                arrData2[i][j] = 16
            else:
                arrData2[i][j] = int(arrLine[j])
    
    return arrData2

def printArr(arrData):
    i = 0
    while (i < 4) :
        j = 0
        while (j < 4) :
            if (arrData[i][j] == 16):
                print("- ", end = "")
            else:
                print(str(arrData[i][j]) + " ", end ="")
            j += 1
        print()
        i += 1
    print()

def isRun(arrData):
    simpanScore = [0] * (16)
    countRun = 0
    positionXStart = -1
    positionYStart = -1
    i = 0
    while (i < 4) :
        j = 0
        while (j < 4) :
            checkScore = 0
            if (arrData[i][j] == 16) :
                positionYStart = i + 1
                positionXStart = j + 1
            m = j
            while (m < 4) :
                if (arrData[i][m] < arrData[i][j]) :
                    checkScore += 1
                m += 1
            k = i + 1
            while (k < 4) :
                l = 0
                while (l < 4) :
                    if (arrData[k][l] < arrData[i][j]) :
                        checkScore += 1
                    l += 1
                k += 1
            countRun += checkScore
            simpanScore[arrData[i][j]-1] = checkScore
            j += 1
        i += 1
    X = 0
    if ((positionXStart % 2 == 0 and positionYStart % 2 == 1) or (positionXStart % 2 == 1 and positionYStart % 2 == 0)) :
        countRun += 1
        X = 1
    print("Nilai Kurang(i): ")
    for i in range (0, 16):
        print("Dari " + str(i+1) + ": " + str(simpanScore[i])) 
    print("Nilai X: " + str(X))
    print("Nilai Akhir: " + str(countRun))
    print()
    if (countRun % 2 == 0) :
        return True
    else :
        return False

def addDataQueue(arrDataQueue, score, levelQueue, lastCommandTemp, idTemp):
    i = 0
    arrDataQueue2 = []
    while (i < len(arrDataQueue) and arrDataQueue[i][0] < score):
        if (arrDataQueue[i] not in arrDataQueue2):
            arrDataQueue2.append(arrDataQueue[i])
        i += 1
    
    listInsert = [score,levelQueue,lastCommandTemp,idTemp]
    if (listInsert not in arrDataQueue2):
        arrDataQueue2.append(listInsert)

    for j in range (i, len(arrDataQueue)):
        if (arrDataQueue[j] not in arrDataQueue2):
            arrDataQueue2.append(arrDataQueue[j])

    return arrDataQueue2
    
def dataQueuePos(arrDataQueue, score):
    i = 0
    while (i < len(arrDataQueue) and arrDataQueue[i][0] < score):
        i += 1
    return i

def addQueuePos(arrQueue, arrData, posArr):
    if (arrQueue == None or len(arrQueue) == 0) :
        arrQueue2 = [None] * (1)
        arrQueue2[0] = arrData
        return arrQueue2
    else :
        arrQueue2 = [None] * (len(arrQueue) + 1)
        i = 0
        while (i < posArr) :
            arrQueue2[i] = arrQueue[i]
            i += 1

        arrQueue2[posArr] = arrData
        i = len(arrQueue2) - 1

        while (i > posArr) :
            arrQueue2[i] = arrQueue[i - 1]
            i -= 1
        return arrQueue2

def delQueue(arrQueue):
    if (len(arrQueue) == 1):
        return []

    else:
        for i in range (0, len(arrQueue)-1):
            arrQueue[i] = arrQueue[i+1]
            
        return arrQueue

def delDataQueue(arrDataQueue):
    if (len(arrDataQueue) == 1):
        return []
        
    else:
        for i in range (0, len(arrDataQueue)-1):
            arrDataQueue[i] = arrDataQueue[i+1]
            
        return arrDataQueue