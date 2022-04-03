import time
import sys
import puzzleFunction

filename = sys.argv[1]
arrData = puzzleFunction.readFileInput(filename)
run = puzzleFunction.isRun(arrData)

startProcess = time.time()
arrDataQueue = [[0,0,"",""]]
arrQueue = [arrData]

arrDataStart = arrData

arrDataPrint = [[0,0,"",""]]
arrPrint = [arrDataStart]

countSimpul = 0
if (run):
    print("Penyelesaian Puzzle")
    while(puzzleFunction.isDone(arrData) == False):
        arrData = arrQueue[0]
        data = arrDataQueue[0]
        level = arrDataQueue[0][1]
        lastCommand = arrDataQueue[0][2]
        idPos = arrDataQueue[0][3]
        arrQueue = puzzleFunction.delQueue(arrQueue)
        arrDataQueue = puzzleFunction.delDataQueue(arrDataQueue)
        upScore = puzzleFunction.moveUpScore(arrData, level+1)
        leftScore = puzzleFunction.moveLeftScore(arrData, level+1)
        downScore = puzzleFunction.moveDownScore(arrData, level+1)
        rightScore = puzzleFunction.moveRightScore(arrData, level+1)
        arrDataLeft = puzzleFunction.moveLeft(arrData)
        arrDataRight = puzzleFunction.moveRight(arrData)
        arrDataUp = puzzleFunction.moveUp(arrData)
        arrDataDown = puzzleFunction.moveDown(arrData)

        if (lastCommand == "Left"):
            rightScore = 99999
        

        elif (lastCommand == "Right"):
            leftScore = 99999
        

        elif (lastCommand == "Up"):
            downScore = 99999
                

        elif (lastCommand == "Down"):
            upScore = 99999

        if (leftScore != 99999):
            countSimpul += 1
            idNew = idPos + "L"
            arrDataQueue = puzzleFunction.addDataQueue(arrDataQueue, leftScore, level+1, "Left", idNew)
            posArr = puzzleFunction.dataQueuePos(arrDataQueue, leftScore)
            arrQueue = puzzleFunction.addQueuePos(arrQueue,arrDataLeft,posArr)
            arrDataPrint.append([leftScore, level+1, "Left", idNew])
            arrPrint.append(arrDataLeft)

        if (rightScore != 99999):
            countSimpul += 1
            idNew = idPos + "R"
            arrDataQueue = puzzleFunction.addDataQueue(arrDataQueue, rightScore, level+1, "Right", idNew)
            posArr = puzzleFunction.dataQueuePos(arrDataQueue, rightScore)
            arrQueue = puzzleFunction.addQueuePos(arrQueue,arrDataRight,posArr)
            arrDataPrint.append([rightScore, level+1, "Right", idNew])
            arrPrint.append(arrDataRight)

        if (upScore != 99999):
            countSimpul += 1
            idNew = idPos + "U"
            arrDataQueue = puzzleFunction.addDataQueue(arrDataQueue, upScore, level+1, "Up", idNew)
            posArr = puzzleFunction.dataQueuePos(arrDataQueue, upScore)
            arrQueue = puzzleFunction.addQueuePos(arrQueue,arrDataUp,posArr)
            arrDataPrint.append([upScore, level+1, "Up", idNew])
            arrPrint.append(arrDataUp)
        
        if (downScore != 99999):
            countSimpul += 1
            idNew = idPos + "D"
            arrDataQueue = puzzleFunction.addDataQueue(arrDataQueue, downScore, level+1, "Down", idNew)
            posArr = puzzleFunction.dataQueuePos(arrDataQueue, downScore)
            arrQueue = puzzleFunction.addQueuePos(arrQueue,arrDataDown,posArr)
            arrDataPrint.append([downScore, level+1, "Down", idNew])
            arrPrint.append(arrDataDown)
    
        if (upScore <= leftScore and upScore <= rightScore and upScore <= downScore):
            idNew = idPos + "U"
            data = [upScore, level+1, "Up", idNew]
            arrData = puzzleFunction.moveUp(arrData)

        
        elif (rightScore <= leftScore and rightScore <= upScore and rightScore <= downScore):
            idNew = idPos + "R"
            data = [rightScore, level+1, "Right", idNew]
            arrData = puzzleFunction.moveRight(arrData)

        
        elif (downScore <= leftScore and downScore <= rightScore and downScore <= upScore):
            idNew = idPos + "D"
            data = [downScore, level+1, "Down", idNew]
            arrData = puzzleFunction.moveDown(arrData)

        
        elif (leftScore <= rightScore and leftScore <= upScore and leftScore <= downScore):
            idNew = idPos + "L"
            data = [leftScore, level+1, "Left", idNew]
            arrData = puzzleFunction.moveLeft(arrData)


    total = 0
    for i in range (0, len(arrDataPrint)):
        isPrint = True
        for j in range (0, len(arrDataPrint[i][3])):
            if(len(arrDataPrint[i][3]) > len(data[3])):
                isPrint = False
            elif (arrDataPrint[i][3][j] != data[3][j]):
                isPrint = False
        if (isPrint):
            total += 1
            if (arrDataPrint[i][2] == ''):
                print("Awal data: ")
            else:
                print("Perintah: " + arrDataPrint[i][2])
            puzzleFunction.printArr(arrPrint[i])

    endProcess = time.time()
    print("Waktu yang dibutuhkan: " + str(endProcess-startProcess) + " detik")
    print("Jumlah langkah yang dilakukan: " + str(total-1))
    print("Jumlah simpul yang dibangkitkan: " + str(countSimpul))

else:
    print("Puzzle tidak dapat diselesaikan")