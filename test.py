import re

text = "\ncat catch cats concatenate"

# БЕЗ \b - найдёт подстроки
matches = re.findall(r'cat', text)
print("Без \\b:", matches)
# Вывод: ['cat', 'cat', 'cat', 'cat']
# Нашло во всех словах!

# С \b - только целое слово
matches = re.findall(r'[]cat\b', text)
print("С \\b:", matches)
# Вывод: ['cat']
# Только отдельное слово!