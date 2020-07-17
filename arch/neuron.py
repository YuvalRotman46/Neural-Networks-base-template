import numpy as np


class Neuron:

    def __init__(self, inputs_n, weights=None,):

        if weights is None:
            self.weights = np.random.random(inputs_n)
        else:
            self.weights = weights

        self.inputs_n = inputs_n
