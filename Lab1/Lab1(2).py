import os

# Шляхи до файлів
files = ['math.txt', 'statistics.txt', 'physics.txt', 'student_names.txt']

# Перевірка наявності всіх файлів та відкриття
students_data = {}  # Словник для зберігання оцінок студентів
subjects = ['math', 'statistics', 'physics']

# Читаємо файли з оцінками та іменами студентів
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

    # Обчислення середніх оцінок
    student_averages = {
        name: sum(scores.values()) / len(scores)
        for name, scores in students_data.items()
    }

    # Сортуємо студентів за середньою оцінкою у спадному порядку
    sorted_students = sorted(student_averages.items(), key=lambda x: x[1], reverse=True)

    # Отримуємо трьох студентів з найвищими середніми оцінками
    top_students = sorted_students[:3]

    # Виведення результатів
    print("\nТри студенти з найвищими середніми оцінками:")
    for rank, (name, average) in enumerate(top_students, start=1):
        print(f"{rank}. {name}: середня оцінка {average:.2f}")

else:
    print("Не всі файли існують!")
