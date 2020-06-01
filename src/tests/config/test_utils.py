import pytest
from config.utils import upload_to_classname
from words.models import Word


@pytest.mark.parametrize("instance,filename", [(Word, "picture.png")])
def test_upload_to_classname_function(instance, filename):
    assert upload_to_classname(instance, filename) == "word/picture.png"
