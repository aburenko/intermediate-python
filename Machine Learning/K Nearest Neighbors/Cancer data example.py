import numpy as np
import pandas as pd
from sklearn import neighbors
from sklearn.model_selection import train_test_split

df = pd.read_csv('../../../breast-cancer-wisconsin.data')

# look for useless data
# replace missing data
df.replace('?', -99999, inplace=True)
# remove id because it plays no role for us
# when including the id column it will show significant changes
# because it will predict the result on hand of id what is harmful
df.drop(['id'], 1, inplace=True)

# define features and labels
X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# create and train the classifier
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print("Accuracy of the classifier is {}".format(accuracy))

# make prediction with one example
example_measures = np.array([[4, 2, 1, 1, 1, 2, 3, 2, 1], [7, 2, 1, 4, 1, 6, 3, 2, 1]])
example_measures = example_measures.reshape(len(example_measures), -1)
prediction = clf.predict(example_measures)
print(prediction)
