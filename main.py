def count_words_and_sentences(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Розділяємо текст на слова
    words = text.split()

    # Рахуємо кількість речень
    sentences = text.count('.') + text.count('!') + text.count('?') + text.count('...')

    # Підраховуємо кількість слів
    word_count = len(words)

    return word_count, sentences

# Приклад використання
file_path = "text.txt.txt"  # Змініть шлях до свого файлу
words, sentences = count_words_and_sentences(file_path)
print("Кількість слів:", words)
print("Кількість речень:", sentences)
