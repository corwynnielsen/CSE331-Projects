import sys
from Solution import Solution

def read_file(filename):
    listOfRallies = []
    with open(filename, 'r') as input_file:
        next(input_file)
        for line in input_file:
            values = [int(value) for value in line.split()]
            rally = (values[0], values[1],)
            listOfRallies.append(rally)
    return listOfRallies

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the testcase filepath as a command line argument.")
    else:
        rallies = read_file(sys.argv[1])
        sol = Solution(rallies).getSchedule()
        print("Your Solution:")
        print("============================================================================")
        print(sol)
        print("============================================================================")
