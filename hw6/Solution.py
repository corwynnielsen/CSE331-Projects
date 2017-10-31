class Solution:
    
    def __init__(self, listOfRallies):
        self.rallies = listOfRallies
    
    def getSchedule(self):
        result = []
        enumerated = list(enumerate(self.rallies))
        enumerated.sort(key=lambda x: x[1][1])

        current_time = 0
        for rally in enumerated:
            duration = rally[1][0]
            deadline = rally[1][1]
            if current_time + duration > deadline:
                return []
            result.append((rally[0], current_time))
            current_time += duration
        return result

