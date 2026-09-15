import statistics

class Question:
    def __init__(self, answer):
        self.answer = answer.answer if isinstance(answer, Question) else answer
    def grade(self, correct):
        return int(self.answer == (correct.answer if isinstance(correct, Question) else correct))

class Test:
    def __init__(self, answers, answerKey):
        self.answers = answers
        self.answerKey = answerKey
    def score(self):
        matches = sum(q.grade(k) for q, k in zip(self.answers, self.answerKey))
        return (matches / len(self.answerKey)) * 100

key = [Question(c) for c in input()]
tests = [
    Test([Question(c) for c in input()], key)
    for _ in range(int(input()))
]

grades = [t.score() for t in tests]
correctCounts = [
    sum(t.answers[i].grade(key[i]) for t in tests)
    for i in range(len(key))
]

print(f"High Score = {max(grades):.1f}")
print(f"Median Score = {statistics.median(grades):.1f}")
print(f"Question Number Answered Most Correctly = {correctCounts.index(max(correctCounts)) + 1}")
print(f"Question Number Answered Most Incorrectly = {correctCounts.index(min(correctCounts)) + 1}")
