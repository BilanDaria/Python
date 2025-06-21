class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        if len(self.grades) == 0:
            return 0
        else:
            average_grade = sum(self.grades) / len(self.grades)
            return average_grade

    def __str__(self):
        return (f"Student name: {self.name}\n"
                f"Student grades: {self.grades}\n"
                f"Average grade: {self.average():.2f}")
