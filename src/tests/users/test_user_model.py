import pytest

@pytest.mark.django_db
def test_user_model_str(django_user_model):
    user = django_user_model.objects.create(
        email="yarpen@zigrin.com",
        password="something",
    )

    assert str(user) == f"User(id={user.id}, email={user.email})"
