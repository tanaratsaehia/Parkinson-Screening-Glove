import pandas as pd
from sklearn import svm
import pickle

pathcsvl = str("D:/GloveAi/NewDataLeft.csv")
pathcsvr = str("D:/GloveAi/NewDataRight.csv")

dfR = pd.read_csv(pathcsvl)
xR = dfR[['x1', 'y1', 'z1', 'x2', 'y2', 'z2']]
yR = dfR['par_state']
linearR = svm.SVC(kernel = 'linear')
polyR = svm.SVC(kernel = 'poly')
rbfR = svm.SVC(kernel = 'rbf')

dfL = pd.read_csv(pathcsvl)
xL = dfL[['x1', 'y1', 'z1', 'x2', 'y2', 'z2']]
yL = dfL['par_state']
linearL = svm.SVC(kernel = 'linear')
polyL = svm.SVC(kernel = 'poly')
rbfL = svm.SVC(kernel = 'rbf')
print("kernel loaded")

linearModelRight = linearR.fit(xR, yR)
polyModelRight = polyR.fit(xR, yR)
rbfModelRight = rbfR.fit(xR, yR)

linearModelLeft = linearL.fit(xL, yL)
polyModelLeft = polyL.fit(xL, yL)
rbfModelLeft = rbfL.fit(xL, yL)
print("model fited")

filenamelinearRight = 'finalized_model_linear_right.sav'
filenamepolyRight = 'finalized_model_poly_right.sav'
filenamerbfRight = 'finalized_model_rbf_right.sav'
filenamelinearLeft = 'finalized_model_linear_left.sav'
filenamepolyLeft = 'finalized_model_poly_left.sav'
filenamerbfLeft = 'finalized_model_rbf_left.sav'
pickle.dump(linearModelRight, open(filenamelinearRight, 'wb'))
pickle.dump(polyModelRight, open(filenamepolyRight, 'wb'))
pickle.dump(rbfModelRight, open(filenamerbfRight, 'wb'))
pickle.dump(linearModelLeft, open(filenamelinearLeft, 'wb'))
pickle.dump(polyModelLeft, open(filenamepolyLeft, 'wb'))
pickle.dump(rbfModelLeft, open(filenamerbfLeft, 'wb'))
print("model saved")

loaded_model_linear_right = pickle.load(open('finalized_model_linear_right.sav', 'rb'))
loaded_model_poly_right = pickle.load(open('finalized_model_poly_right.sav', 'rb'))
loaded_model_rbf_right = pickle.load(open('finalized_model_rbf_right.sav', 'rb'))

loaded_model_linear_left = pickle.load(open('finalized_model_linear_left.sav', 'rb'))
loaded_model_poly_left = pickle.load(open('finalized_model_poly_left.sav', 'rb'))
loaded_model_rbf_left = pickle.load(open('finalized_model_rbf_left.sav', 'rb'))
print("model loaded")

#predict test
answer1 = loaded_model_linear_right.predict([[9.18,-1.96,7.18,10.87,0.47,-1.37]])
answer2 = loaded_model_poly_right.predict([[9.18,-1.96,7.18,10.87,0.47,-1.37]])
answer3 = loaded_model_rbf_right.predict([[9.18,-1.96,7.18,10.87,0.47,-1.37]])

answer4 = loaded_model_linear_left.predict([[9.18,-1.96,7.18,10.87,0.47,-1.37]])
answer5 = loaded_model_poly_left.predict([[9.18,-1.96,7.18,10.87,0.47,-1.37]])
answer6 = loaded_model_rbf_left.predict([[9.18,-1.96,7.18,10.87,0.47,-1.37]])
print("predicted")

answerStr1 = answer1[0]
answerStr2 = answer2[0]
answerStr3 = answer3[0]
answerStr4 = answer4[0]
answerStr5 = answer5[0]
answerStr6 = answer6[0]

print(answerStr1)
print(answerStr2)
print(answerStr3)
print(answerStr4)
print(answerStr5)
print(answerStr6)