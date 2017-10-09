from Match import Match
import itertools

class Solution:
    
    def __init__(self, m, n, hospital_list, student_list, hosp_open_slots):
        """
            The constructor exists only to initialize variables. You do not need to change it.
            :param m: The number of hospitals
            :param n: The number of students
            :param hospital_list: The preference list of hospitals, as a dictionary.
            :param student_list: The preference list of the students, as a dictionary.
            :param hosp_open_slots: Open slots of each hospital
            """
        self.m = m
        self.n = n
        self.hospital_list = hospital_list
        self.student_list = student_list
        self.hosp_open_slots = hosp_open_slots
    
    def get_matches(self):
        matchings = []
        matchedStudents = {}
        while self.still_has_spots(self.hosp_open_slots.values()):
            for hosp, prefs in self.hospital_list.items():
                if len(self.hospital_list[hosp]) == 0 or self.hosp_open_slots[hosp] == 0:
                    continue
                current_student = self.hospital_list[hosp][0]
                if current_student not in matchedStudents:
                    matchings.append(Match(hosp, current_student))
                    matchedStudents[current_student] = hosp
                    self.hosp_open_slots[hosp] -= 1
                elif self.student_list[current_student].index(hosp) < self.student_list[current_student].index(matchedStudents[current_student]):
                    match_index = self.find_existing_matching_index(matchings, Match(matchedStudents[current_student], current_student))
                    matchings[match_index] = Match(hosp, current_student)
                    self.hosp_open_slots[matchedStudents[current_student]] += 1
                    self.hosp_open_slots[hosp] -= 1 
                    matchedStudents[current_student] = hosp
                del self.hospital_list[hosp][0]

        return matchings

    def still_has_spots(self, slots):
        count = 0
        for i in slots:
            if i > 0:
                count += 1
        return count > 0

    def find_existing_matching_index(self, matchings, current_match):
        for i, match in enumerate(matchings):
            if (match.hospital == current_match.hospital) and (match.student == current_match.student):
                return i
