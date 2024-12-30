# Створимо тестовий файл netflix_list.csv
csv_content = """title,type,rating,numVotes,language,endYear,numEpisodes,cast,isAdult
Stranger Things,Show,8.7,1200000,English,2022,34,Winona Ryder; David Harbour,0
The Witcher,Show,8.2,800000,English,2023,16,Henry Cavill; Anya Chalotra,0
Breaking Bad,Show,9.5,1800000,English,2013,62,Bryan Cranston; Aaron Paul,1
The Crown,Show,8.6,250000,English,2022,60,Olivia Colman; Claire Foy,0
Dark,Show,8.8,400000,German,2020,26,Louis Hofmann; Lisa Vicari,0
The Irishman,Movie,7.9,350000,English,2019,1,Robert De Niro; Al Pacino,0
Roma,Movie,7.7,150000,Spanish,2018,1,Yalitza Aparicio; Marina de Tavira,0
Bird Box,Movie,6.6,300000,English,2018,1,Sandra Bullock; Trevante Rhodes,0
"""
with open('netflix_list.csv', 'w', encoding='utf-8') as f:
    f.write(csv_content)

# Зчитування файлу
with open('netflix_list.csv', 'r', encoding='utf-8') as file:
    data = [line.strip().split(',') for line in file]

headers = data[0]
rows = data[1:]

# Завдання 1.a: Фільтрація за рейтингом > 7.5
high_rating = [row for row in rows if float(row[headers.index('rating')]) > 7.5]

# Завдання 1.b: Перші 5 колонок
shortened_rows = [row[:5] for row in rows]

# Завдання 2: Генератор для фільтрації за мовою і роком
def filter_by_language_and_year(rows, headers):
    for row in rows:
        try:
            if (row[headers.index('language')] == 'English' and
                int(row[headers.index('endYear')]) > 2015):
                yield row
        except (ValueError, IndexError):
            continue

filtered_data = list(filter_by_language_and_year(rows, headers))

# Завдання 3: Ітератор для акторського складу
class CastIterator:
    def __init__(self, rows, headers):
        self.rows = rows
        self.headers = headers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.rows):
            cast = self.rows[self.index][headers.index('cast')]
            self.index += 1
            if len(cast) > 50:
                return cast
        raise StopIteration

# Безпечне отримання довгих записів
cast_iterator = CastIterator(rows, headers)
long_casts = []

try:
    while len(long_casts) < 10:
        long_casts.append(next(cast_iterator))
except StopIteration:
    pass

# Завдання 4: Статистика
def calculate_stats(rows, headers):
    try:
        adult_count = sum(1 for row in rows if int(row[headers.index('isAdult')]) == 1)
        high_votes = [float(row[headers.index('rating')]) for row in rows if int(row[headers.index('numVotes')]) > 1000]
        avg_rating = sum(high_votes) / len(high_votes) if high_votes else 0
    except (ValueError, IndexError):
        adult_count, avg_rating = 0, 0
    return adult_count, avg_rating

adult_count, avg_rating = calculate_stats(rows, headers)

# Завдання 5: Заголовки шоу
avg_rating_all = sum(float(row[headers.index('rating')]) for row in rows) / len(rows)
titles = [row[headers.index('title')] for row in rows if int(row[headers.index('numEpisodes')]) > 10 and float(row[headers.index('rating')]) > avg_rating_all]

# Вивід результатів
print("Шоу з рейтингом > 7.5:", high_rating)
print("Перші 5 колонок кожного рядка:", shortened_rows[:5])
print("Відфільтровані дані (English, після 2015):", filtered_data[:5])
print("Довгі записи акторського складу (перші 10):", long_casts)
print("Кількість дорослих шоу:", adult_count)
print("Середній рейтинг шоу з більше ніж 1000 голосів:", avg_rating)
print("Заголовки шоу з > 10 епізодами та рейтингом вище середнього:", titles)
