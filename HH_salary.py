import pandas as pd

# Загрузка данных из CSV-файла
file_path_hh = '/Users/elizarov09/Desktop/PytonProject/myvenv/AZ01_DATA/dz.csv'
data_hh = pd.read_csv(file_path_hh)

# Очистка данных от пустых значений в столбцах 'City' и 'Salary'
data_hh.dropna(subset=['City', 'Salary'], inplace=True)

# Преобразование зарплаты в числовой тип, если необходимо
data_hh['Salary'] = pd.to_numeric(data_hh['Salary'], errors='coerce')
data_hh.dropna(subset=['Salary'], inplace=True)  # Удаление строк, где зарплата не удалось преобразовать в число

# Определение средней зарплаты по городам
average_salary_by_city = data_hh.groupby('City')['Salary'].mean().reset_index()

# Вывод результата
print(average_salary_by_city)
