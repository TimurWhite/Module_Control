def count_words_and_sentences(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    words = text.split()
    sentences = text.count('.') + text.count('!') + text.count('?') + text.count('...')
    word_count = len(words)
    return word_count, sentences

file_path = "text.txt"
words, sentences = count_words_and_sentences(file_path)
print("Кількість слів:", words)
print("Кількість речень:", sentences)
