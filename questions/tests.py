import pytest
from django.urls import reverse
from rest_framework.test import APIClient

client = APIClient()

def test_create_question(db):
    url = reverse("question-list")
    resp = client.post(url, {"text": "test?"}, format="json")
    assert resp.status_code == 201
    assert resp.data["text"] == "test?"

def test_add_answer(db):
    q = client.post(reverse("question-list"), {"text": "q?"}, format="json").data
    url = reverse("question-answers", args=[q["id"]])
    resp = client.post(url, {"text": "a"}, format="json")
    assert resp.status_code == 201
    assert resp.data["text"] == "a"
