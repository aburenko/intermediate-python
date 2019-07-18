# features and labels
# features are data that are major values for the prediction of label
# label are the predictions
import math
import quandl
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')

# get data in form of a data frame
df = quandl.get('WIKI/GOOGL')
# get only valuable columns
# values description:
#   open price of the day
#   highest price of the day
#   lowest price of the day
#   close price of the day
#   volume - value?
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume', ]]
# define new column for percent volatility, highlow_percent
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
# daily percent change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

# after init of better values for features
# take only the values we are care about
# so out features are:
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
print(df.head())

forecast_col = 'Adj. Close'
# in ML no "not a number" data so use -99999 and not NA
df.fillna(-99999, inplace=True)
# round to upper floor the number of days out
# so we want to predict with n days before
forecast_out = int(math.ceil(0.01 * len(df)))
print("length of df is {} and forecast_out is {}".format(len(df), forecast_out))
# creating label
# shift shifts the rows down, so with negative number it will
# shift the values upwards and we are going to become the future numbers
df['label'] = df[forecast_col].shift(-forecast_out)

print(df.head())

# X is all except label
X = np.array(df.drop(['label'], 1))
# scale values
# becomes values between 0 and 1
X = preprocessing.scale(X)

X = X[:-forecast_out]
X_lately = X[-forecast_out:]
# y is only the label
# delete not a number values
df.dropna(inplace=True)
y = np.array(df['label'])

# there are train and test X and y
# we want to use different variables because we want test
# the classifier on other data than we trained it on
# test size specifies how many data in percent we want to use
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)

# PICKLE save classifier
# with open('linearregression.pickle', 'wb') as f:
#     pickle.dump(clf., f)
# PICKLE load saved classifier
# to avoid training it one more time
# pickle_in = open('linearregression.pickle', 'rb')
# clf = pickle.load(pickle_in)


accuracy = clf.score(X_test, y_test)

print("accuracy is {}".format(accuracy))

# doing a prediction

forecast_set = clf.predict(X_lately)
# print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan

# find out what the last day was
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

# add forecasts in data frame (df)
for i in forecast_set:
    print(i)
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]

print(df.head())

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Data')
plt.ylabel('Price')
plt.show()
