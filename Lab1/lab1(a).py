import os

# Перевірка існування файлів
files = ["math.txt", "statistics.txt", "physics.txt", "student_names.txt"]

missing_files = [file for file in files if not os.path.exists(file)]
if missing_files:
    raise FileNotFoundError(f"Відсутні файли: {', '.join(missing_files)}")

# Зчитування даних
subjects = ["math", "statistics", "physics"]
grades = {}
students = []

for subject in subjects:
    with open(f"{subject}.txt", "r", encoding="utf-8") as f:
        grades[subject] = [int(line.strip()) for line in f]

with open("student_names.txt", "r", encoding="utf-8") as f:
    students = [line.strip() for line in f]

# Перевірка, чи кількість студентів співпадає з кількістю оцінок
for subject, scores in grades.items():
    if len(scores) != len(students):
        raise ValueError(f"Кількість оцінок у файлі {subject}.txt не відповідає кількості студентів.")

# Формування результатів
student_data = {}
for i, student in enumerate(students):
    student_data[student] = {
        subject: grades[subject][i] for subject in subjects
    }

# Обчислення середніх оцінок для кожного студента
for student, subjects_scores in student_data.items():
    avg_score = sum(subjects_scores.values()) / len(subjects_scores)
    print(f"Студент: {student}")
    for subject, score in subjects_scores.items():
        print(f"  {subject}: {score}")
    print(f"  Середня оцінка: {avg_score:.2f}")
    print("-" * 40)
