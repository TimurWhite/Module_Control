import pytest
from count_words_and_sentences import count_words_and_sentences

@pytest.mark.parametrize("input_text,expected_words,expected_sentences", [
    ("test sentence.", 5, 1),
    ("another test sentence, more words!", 8, 2),
    ("1,2,3,4...", 4, 4),
])
def test_count_words_and_sentences(input_text, expected_words, expected_sentences):
    words, sentences = count_words_and_sentences(input_text)
    assert words == expected_words
    assert sentences == expected_sentences

def test_empty_input():
    words, sentences = count_words_and_sentences("")
    assert words == 0
    assert sentences == 0

def test_special_characters_only():
    words, sentences = count_words_and_sentences("!@#$%^&*()")
    assert words == 0
    assert sentences == 0
