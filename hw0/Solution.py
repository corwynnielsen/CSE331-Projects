class Solution:

    def __init__(self, ip):
        """
            The constructor exists only to initialize variables. You do not need to change it.
            :param ip: input list that consists of n element from {A,B}
        """
        self.inputList = ip

    def outputSortedList(self, A, B, n):
        # self.printList(self.inputList)
        self.inputList.sort()
        # self.printList(self.inputList)
        return self.inputList

    def printList(self, input):
        for i in input:
            print(i)
        print('\n')