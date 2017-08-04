import pandas as pd
import types

from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model, tree
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier

def multi_train(X,vector,predict):
 
    seed = 7
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    # create the sub models
    estimators = []
    model1 = LogisticRegression()
    estimators.append(('logistic', model1))
    model2 = DecisionTreeClassifier()
    estimators.append(('cart', model2))
    model3 = SVC()
    estimators.append(('svm', model3))
    # create the ensemble model
    ensemble = VotingClassifier(estimators)
    results = model_selection.cross_val_score(ensemble, X, Y, cv=kfold)
    print(results.mean())

def d_tree_train_1(X,vector,predict):
    clf=tree.DecisionTreeClassifier()
    clf=clf.fit(X,vector)
    print clf.predict(predict)
    return clf.predict(predict)

def d_tree_train_2(X,vector,predict):
    #clf=tree.DecisionTreeClassifier()
    clf = tree.DecisionTreeRegressor()
    clf=clf.fit(X,vector)
    print clf.predict(predict)
    return clf.predict(predict)

def rf_train(X,vector,predict):
    rf = RandomForestClassifier(n_estimators=100) # initialize
    rf.fit(X, vector) # fit the data to the algorithm
    print rf.predict(predict)
    return rf.predict(predict)
    
def train_1(X,vector,predict):
    #X = [[0.44, 0.68], [0.99, 0.23]]
    #vector = [109.85, 155.72]
    #predict= [0.49, 0.18]
    """
    print "**********************"
    print X
    print "^^^^^^^^^^^^^^"
    print vector
    print "**********************"
    """
    #predict=[0,1,0,0,1,0,0,0,1,0]
    #predict=[0,0,0,1,1,1,0,0,0,0]
    #predict=[0,1,0,0,1,1,0,0,0,0]

    poly = PolynomialFeatures(degree=2)
    X_ = poly.fit_transform(X)
    predict_ = poly.fit_transform(predict)

    clf = linear_model.LinearRegression()
    clf.fit(X_, vector)
    #print clf.predict(predict_)
    return clf.predict(predict_)

def main():
    df = pd.read_csv("one_pr.txt",usecols=[2,3,4,5,6,7,8,9,10,11]) 
    """
    print df.columns
    print df.values
    """
    df1 = pd.read_csv("one_pr.txt",usecols=[13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]) 
    """
    print df1.columns
    print df1.values
    print df1[df1.columns[0]]
    #print type(df1_co_1)
    print type(df)
    """
    #predict=[0,0,0,1,1,1,0,0,0,0]
    predict=[0,1,0,0,1,1,0,0,0,0]
    a_df = df.values
    test_case_predict=[]
    test_case_predict_1=[]
    test_case_predict_2=[]
    test_case_predict_3=[]

    for i in range(len(df1.columns)): 
       df1_co_1= df1[df1.columns[i]]
       a_df1 = df1_co_1.values
       test_case_predict.append(train_1(a_df,a_df1.transpose(),predict))
       #test_case_predict_1.append(d_tree_train_1(a_df,a_df1.transpose(),predict))
       test_case_predict_2.append(d_tree_train_1(a_df,a_df1.transpose(),predict))
       test_case_predict_3.append(rf_train(a_df,a_df1.transpose(),predict))
    for p in range(len(test_case_predict)):
       #print test_case_predict[p], test_case_predict_1[p],test_case_predict_2[p]
       print df1.columns[p],test_case_predict[p],test_case_predict_2[p],test_case_predict_3[p]

main()
