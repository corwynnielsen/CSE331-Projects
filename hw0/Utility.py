import re

class Utility:
    
    def read_file(self, input_file):
        
        f = open(input_file, 'r')
        line = f.readlines()
        outputList = [x.strip() for x in line[0].split(',')]

        return outputList
