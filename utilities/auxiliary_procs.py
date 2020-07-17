import numpy as np

"""
@:param A length for the vector
@:return The zeroed vector

The subroutine returns a zeroed vector of [length] dimensions.
"""
def get_zeroed_vector(length):
    return np.array([0 for i in range(length)])