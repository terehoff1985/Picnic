from collections import defaultdict

# Задание 1: подсчет слов
def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        return len(words)

# Задание 2: поиск самого длинного слова
def find_longest_word(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        longest_word = max(words, key=len)
        return longest_word

# Задание 3: вычисление частоты слов
def word_frequency(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        frequency = defaultdict(int)
        for word in words:
            frequency[word] += 1
        return frequency


filename = 'input.txt'

word_count = count_words(filename)
print("Количество слов в файле:", word_count)

longest_word = find_longest_word(filename)
print("Самое длинное слово в файле:", longest_word)

frequency = word_frequency(filename)
print("Частота слов в файле:")
for word, count in frequency.items():
    print(f"{word}: {count}")
