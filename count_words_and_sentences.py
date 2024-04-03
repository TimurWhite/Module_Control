def count_words_and_sentences(text):
    words = text.split()
    sentences = text.count('.') + text.count('!') + text.count('?') + text.count('...')
    word_count = len(words)
    return word_count, sentences
