import itertools

class Solution:

    def __init__(self, in_vector):
        """
        The constructor exists only to initialize variables.
        You do not need to change it.
        :param in_vector: The vector given from the file, as a list
        """
        self.in_vector = in_vector

    def output_vector(self):
        """
        This method must be filled in by you. You may add
        other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        :return: a correct output vector, as a Python list
        """

        n = len(self.in_vector)-1
        vector_sum = sum(self.in_vector)
        result = [vector_sum]
        self.in_vector.reverse()

        for i in range(n, 0, -1):
            last_val = self.in_vector[-1]
            vector_sum -= last_val
            result.append(vector_sum)
            self.in_vector.pop()

        return result
