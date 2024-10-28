#!/Users/pfb2024/mamba/envs/bio/bin/python
import pandas as pd

#read in the data using pandas
df = pd.read_csv('diabetes_data.csv')
#check data has been read in properly
df.head()
#print(df.head())

#check number of rows and columns in dataset
#print(df.shape)

#create a dataframe with all training data except the target column
X = df.drop(columns=['diabetes'])
#check that the target variable has been removed
#print(X.head())

#separate target values
y = df['diabetes'].values
#view target values
#print(y[0:5])

###train and test the model using the the holdout method
#from sklearn.model_selection import train_test_split
##split dataset into train and test data
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)

from sklearn.neighbors import KNeighborsClassifier
##Create KNN classifier, where classified by majority of three
#knn = KNeighborsClassifier(n_neighbors = 3)
## Fit the classifier to the data
#knn.fit(X_train,y_train)

##show first 5 model predictions on the test data
#print(knn.predict(X_test)[0:5])

##check accuracy of our model on the test data by scoring it
#print(knn.score(X_test, y_test))

###train and test model using cross validation
from sklearn.model_selection import cross_val_score
import numpy as np
#create a new KNN model
knn_cv = KNeighborsClassifier(n_neighbors=3)
#train model with cv of 5 
cv_scores = cross_val_score(knn_cv, X, y, cv=5)
#print each cv score (accuracy) and average them
print(cv_scores)
print('cv_scores mean:{}'.format(np.mean(cv_scores)))

###run a test to find the best n_neighbors value
from sklearn.model_selection import GridSearchCV
#create new a knn model
knn2 = KNeighborsClassifier()
#create a dictionary of all values we want to test for n_neighbors
param_grid = {'n_neighbors': np.arange(1, 25)}
#use gridsearch to test all values for n_neighbors
knn_gscv = GridSearchCV(knn2, param_grid, cv=5)
#fit model to data
knn_gscv.fit(X, y)
#check top performing n_neighbors value
print(knn_gscv.best_params_)
#check mean score for the top performing value of n_neighbors
print(knn_gscv.best_score_)