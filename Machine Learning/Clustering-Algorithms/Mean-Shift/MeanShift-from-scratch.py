import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import random
from sklearn.datasets.samples_generator import make_blobs

style.use("ggplot")

centers = random.randrange(2, 5)

X, y = make_blobs(n_samples=25, centers=centers, n_features=2)

# X = np.array([
#     [1, 2],
#     [1.5, 1.8],
#     [5, 8],
#     [8, 8],
#     [1, 0.6],
#     [9, 11],
#     [8, 2],
#     [10, 2],
#     [9, 3]
# ])


class MeanShift:
    def __init__(self, radius=None, radius_norm_step=100):
        self.radius = radius
        self.radius_norm_step = radius_norm_step
        self.centroids = {}
        self.classifications = {}

    def fit(self, data):

        if self.radius is None:
            all_data_centroid = np.average(data, axis=0)
            all_data_norm = np.linalg.norm(all_data_centroid)
            self.radius = all_data_norm / self.radius_norm_step

        centroids = {}
        # init all features as centroids
        for i in range(len(data)):
            centroids[i] = data[i]

        weights = [i for i in range(self.radius_norm_step)][::-1]

        while True:
            new_centroids = []
            for i in centroids:
                in_bandwidth = []
                centroid = centroids[i]

                # add in radius features
                for feature_set in data:
                    distance = np.linalg.norm(feature_set - centroid)
                    if distance == 0:
                        distance = 0.00001
                    weight_index = int(distance / self.radius)
                    if weight_index > len(weights) - 1:
                        weight_index = len(weights) - 1
                    # we are adding the features n times
                    # where n is defined according ti weight
                    to_add = (weights[weight_index] ** 2) * [feature_set]
                    in_bandwidth += to_add

                new_centroid = np.average(in_bandwidth, axis=0)
                new_centroids.append(tuple(new_centroid))

            unique_centroids = sorted(list(set(new_centroids)))

            to_pop = []

            for i in unique_centroids:
                for ii in unique_centroids:
                    if i == ii:
                        continue
                    elif np.linalg.norm(np.array(i) - np.array(ii)) <= self.radius:
                        to_pop.append(ii)
                        break

            for i in to_pop:
                try:
                    unique_centroids.remove(i)
                except ValueError:
                    pass
            del to_pop

            prev_centroids = dict(centroids)
            centroids = {}
            for i in range(len(unique_centroids)):
                centroids[i] = np.array(unique_centroids[i])

            optimized = True
            for i in centroids:
                if not np.array_equal(centroids[i], prev_centroids[i]):
                    optimized = False
                    break

            if optimized:
                break

        self.centroids = centroids

        # divide all features in classifications
        self.classifications = {}
        for i in range(len(self.centroids)):
            self.classifications[i] = []
        for feature_set in data:
            distances = [np.linalg.norm(feature_set - self.centroids[centroid])
                         for centroid in self.centroids]
            classification = distances.index(min(distances))
            self.classifications[classification].append(feature_set)

    def predict(self, feature_set):
        if self.centroids == {}:
            return
        distances = [np.linalg.norm(feature_set - self.centroids[centroid])
                     for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification


def main(data):
    colors = 2 * ['g', 'r', 'c', 'b', 'k']
    clf = MeanShift()
    clf.fit(data)
    centroids = clf.centroids

    for classification in clf.classifications:
        color = colors[classification]
        for feature_set in clf.classifications[classification]:
            plt.scatter(feature_set[0], feature_set[1], marker='*', s=150, color=color)

    for c in centroids:
        plt.scatter(centroids[c][0], centroids[c][1], s=150, color='k', marker='*')
    plt.show()


if __name__ == '__main__':
    main(X)
