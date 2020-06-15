import pytest

from words.models import Word
from sentences.models import Sentence


@pytest.mark.django_db
def test_sentence_model_str():
    word_name = "lord"
    word = Word.objects.create(name=word_name)
    sentence = Sentence.objects.create(
        word=word, name="He always brags about being a lord."
    )
    assert str(sentence) == f"Sentence(id={sentence.id}, word={word_name})"
