import serial
import pandas as pd
from sklearn import svm
from datetime import datetime as dt 
xxxxx = str("D:/GloveAi/NewDataLeft.csv")
df = pd.read_csv(xxxxx)
x = df[['x1', 'y1', 'z1', 'x2', 'y2', 'z2']]
y = df['par_state']
linear = svm.SVC(kernel = 'linear')
poly = svm.SVC(kernel = 'poly')
rbf = svm.SVC(kernel = 'rbf')
print()
print('kernel loaded')
print()
linearModel = linear.fit(x, y)
polyModel = poly.fit(x, y)
rbfModel = rbf.fit(x, y)
print('model fited')

while True:
    c = 0
    parCount = 0

    print()
    inputText = input("Hands 'R'(right) or 'L'(left) or Exit : ")
    print()
    if inputText == "Exit" or inputText == "exit" or inputText == "EXIT" or inputText == "e":
        break
    elif inputText != "r" and inputText != "R" and inputText != "l" and inputText != "L":
            print("plase input R or L or Exit")
            continue
    kernelText = input("Kernel 'L'(Linear) or 'P'(poly) or 'R'(rbf) : ")
    print()

    if kernelText == "l" or kernelText == "L" or  kernelText == "linear" or kernelText == "Linear" or kernelText == "LINEAR":
        modelTrained = linearModel
    elif kernelText == "p" or kernelText == "P" or kernelText == "poly" or kernelText == "Poly" or kernelText == "POLY":
        modelTrained = polyModel
    elif kernelText == "r" or kernelText == "R" or kernelText == "rbf" or kernelText == "Rbf" or kernelText == "RBF":
        modelTrained = rbfModel 
    else:
        print()
        print("plase chose kennel")
        print()
        continue

    if inputText == "R" or inputText == "r":
        ser = serial.Serial("COM4", 9600)
        while True:
            if c >= 103:
                break
            elif c > 2:
                x = ser.readline()
                #strX = x.encode("UTF-8")
                a = x.strip()
                b = str(a)
                b = b.replace("b","")
                b = b.replace("'","")
                listX = b.split('_')
                print(listX)

                x = ser.readline()
                #strX = x.encode("UTF-8")
                a = x.strip()
                b = str(a)
                b = b.replace("b","")
                b = b.replace("'","")
                listX = b.split('_')
                x1 = float(listX[0])
                y1 = float(listX[1])
                z1 = float(listX[2])
                x2 = float(listX[3])
                y2 = float(listX[4])
                z2 = float(listX[5])
                realData = [x1, y1, z1, x2, y2, z2]
                print(realData)
                answer = modelTrained.predict([realData])
                answerStr = answer[0]
                print(answerStr)
                if answer[0] == 'par':
                    parCount += 1
            c += 1
        del ser, modelTrained

    elif inputText == "L" or inputText == "l":
        ser2 = serial.Serial("COM6", 9600)
        while True:
            if c >= 103:
                break
            elif c > 2:
                x2 = ser2.readline()
                #strX = x.encode("UTF-8")
                a2 = x2.strip()
                b2 = str(a2)
                b2 = b2.replace("b","")
                b2 = b2.replace("'","")
                listX = b2.split('_')
                print(listX)

                x2 = ser2.readline()
                #strX = x.encode("UTF-8")
                a2 = x2.strip()
                b2 = str(a2)
                b2 = b2.replace("b","")
                b2 = b2.replace("'","")
                listX = b2.split('_')

                x1 = float(listX[0])
                y1 = float(listX[1])
                z1 = float(listX[2])
                x2 = float(listX[3])
                y2 = float(listX[4])
                z2 = float(listX[5])
                realData = [x1, y1, z1, x2, y2, z2]
                print(realData)
                answer = modelTrained.predict([realData])
                answerStr = answer[0]
                print(answerStr)
                if answer[0] == 'par':
                    parCount += 1
            c += 1
        del ser2, modelTrained


    print()
    print()
    print(parCount)
    if parCount >= 30:
        print()
        print('----------------->parkinson is detected')
    else:
        print()
        print('----------------->you are normal')
    #print(modelTrained)