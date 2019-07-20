import random
import numpy as np
from matplotlib import style
from collections import Counter
import pandas as pd

from sklearn.model_selection import train_test_split

style.use('fivethirtyeight')


def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        print("K is set to a value less than total voting group")

    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euclidean_distance, group])

    # get all group names for sorted first k elements
    votes = [i[1] for i in sorted(distances)[:k]]
    # give back the most common
    vote_result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1] / k

    return vote_result, confidence


df = pd.read_csv('../../../breast-cancer-wisconsin.data')

df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)

full_data = df.astype(float).values.tolist()
random.shuffle(full_data)

test_size = 0.2
train_set = {2: [], 4: []}
test_set = {2: [], 4: []}
train_data = full_data[:-int(test_size * len(full_data))]
test_data = full_data[-int(test_size * len(full_data)):]

# i[-1] will be the class(group)
# i[:-1] gives us the list with all element without group

for i in train_data:
    train_set[i[-1]].append(i[:-1])

for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        vote, conf = k_nearest_neighbors(train_set, data, k=5)
        if group == vote:
            correct += 1
        else:
            print(conf)
        total += 1

print("Accuracy:", correct / total)