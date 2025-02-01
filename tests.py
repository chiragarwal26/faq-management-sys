import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_translation():
    faq = FAQ.objects.create(
        question_en='What is Django?',
        answer_en='A web framework.',
    )
    faq.save()
    assert faq.question_hi != ''
    assert faq.answer_hi != ''

@pytest.mark.django_db
def test_faq_api():
    client = APIClient()
    faq = FAQ.objects.create(
        question_en='Test',
        answer_en='Test answer',
    )
    faq.save()
    response = client.get('/api/faqs/?lang=en')
    assert response.status_code == 200
    assert response.data[0]['question'] == 'Test'