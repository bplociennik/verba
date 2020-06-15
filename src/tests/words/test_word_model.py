import pytest
from words.models import Word


@pytest.mark.django_db
def test_word_model_str():
    word_name = "lord"
    word = Word.objects.create(name=word_name)
    assert str(word) == f"Word(id={word.id}, name={word_name})"
