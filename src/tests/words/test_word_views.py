from django.urls import reverse

import pytest


@pytest.mark.django_db
class TestWordCreateView:
    def test_create_word_without_permissions(self, client):
        response = client.post(reverse("word-list"), data={"name": "tree"})
        assert response.status_code == 403


@pytest.mark.django_db
class TestWordListView:
    def test_list_word_without_permissions(self, client):
        response = client.get(reverse("word-list"))
        assert response.status_code == 403
