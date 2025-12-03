
import re
import csv
from typing import List


TASK1_FILE = 'task1-en.txt'
TASK2_FILE = 'task2.html'
TASK3_FILE = 'task3.txt'
OUTPUT_FILE = 'output.csv'

def task1_find_patterns(filename: str) -> List[str]:

    with open(filename, encoding='utf-8') as f:
        text = f.read()

    pattern = r'[0-9]+[.,][0-9]+|[0-9]+|[¼]|\b[A-Za-z]{8}\b|\b[A-Za-z]{6}\b'
    matches = re.findall(pattern, text)

    return matches


def task2_extract_content(filename: str) -> List[str]:

    with open(filename, encoding='utf-8') as f:
        text = f.read()

    # Паттерн для извлечения значения атрибута content
    pattern = r'content="([^"]*)"'
    matches = re.findall(pattern, text)

    return matches


def task3_extract_user_data(filename: str) -> dict:

    with open(filename, encoding='utf-8') as f:
        text = f.read()

    patterns = {
        'id': r' ([0-9]+)(?= )',
        'surname': r' ([a-zA-Z]+)(?= )',
        'email': r' ([a-zA-Z0-9-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+)(?= )',
        'date': r'\b[0-9]+-[0-9]+-[0-9]+\b',
        'website': r'https?://[a-zA-Z0-9.-]+/'
    }

    data = {
        'id': re.findall(patterns['id'], text),
        'surname': re.findall(patterns['surname'], text),
        'email': re.findall(patterns['email'], text),
        'date': re.findall(patterns['date'], text),
        'website': re.findall(patterns['website'], text)
    }

    return data


def save_to_csv(data: dict, filename: str) -> None:

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Заголовки
        headers = ['ID', 'Фамилия', 'Почта', 'Дата регистрации', 'Сайт']
        writer.writerow(headers)

        # Данные (транспонируем массивы с помощью zip)
        for row in zip(
            data['id'],
            data['surname'],
            data['email'],
            data['date'],
            data['website']
        ):
            writer.writerow(row)


if __name__ == '__main__':
    # Задание 1
    matches1 = task1_find_patterns(TASK1_FILE)
    print(f"Задание 1: найдено {len(matches1)} совпадений")

    # Задание 2
    matches2 = task2_extract_content(TASK2_FILE)
    print(f"Задание 2: найдено {len(matches2)} атрибутов content")

    # Задание 3
    user_data = task3_extract_user_data(TASK3_FILE)
    print(f"Задание 3: найдено {len(user_data['website'])} записей")

    # Сохранение результатов в CSV
    save_to_csv(user_data, OUTPUT_FILE)
