
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

#Preprocessing start
df_xlsx=pd.read_excel('Data.xlsx')
#print(df_xlsx["Logical"].plot.hist())
#print(df_xlsx.head(3))
gender=(pd.get_dummies(df_xlsx['Gender'],drop_first=True))
board10=(pd.get_dummies(df_xlsx['10board']))
board12=(pd.get_dummies(df_xlsx['12board']))
specialization=(pd.get_dummies(df_xlsx['Specialization']))
degree=(pd.get_dummies(df_xlsx['Degree']))
collegestate=(pd.get_dummies(df_xlsx['CollegeState']))
df_xlsx=pd.concat([df_xlsx,gender,board10,specialization,degree,collegestate,board12],axis=1)
#print(df_xlsx.head(4))
df_xlsx.drop(['DOB','Gender','10board','CollegeState','Specialization','Degree','ID','12board'],axis=1,inplace=True)
#print(df_xlsx.head(4))
X=df_xlsx.drop('High-Salary',axis=1)
y=df_xlsx['High-Salary']
#Preprocessing over


X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.3,random_state=1)
logmodel=LogisticRegression(max_iter=10000)
logmodel.fit(X_train,y_train)
print(logmodel.score(X_test,y_test))

li=[0.1,0.2,0.3,0.4,0.5]
list1=[]
for cnt in range(0,5):
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=li[cnt],random_state=1,shuffle=False)
    logmodel=LogisticRegression(max_iter=10000)
    logmodel.fit(X_train,y_train)
    list1.append(logmodel.score(X_test,y_test))
                           print(confusion_matrix(y_test,logmodel.predict(X_test)))

xs = np.array(li)
ys = np.array(list1)    
plt.plot(xs, ys)
plt.show()

list2=[]
for cnt in range(0,5):
    X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=li[cnt],random_state=1,shuffle=True)
    logmodel=LogisticRegression(max_iter=10000)
    logmodel.fit(X_train,y_train)
    list2.append(logmodel.score(X_test,y_test))
     print(confusion_matrix(y_test,logmodel.predict(X_test)))

xs = np.array(li)
ys = np.array(list2)
plt.plot(xs, ys)
plt.show()

df_xlsx.drop(['CollegeID','CollegeCityID','collegestate'])
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.1,random_state=1)
logmodel=LogisticRegression(max_iter=10000)
logmodel.fit(X_train,y_train,shuffle=True)
print(logmodel.score(X_test,y_test))
print(confusion_matrix(y_test,logmodel.predict(X_test)))
