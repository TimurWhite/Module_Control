import pytest
from main import count_words_and_sentences

@pytest.fixture
def text_file():
    text = "The Large Hadron Collider (LHC) is the world's largest and highest-energy particle collider. It was built by the European Organization for Nuclear Research (CERN) between 1998 and 2008 in collaboration with over 10,000 scientists and hundreds of universities and laboratories across more than 100 countries. It lies in a tunnel 27 kilometres (17 mi) in circumference and as deep as 175 metres (574 ft) beneath the France–Switzerland border near Geneva."
    file_path = "text.txt"
    with open(file_path, "w") as file:
        file.write(text)
    yield file_path

def test_count_words_and_sentences(text_file):
    words, sentences = count_words_and_sentences(text_file)
    assert words == 70
    assert sentences == 3
