import pandas as pd

# Загрузка данных из CSV-файла
file_path = '/Users/elizarov09/Desktop/PytonProject/myvenv/AZ01_DATA/Data_eng_salary.csv'
data = pd.read_csv(file_path)

# Преобразование всех числовых столбцов в целые числа
for col in data.columns:
    if data[col].dtype == 'float64' or data[col].dtype == 'float32':
        data[col] = data[col].round().astype(int)

# Вывод первых 5 строк данных
first_five_rows = data.head()
print(first_five_rows)

# Получение информации о данных
data_info = data.info()
print(data_info)

# Статистическое описание данных
data_description = data.describe().astype(int)  # Явное преобразование результатов в целые числа
print(data_description)

# Общее количество вакансий по годам
jobs_per_year = data['work_year'].value_counts()
print(jobs_per_year)

# Группировка по названию должности (job_title)
grouped_by_job = data.groupby('job_title').agg({'job_title': 'count', 'salary_in_usd': 'mean'}).rename(columns={'job_title': 'count', 'salary_in_usd': 'average_salary'}).astype({'average_salary': 'int'})
print(grouped_by_job)

# Группировка по уровню опыта (experience_level)
grouped_by_experience = data.groupby('experience_level').agg({'experience_level': 'count', 'salary_in_usd': 'mean'}).rename(columns={'experience_level': 'count', 'salary_in_usd': 'average_salary'}).astype({'average_salary': 'int'})
print(grouped_by_experience)
