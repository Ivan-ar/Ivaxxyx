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

    # Визначення студентів із середньою оцінкою нижче 50
    low_average_students = []
    for name, scores in students_data.items():
        average_score = sum(scores.values()) / len(scores)
        if average_score < 50:
            low_average_students.append(name)

    # Вивід результатів
    print(f"Загальна кількість студентів із середньою оцінкою нижче 50: {len(low_average_students)}")
    if low_average_students:
        print("Список таких студентів:")
        for student in low_average_students:
            print(f"- {student}")
    else:
        print("Немає студентів із середньою оцінкою нижче 50.")
else:
    print("Не всі файли існують!")
