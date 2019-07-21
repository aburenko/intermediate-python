import numpy as np
import matplotlib.pyplot as plt
import logging as lg

lg.basicConfig(level=lg.INFO)


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
        lg.debug("w: {} b {} np.dot {}".format(self.w, self.b, np.dot(np.array(features), self.w)))
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
        hyp_x_min = data_range[0] * 2
        hyp_x_max = data_range[1] * 2

        psv1 = hyperplane(hyp_x_min, self.w, self.b, 1)
        psv2 = hyperplane(hyp_x_max, self.w, self.b, 1)
        self.ax.plot([hyp_x_min, hyp_x_max], [psv1, psv2])

        nsv1 = hyperplane(hyp_x_min, self.w, self.b, -1)
        nsv2 = hyperplane(hyp_x_max, self.w, self.b, -1)
        self.ax.plot([hyp_x_min, hyp_x_max], [nsv1, nsv2])

        dv1 = hyperplane(hyp_x_min, self.w, self.b, 0)
        dv2 = hyperplane(hyp_x_max, self.w, self.b, 0)
        self.ax.plot([hyp_x_min, hyp_x_max], [dv1, dv2])

        # show vector zero to w
        self.ax.plot([0, self.w[0]], [0, self.w[1]])

        plt.show()

    def fit(self, data):
        self.data = data
        # { |w|: [w, b] }
        opt_dict = {}
        # in this example we are looking only for vectors that are x=y
        # apply(make the product) to the vector of w
        transform = [[1, 1], [-1, 1], [1, -1], [-1, -1]]

        # get max and min values for features data
        all_data = []
        for yi in self.data:
            for feature_set in self.data[yi]:
                for feature in feature_set:
                    all_data.append(feature)

        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        del all_data

        # create steps for search the minimum value
        # for efficient finding the value stepping first
        # with big steps and than with smaller
        step_sizes = [self.max_feature_value * 0.1,
                      self.max_feature_value * 0.01,
                      # point of expense:
                      self.max_feature_value * 0.001]

        # # variables used for stepping with b:
        # extremely expensive
        b_range_multiple = 5
        # we don't need to take as small of steps
        # with b as we do with w
        b_multiple = 5

        latest_optimum = self.max_feature_value * 10

        # stepping process
        for step in step_sizes:
            # corners are gonna be cut here
            w = np.array([latest_optimum, latest_optimum])
            # we can do this because convex so we know where to stop
            optimized = False
            while not optimized:
                # so we are going through all possible values
                # possible values are max feature value with range multiple
                for b in np.arange(-1 * self.max_feature_value * b_range_multiple,
                                   self.max_feature_value * b_range_multiple,
                                   step * b_multiple):
                    # when going with be look all possible transformations
                    for transformation in transform:
                        w_t = w * transformation
                        # weakest link in SVM fundamentally
                        # SMO attempts to fix this a bit
                        # yi(xi.w+b) >= 1
                        found_option = True
                        # so for this moment we are looking for each point in data
                        # and vector w in each fourth of graph for some 'b'
                        # if it match the hyperplane
                        for yi in self.data:
                            if not found_option:
                                break
                            for xi in self.data[yi]:
                                if not yi * (np.dot(w_t, xi) + b) >= 1:
                                    # if one sample is not fitting the definition
                                    # we skipped through the local minimum
                                    found_option = False
                                    break

                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]

                # look if step is already is optimized
                if w[0] < 0:
                    optimized = True
                    print('Optimized a step')
                else:
                    w = w - step
                # this shows it goes up to negative
                # lg.info("w after a step is {}".format(w))

            norms = sorted([n for n in opt_dict])
            # |w| : [w, b]
            # take the smallest norm
            opt_choice = opt_dict[norms[0]]
            self.w = opt_choice[0]
            self.b = opt_choice[1]
            latest_optimum = opt_choice[0][0] + step * 2

        lg.info("fit got w: {} and b {}".format(self.w, self.b))


data_dict = {-1: np.array([[1, 6], [2, 9], [3, 8]]),
             1: np.array([[5, 1], [6, -1], [7, 3]])}


def main(data):
    svm = SupportVectorMachine()
    svm.fit(data=data)

    predict_this = [[0, 10], [6, -5], [5, 8]]

    for p in predict_this:
        svm.predict(p)
        break

    svm.visualize()


if __name__ == '__main__':
    main(data_dict)
