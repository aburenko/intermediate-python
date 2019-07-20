import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter

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

    return vote_result


# example data set
data_set = {'k': [[1, 2], [2, 3], [3, 1]],
            'r': [[6, 5], [7, 7], [8, 6]]}

# define and identify new feature
new_features = [5, 7]
result = k_nearest_neighbors(data_set, new_features, k=3)
print(result)

# scatter all values
[[plt.scatter(*values, s=100, color=key) for values in data_set[key]] for key in data_set]
# scatter new value
plt.scatter(new_features[0], new_features[1], s=150, color="b")

plt.show()
