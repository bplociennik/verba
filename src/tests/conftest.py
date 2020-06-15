import pytest

from words.models import Word
from sentences.models import Sentence


@pytest.fixture
@pytest.mark.django_db
def word_fixture():
    word = Word.objects.create(name="lord")
