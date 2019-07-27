import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use("ggplot")

X = np.array([
    [1, 2],
    [1.5, 1.8],
    [5, 8],
    [8, 8],
    [1, 0.6],
    [9, 11]
])


class KMeans:
    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

        self.centroids = {}
        self.classifications = {}

    def fit(self, data):
        # take k first features
        for i in range(self.k):
            self.centroids[i] = data[i]
        # start iterating
        for i in range(self.max_iter):
            # clear classifications
            for j in range(self.k):
                self.classifications[j] = []

            for feature_set in data:
                # get distances to each centroid
                distances = [np.linalg.norm(feature_set - self.centroids[centroid])
                             for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(feature_set)

            prev_centroids = dict(self.centroids)
            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            # look if optimized with given tolerance
            optimized = True
            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid-original_centroid)/original_centroid*100) > self.tol:
                    optimized = False
                    break

            if optimized:
                break

    def predict(self, feature_set):
        distances = [np.linalg.norm(feature_set - self.centroids[centroid])
                     for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification


def plot_clf(clf, colors):
    for cen in clf.centroids:
        plt.scatter(clf.centroids[cen][0], clf.centroids[cen][1], marker='o',
                    color='k', s=100, linewidths=5)

    for classification in clf.classifications:
        color = colors[classification]
        for feature_set in clf.classifications[classification]:
            plt.scatter(feature_set[0], feature_set[1], marker='x', color=color, s=150, linewidths=5)

    plt.show()


def main(data):
    colors = 2 * ['g', 'r', 'c', 'b', 'k']
    clf = KMeans()
    clf.fit(data)

    unknowns = np.array([[4, 9]])

    for unknown in unknowns:
        classification = clf.predict(unknown)
        plt.scatter(*unknown, color=colors[classification], marker='*', s=75)

    plot_clf(clf, colors)


if __name__ == '__main__':
    main(X)
