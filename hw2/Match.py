class Match:

    def __init__(self, hospital_val, student_val):
        self.hospital = hospital_val
        self.student = student_val

    def hospital(self):
        return self.hospital
    def student(self):
        return self.student

    def equals(self, match):
        return (match.hospital == self.hospital) and (match.student == self.student)

    def __str__(self):
        return "(" + str(self.hospital) + ", " + str(self.student) + ")"

    __repr__ = __str__

    def __lt__(self, other):
        return self.hospital < other.hospital

    def __eq__(self, other):
        return self.student == other.student and self.hospital == other.hospital
