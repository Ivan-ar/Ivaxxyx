import os

# Шляхи до файлів
files = ['math.txt', 'statistics.txt', 'physics.txt', 'student_names.txt']

# Перевірка наявності всіх файлів та відкриття
students_data = {}  # Словник для зберігання оцінок студентів
subjects = ['math', 'statistics', 'physics']

if all(os.path.exists(file) for file in files):
    with open('student_names.txt', 'r') as f:
        student_names = [line.strip() for line in f.readlines()]

    # Читання оцінок з кожного файлу
    math_scores = [int(line.strip()) for line in open('math.txt', 'r')]
    statistics_scores = [int(line.strip()) for line in open('statistics.txt', 'r')]
    physics_scores = [int(line.strip()) for line in open('physics.txt', 'r')]

    # Заповнення словника студентів і їх оцінок
    for i, name in enumerate(student_names):
        students_data[name] = {
            'math': math_scores[i],
            'statistics': statistics_scores[i],
            'physics': physics_scores[i]
        }

    # Виведення студента з найвищим балом для кожного предмету
    print("\nСтуденти з найвищими балами для кожного предмету:")
    for subject in subjects:
        max_score = -1
        top_student = ""
        for name, scores in students_data.items():
            if scores[subject] > max_score:
                max_score = scores[subject]
                top_student = name
        print(f"{subject.capitalize()}: студент {top_student}, оцінка {max_score}")

else:
    print("Не всі файли існують!")
