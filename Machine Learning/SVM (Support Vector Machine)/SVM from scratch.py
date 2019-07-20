import numpy as np
import matplotlib.pyplot as plt


class SupportVectorMachine:
    def __init__(self, vizualization=True):
        self.data = None
        self.max_feature_value = self.min_feature_value = 0
        self.b = 0.0
        self.w = [0, 0]

        self.vizualization = vizualization
        self.colors = {1: 'r', -1: 'b'}
        if vizualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1, 1, 1)

    def predict(self, features):
        classification = np.sign(np.dot(np.array(features), self.w) + self.b)
        if classification != 0 and self.vizualization:
            self.ax.scatter(features[0], features[1], s=200, marker='*', c=self.colors[classification])
        return classification

    def visualize(self):
        [[self.ax.scatter(x[0], x[1], s=100, color=self.colors[i]) for x in data_dict[i]] for i in data_dict]

        # hyperplane = x.w + b
        # v = x.w + b
        # positive support vector = 1
        # nsv = -1
        # dec = 0
        def hyperplane(x, w, b, v):
            return (-w[0] * x - b + v) / w[1]

        data_range = (self.min_feature_value * 0.9, self.max_feature_value * 1.1)
        hyp_x_min = data_range[0]
        hyp_x_max = data_range[1]

        psv1 = hyperplane(hyp_x_min, self.w, self.b, 1)
        psv2 = hyperplane(hyp_x_max, self.w, self.b, 1)
        self.ax.plot([hyp_x_min, hyp_x_max], [psv1, psv2])

        nsv1 = hyperplane(hyp_x_min, self.w, self.b, -1)
        nsv2 = hyperplane(hyp_x_max, self.w, self.b, -1)
        self.ax.plot([hyp_x_min, hyp_x_max], [nsv1, nsv2])

        dv1 = hyperplane(hyp_x_min, self.w, self.b, 0)
        dv2 = hyperplane(hyp_x_max, self.w, self.b, 0)
        self.ax.plot([hyp_x_min, hyp_x_max], [dv1, dv2])

        plt.show()

    def fit(self, data):
        self.data = data
        opt_dict = {}

        transform = [[1, 1], [-1, 1], [1, -1], [-1, -1]]

        all_data = []
        for yi in self.data:
            for feature_set in self.data[yi]:
                for feature in feature_set:
                    all_data.append(feature)

        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)

        del all_data

        step_sizes = [self.max_feature_value * 0.1,
                      self.max_feature_value * 0.01,
                      # point of expense:
                      self.max_feature_value * 0.001]

        # extremely expensive
        b_range_multiple = 5
        # we don't need to take as small of steps
        # with b as we do with w
        b_multiple = 5

        latest_optimum = self.max_feature_value * 10

        # stepping process
        for step in step_sizes:
            w = np.array([latest_optimum, latest_optimum])
            # we can do this because convex
            optimized = False
            while not optimized:
                for b in np.arange(-1 * self.max_feature_value * b_range_multiple,
                                   self.max_feature_value * b_range_multiple,
                                   step * b_multiple):
                    for transformation in transform:
                        w_t = w * transformation
                        # weakest link in SVM fundamentally
                        # SMO attempts to fix this a bit
                        # yi(xi.w+b) >= 1
                        found_option = True
                        for i in self.data:
                            for xi in self.data[i]:
                                yi = i
                                if not yi * (np.dot(w_t, xi) + b) >= 1:
                                    found_option = False

                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]

                if w[0] < 0:
                    optimized = True
                    print('Optimized a step')
                else:
                    w = w - step

            norms = sorted([n for n in opt_dict])
            # |w| : [w, b]
            opt_choice = opt_dict[norms[0]]
            self.w = opt_choice[0]
            self.b = opt_choice[1]
            latest_optimum = opt_choice[0][0] + step * 2


data_dict = {-1: np.array([[1, 7], [2, 8], [3, 8]]),
             1: np.array([[5, 1], [6, -1], [7, 3]])}


def main(data):
    svm = SupportVectorMachine()
    svm.fit(data=data)

    predict_this = [[0, 10], [6, -5], [5, 8]]

    for p in predict_this:
        svm.predict(p)

    svm.visualize()


if __name__ == '__main__':
    main(data_dict)
