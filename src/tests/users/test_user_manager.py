import pytest


@pytest.mark.django_db
class TestCreateUser:
    def test_create_user(self, django_user_model):
        email = "yarpen@zigrin.com"
        user = django_user_model.objects.create_user(
            email="yarpen@zigrin.com", password="something",
        )

        assert user.is_active
        assert user.is_staff is False
        assert user.is_superuser is False
        assert django_user_model.objects.filter(email=email).exists()

    def test_create_user_without_providing_email(self, django_user_model):
        with pytest.raises(ValueError) as exception:
            django_user_model.objects.create_user(
                email=None, password="something",
            )

        assert str(exception.value) == "The given email must be set."

    def test_create_user_when_field_is_staff_is_true(self, django_user_model):
        email = "yarpen@zigrin.com"
        user = django_user_model.objects.create_user(
            email=email, password="something", is_staff=True, is_superuser=True,
        )

        assert user.is_active
        assert user.is_staff
        assert user.is_superuser
        assert django_user_model.objects.filter(email=email).exists()


@pytest.mark.django_db
class TestCreateSuperUser:
    def test_create_superuser(self, django_user_model):
        email = "yarpen@zigrin.com"
        user = django_user_model.objects.create_superuser(
            email="yarpen@zigrin.com", password="something",
        )

        assert user.is_active
        assert user.is_staff
        assert user.is_superuser
        assert django_user_model.objects.filter(email=email).exists()

    def test_create_superuser_when_field_is_staff_is_false(self, django_user_model):
        email = "yarpen@zigrin.com"
        with pytest.raises(ValueError) as exception:
            django_user_model.objects.create_superuser(
                email=email, password="something", is_staff=False,
            )

        assert str(exception.value) == "Superuser must have is_staff=True."
        assert not django_user_model.objects.filter(email=email).exists()

    def test_create_superuser_when_field_is_superuser_is_false(self, django_user_model):
        email = "yarpen@zigrin.com"
        with pytest.raises(ValueError) as exception:
            django_user_model.objects.create_superuser(
                email=email, password="something", is_superuser=False,
            )

        assert str(exception.value) == "Superuser must have is_superuser=True."
        assert not django_user_model.objects.filter(email=email).exists()
