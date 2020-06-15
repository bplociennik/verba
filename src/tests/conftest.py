import pytest
from words.models import Word


@pytest.fixture
@pytest.mark.django_db
def word_fixture():
    Word.objects.create(name="lord")
