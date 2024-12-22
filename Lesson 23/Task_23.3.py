import sys
sys.stdout.reconfigure(encoding='utf-8')

class Student:
    def __init__(self, name):
        self._name = name
        self._scores = []

    def add_score(self, score):
        if 0 <= score <= 100:
            self._scores.append(score)
            print(f"{self._name}-ს დაემატა {score} ქულა.")
        else:
            print("არასწორი ქულა.")

    def get_average(self):
        if self._scores:
            return sum(self._scores) / len(self._scores)
        return 0

    def get_scores(self):
        return self._scores

students = [
    Student("გიორგი"),
    Student("მარიამი"),
    Student("დავითი")
]

students[0].add_score(85)
students[0].add_score(90)
students[0].add_score(78)

students[1].add_score(95)
students[1].add_score(88)
students[1].add_score(102)

students[2].add_score(72)
students[2].add_score(68)
students[2].add_score(75)

for student in students:
    print(f"{student._name}-ს საშუალო ქულაა: {student.get_average():.1f}")

new_student = Student("თამარი")
new_student.add_score(92)
new_student.add_score(89)
print(f"{new_student._name}-ს საშუალო ქულაა: {new_student.get_average():.1f}")

for student in students + [new_student]:
    print(f"{student._name}-ს ქულებია: {student.get_scores()}")
